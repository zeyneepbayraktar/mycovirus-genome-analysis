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