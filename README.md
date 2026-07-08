# Mycovirus Genome Analysis

🇬🇧 **English** | 🇹🇷 **Türkçe**

---

## 🇬🇧 English

This repository documents my steps in learning bioinformatics through real genomic data.

Using BioPython and the NCBI Entrez API, I fetched real mycovirus sequences discovered by researchers working on fungal viruses. I examined the basic properties of virus sequences (length, GC content, features), printed annotation data (UTR regions, CDS, polyprotein), and explored functional domains.

### What's been done so far

**Step 1 — Single sequence analysis (PP389084.1)**
- Fetched *Terfezia claveryi flexivirus 1* genome from NCBI
- Extracted basic metrics: length (9792 bp), GC content (56.02%), first 50 bases
- Read GenBank annotation: 5'UTR, CDS (polyprotein), 3'UTR
- Fetched protein record (WWL46803.1) and mapped functional domains: methyltransferase, helicase, RdRp

**Step 2 — Pairwise RdRp comparison (PP389084.1 vs PP389085.1)**
- Fetched a second mycovirus (*Terfezia claveryi endornavirus 1*) from the same host fungus
- Extracted RdRp domain from both polyproteins using GenBank region annotations
- Performed pairwise alignment using BioPython's `PairwiseAligner`
- Calculated normalized similarity score: **~9.47%** — confirming evolutionary distance between Flexiviridae and Endornaviridae

**Step 3 — Multi-virus RdRp extraction pipeline**
- Searched NCBI for all mycovirus sequences from the same research group
- Built an automated pipeline to fetch 8 virus genomes, extract protein IDs, locate RdRp domains, and extract sequences
- Saved all 8 RdRp sequences to `rdp_sequences.fasta` for downstream analysis

### Viruses analyzed

| Accession | Virus | Host |
|---|---|---|
| PP389084.1 | Terfezia claveryi flexivirus 1 | Terfezia claveryi |
| PP389085.1 | Terfezia claveryi endornavirus 1 | Terfezia claveryi |
| NC_116531.1 | Picoa juniperi mycovirus 1 | Picoa juniperi |
| MT764202.1 | Caloscypha fulgens mycovirus 2 | Caloscypha fulgens |
| MT764195.1 | Caloscypha fulgens mycovirus 1 | Caloscypha fulgens |
| MT764194.1 | Caloscypha fulgens mycovirus A | Caloscypha fulgens |
| MT876191.1 | Picoa juniperi mycovirus 2 | Picoa juniperi |
| MT876190.1 | Picoa juniperi mycovirus 1 | Picoa juniperi |

### Next step
Multiple sequence alignment of all 8 RdRp sequences → phylogenetic tree

### Tools & Libraries
- Python 3
- BioPython (Entrez, SeqIO, PairwiseAligner)
- NCBI GenBank / Protein databases

---

## 🇹🇷 Türkçe

Bu repoda biyoinformatik öğrenme yolculuğumun adımlarını görebilirsiniz.

BioPython ve NCBI Entrez API kullanarak mantar virüsleri (mycovirus) üzerine çalışan araştırmacıların keşfettiği gerçek virüs sequence'lerini çektim.

### Şimdiye kadar yapılanlar

**Adım 1 — Tek sequence analizi (PP389084.1)**
- *Terfezia claveryi flexivirus 1* genomunu NCBI'dan çektim
- Temel metrikler: uzunluk (9792 bp), GC içeriği (%56.02), ilk 50 baz
- GenBank annotation okuma: 5'UTR, CDS (polyprotein), 3'UTR
- Protein kaydı (WWL46803.1) çekilerek fonksiyonel domain haritası çıkarıldı

**Adım 2 — İkili RdRp karşılaştırması**
- Aynı konakçı mantardan ikinci bir virüs (*Terfezia claveryi endornavirus 1*) çekildi
- Her iki virüsün polyproteininden RdRp domain'i çıkarıldı
- BioPython `PairwiseAligner` ile pairwise alignment yapıldı
- Normalize benzerlik skoru: **~%9.47** — iki virüsün evrimsel olarak uzak ailelere ait olduğunu doğruladı

**Adım 3 — Çoklu virüs RdRp çıkarma pipeline'ı**
- Aynı araştırma grubuna ait tüm mycovirus sequence'leri NCBI'da arandı
- 8 virüs genomundan otomatik olarak protein ID'leri alındı, RdRp domain'leri bulundu ve sequence'ler çıkarıldı
- Tüm 8 RdRp sequence'i `rdp_sequences.fasta` dosyasına kaydedildi

### Analiz edilen virüsler

| Accession | Virüs | Konakçı |
|---|---|---|
| PP389084.1 | Terfezia claveryi flexivirus 1 | Terfezia claveryi |
| PP389085.1 | Terfezia claveryi endornavirus 1 | Terfezia claveryi |
| NC_116531.1 | Picoa juniperi mycovirus 1 | Picoa juniperi |
| MT764202.1 | Caloscypha fulgens mycovirus 2 | Caloscypha fulgens |
| MT764195.1 | Caloscypha fulgens mycovirus 1 | Caloscypha fulgens |
| MT764194.1 | Caloscypha fulgens mycovirus A | Caloscypha fulgens |
| MT876191.1 | Picoa juniperi mycovirus 2 | Picoa juniperi |
| MT876190.1 | Picoa juniperi mycovirus 1 | Picoa juniperi |

### Sıradaki adım
8 RdRp sequence'inin multiple sequence alignment'ı → filogenetik ağaç

### Kullanılan Araçlar
- Python 3
- BioPython (Entrez, SeqIO, PairwiseAligner)
- NCBI GenBank / Protein veritabanları
