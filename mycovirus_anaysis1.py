import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from Bio import Entrez, SeqIO

Entrez.email = "your@email.com"

handle = Entrez.efetch(db="protein", id="WWL46803.1", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

print("ID:", record.id)
print("Açıklama:", record.description)
print("Uzunluk:", len(record.seq), "aa")
print("İlk 30 amino asit:", record.seq[:30])

print("\n--- FEATURE'LAR ---")
for feature in record.features:
    print(feature.type, "→", feature.location)
    for key, value in feature.qualifiers.items():
        print(f"   {key}: {value[0]}")