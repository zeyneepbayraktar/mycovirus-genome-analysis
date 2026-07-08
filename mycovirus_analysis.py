import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from Bio import Entrez, SeqIO

Entrez.email = "your@email.com"

#  bir mycovirus sequence'i çek
accession = "PP389084.1"

handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

# Temel bilgileri yazdır
print("ID:", record.id)
print("Açıklama:", record.description)
print("Uzunluk:", len(record.seq), "bp")
print("İlk 50 baz:", record.seq[:50])

# GC içeriği hesapla
from Bio.SeqUtils import gc_fraction
gc = gc_fraction(record.seq) * 100
print(f"GC içeriği: {gc:.2f}%")

print("\n--- FEATURE'LAR ---")
for feature in record.features:
    print(feature.type, "→", feature.location)
    if "product" in feature.qualifiers:
        print("   Ürün:", feature.qualifiers["product"][0])
    if "protein_id" in feature.qualifiers:
        print("   Protein ID:", feature.qualifiers["protein_id"][0])

print("\n--- POLYPROTEİN ---")
for feature in record.features:
    if feature.type == "CDS":
        protein_seq = feature.qualifiers["translation"][0]
        print("Protein uzunluğu:", len(protein_seq), "aa")
        print("İlk 30 amino asit:", protein_seq[:30])

