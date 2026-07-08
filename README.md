# Mycovirus Genome Analysis

🇬🇧 **English** | 🇹🇷 **Türkçe**

---

## 🇬🇧 English

This repository documents my steps in learning bioinformatics through real genomic data.

Using BioPython and the NCBI Entrez API, I fetched real mycovirus sequences discovered by researchers working on fungal viruses. I examined the basic properties of a virus sequence (length, GC content, features), printed its annotation data (UTR regions, CDS, polyprotein), and explored its functional domains.

In the second part, I compared the **RdRp (RNA-dependent RNA Polymerase)** regions of two different mycoviruses isolated from the same host fungus (*Terfezia claveryi*):

- **PP389084.1** — *Terfezia claveryi flexivirus 1*
- **PP389085.1** — *Terfezia claveryi endornavirus 1*

I extracted the RdRp domain from each virus's polyprotein, performed pairwise alignment using BioPython's `PairwiseAligner`, and calculated a normalized similarity score.

**Result:** ~9.47% similarity — confirming that despite sharing the same host, these two viruses belong to evolutionarily distant families (Flexiviridae vs Endornaviridae).

### Tools & Libraries
- Python 3
- BioPython (Entrez, SeqIO, PairwiseAligner)
- NCBI GenBank / Protein databases

---

## 🇹🇷 Türkçe

Bu repoda biyoinformatik öğrenme yolculuğumun adımlarını görebilirsiniz.

BioPython ve NCBI Entrez API kullanarak mantar virüsleri (mycovirus) üzerine çalışan araştırmacıların keşfettiği gerçek virus sequencelerini çektim. Bir virüsün temel bilgilerini (uzunluk, GC içeriği, feature'lar), annotation verilerini (UTR bölgeleri, CDS, polyprotein) ve fonksiyonel domain haritasını inceledim.

İkinci aşamada, aynı konakçı mantardan (*Terfezia claveryi*) izole edilen iki farklı mycovirusun **RdRp (RNA-bağımlı RNA polimeraz)** bölgelerini karşılaştırdım:

- **PP389084.1** — *Terfezia claveryi flexivirus 1*
- **PP389085.1** — *Terfezia claveryi endornavirus 1*

Her iki virusun polyproteininden RdRp domain'ini çıkardım, BioPython'ın `PairwiseAligner`'ı ile pairwise alignment yaptım ve normalize benzerlik skorunu hesapladım.

**Sonuç:** ~%9.47 benzerlik — aynı konakçıyı paylaşmalarına rağmen bu iki virusun evrimsel olarak uzak ailelere ait olduğunu doğruladı (Flexiviridae vs Endornaviridae).

### Kullanılan Araçlar
- Python 3
- BioPython (Entrez, SeqIO, PairwiseAligner)
- NCBI GenBank / Protein veritabanları
