# fasta-stats

Compute basic statistics from FASTA files.

`fasta-stats` is a lightweight command-line bioinformatics tool written in Python.  
It calculates descriptive statistics from nucleotide FASTA files in a fast and reproducible way.

---

## 🚀 Features

- Count number of sequences
- Compute total sequence length
- Calculate average sequence length
- Estimate GC content (%)
- Simple command-line interface
- No external bioinformatics dependencies

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fasta-stats.git
cd fasta-stats

python -m venv venv
source venv/bin/activate

pip install .

fasta-stats example_data/test.fasta


Sequences      : 25
Total length   : 4320000
Average length : 172800.00
GC content     : 51.23%

fasta-stats/
│
├── README.md
├── CHANGELOG.md
├── setup.py
├── requirements.txt
│
├── fasta_stats/
│   ├── __init__.py
│   ├── parser.py
│   ├── stats.py
│   └── cli.py
│
└── example_data/
