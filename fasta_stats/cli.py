import argparse
from fasta_stats.parser_fasta import parser_fasta
from fasta_stats.parser_stats import compute_stats

def main():
    parser = argparse.ArgumentParser(description="Compute statistics from a FASTA file.")
    parser.add_argument("Fasta_file", help="Path to the FASTA file")
    args = parser.parse_args()

    record = parser_fasta(args.Fasta_file)
    n, total, avg, gc, longest = compute_stats(record)

    print(f"Number of sequences: {n}")
    print(f"Total length of sequences: {total}")
    print(f"Average length of sequences: {avg:.2f}")
    print(f"GC content: {gc:.2f}%")
    print(f"Longest sequence length: {longest}")

