from fasta_stats.parser_fasta import parser_fasta
from fasta_stats.parser_fastq import parser_fastq
from fasta_stats.parser_stats import compute_stats

def compute_stats_file(filepath):
    if filepath.endswith((".fasta", ".fa", ".fasta.gz", ".fa.gz")):
        records = parser_fasta(filepath)
    elif filepath.endswith((".fastq", ".fq", ".fastq.gz", ".fq.gz")):
        records = parser_fastq(filepath)
    else:
        raise ValueError("Unsupported file format")
    return compute_stats(records)