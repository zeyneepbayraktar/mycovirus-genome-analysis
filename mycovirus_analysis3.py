import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from Bio import Entrez, SeqIO

Entrez.email = "your@email.com"

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
    record_protein = SeqIO.read(handle, "genbank")
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

with open("rdp_sequences.fasta", "w") as f:
    for accession, seq in rdp_sequences.items():
        f.write(f">{accession}\n{seq}\n")