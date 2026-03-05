# fasta-stats

Bioinformatics tool to compute statistics for FASTA/FASTQ files (support gzipped files).

**Author:** ndaosif / bioinfosif  
**GitHub:** [https://github.com/ndaosif/fasta-stats](https://github.com/ndaosif/fasta-stats)

---

## Features

- Compute key sequence statistics:
  - Number of sequences
  - Total length
  - Average length
  - Longest sequence
  - GC content (%)
  - N50 value
- Optional sequence length histogram (`length_hist.png`)
- Supports:
  - FASTA (`.fasta`, `.fa`) and gzipped FASTA (`.fasta.gz`, `.fa.gz`)
  - FASTQ (`.fastq`, `.fq`) and gzipped FASTQ (`.fastq.gz`, `.fq.gz`)
- Command-line interface (CLI)
- Lightweight, fast, and written in pure Python
- Ready for integration in bioinformatics pipelines

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ndaosif/fasta-stats.git
cd fasta-stats
```
2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Optional: install as editable Python package:

```bash
pip install -e .
```
##  Usage

Basic usage:

```bash
fasta-stats example.fasta
fasta-stats genome.fasta.gz
fasta-stats reads.fastq.gz

fasta-stats example.fasta --plot # With sequence length histogram
fasta-stats example.fasta --version # Show version
# Output: fasta-stats 0.1 — ndaosif/bioinfosif
```
## Output

Example output for a FASTA file:
```bash
FASTA/FASTQ Statistics
----------------------
Number of sequences : 5
Total length        : 15432
Average length      : 3086.40
Longest sequence    : 4200
GC content          : 41.23%
N50                 : 3200
Length histogram saved as length_hist.png
```
##  Testing

Tests are written with ```bash pytest```. To run tests:
```bash
pytest -v tests/test_stats.py
```

##  Contributing

Contributions are welcome!

* Fork the repository
 
* Create a branch for your feature or bugfix

* Run tests before committing

* Open a pull request with a description of your changes

##  License

MIT License © 2026 ndaosif / bioinfosif

##  Contact

GitHub: https://github.com/ndaosif/fasta-stats

Author: Mamadou Ndao — Bioinformatician

Email: ndaom403@gmail.com
