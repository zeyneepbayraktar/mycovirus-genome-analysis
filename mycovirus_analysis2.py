import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from Bio import Entrez, SeqIO
from Bio.Align import PairwiseAligner

Entrez.email = "your@email.com"

accession = "PP389084.1"

handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

print("ID:", record.id)
print("Açıklama:", record.description)
print("Uzunluk:", len(record.seq), "bp")
print("İlk 50 baz:", record.seq[:50])

accession2 = "PP389085.1"

handle = Entrez.efetch(db="nucleotide", id=accession2, rettype="gb", retmode="text")
record2 = SeqIO.read(handle, "genbank")
handle.close()

print("ID:", record2.id)
print("Açıklama:", record2.description)
print("Uzunluk:", len(record2.seq), "bp")
print("İlk 50 baz:", record2.seq[:50])

for feature in record.features:
    if feature.type == "CDS":
        protein_seq = feature.qualifiers["translation"][0]
        print("Protein uzunluğu:", len(protein_seq), "aa")
        print("İlk 30 amino asit:", protein_seq[:30])

for feature in record2.features:
    if feature.type == "CDS":
        protein_seq = feature.qualifiers["translation"][0]
        print("Protein uzunluğu:", len(protein_seq), "aa")
        print("İlk 30 amino asit:", protein_seq[:30])
    for key, value in feature.qualifiers.items():
        print(f"   {key}: {value[0]}")

handle = Entrez.efetch(db="protein", id="WWL46803.1", rettype="gb", retmode="text")
record_protein1 = SeqIO.read(handle, "genbank")
handle.close()

print("\n--- WWL46803.1 FEATURE'LAR ---")
for feature in record_protein1.features:
    print(feature.type, "→", feature.location)
    for key, value in feature.qualifiers.items():
        print(f"   {key}: {value[0]}")

handle = Entrez.efetch(db="protein", id="WWL46804.1", rettype="gb", retmode="text")
record_protein2= SeqIO.read(handle, "genbank")
handle.close()

for feature in record_protein2.features:
    print(feature.type, "→", feature.location)
    for key, value in feature.qualifiers.items():
        print(f"   {key}: {value[0]}")

rdp1 = record_protein1.seq[2835:3089]
rdp2 = record_protein2.seq[5043:5286]
print("RdRp Bölgesi:",record_protein1.seq[2835:3089])
print("RdRp Bölgesi:", record_protein2.seq[5043:5286])

aligner = PairwiseAligner()
score = aligner.score(rdp1, rdp2)
print("Benzerlik skoru:", score)
max_score = min(len(rdp1), len(rdp2))
similarity = (score / max_score) * 100
print(f"Normalize benzerlik: {similarity:.2f}%")

print("\n--- NCBI SEQUENCE'LERİ ---")
handle = Entrez.esearch(db="nucleotide", term="Sahin E[Author] mycovirus", retmax=50)
search_record = Entrez.read(handle)
handle.close()

print("Toplam sonuç:", search_record["Count"])
print("ID'ler:", search_record["IdList"])

handle = Entrez.efetch(db="nucleotide", id=search_record["IdList"], rettype="acc", retmode="text")
print(handle.read())
handle.close()

handle = Entrez.efetch(db="nucleotide", id=search_record["IdList"], rettype="gb", retmode="text")
records = list(SeqIO.parse(handle, "genbank"))
handle.close()

for r in records:
    print(r.id, "→", r.description)

all_accessions = [
    "PP389084.1",
    "PP389085.1", 
    "NC_116531.1",
    "MT764202.1",
    "MT764195.1",
    "MT764194.1",
    "MT876191.1",
    "MT876190.1"
]

rdp_sequences = {}

for accession in all_accessions:
    print(accession)
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    for feature in record.features:
        if feature.type == "CDS":
            protein_id = feature.qualifiers["protein_id"][0]
    handle = Entrez.efetch(db="protein", id=protein_id, rettype="gb", retmode="text")
    record_protein= SeqIO.read(handle, "genbank")
    handle.close()
    for feature in record_protein.features:
        if feature.type == "Region":
            if "region_name" in feature.qualifiers:
                if "RdRp" in feature.qualifiers["region_name"][0]:
                   print("RdRp bulundu:", feature.location)
    start = feature.location.start
    end = feature.location.end
    rdp_seq = record_protein.seq[start:end]
    print("RdRp sequence:", rdp_seq[:30])
    rdp_sequences[accession] = str(rdp_seq)

print(rdp_sequences)

with open("rdp_sequences.fasta", "w") as f:
    for accession, seq in rdp_sequences.items():
        f.write(f">{accession}\n{seq}\n")

