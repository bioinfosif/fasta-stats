import argparse
from fasta_stats.compute_stats_file import compute_stats_file
from fasta_stats.parser_stats import compute_n50, plot_length_distribution

def main():
    parser = argparse.ArgumentParser(description="FASTA/FASTQ statistics tool")
    parser.add_argument("file", help="Path to FASTA/FASTQ file (can be .gz)")
    parser.add_argument("--plot", action="store_true", help="Save sequence length histogram")
    parser.add_argument("--version", action="version", version="fasta-stats 0.1 — ndaosif/bioinfosif")
    args = parser.parse_args()

    stats = compute_stats_file(args.file)

    print("\nFASTA/FASTQ Statistics")
    print("----------------------")
    print(f"Number of sequences : {stats['count_sequences']}")
    print(f"Total length        : {stats['total_length']}")
    print(f"Average length      : {stats['average_length']:.2f}")
    print(f"Longest sequence    : {stats['longest_sequence']}")
    print(f"GC content          : {stats['gc_content']:.2f}%")
    print(f"N50                 : {compute_n50(stats['lengths'])}")

    if args.plot:
        plot_length_distribution(stats['lengths'])
        print("Length histogram saved as length_hist.png")

if __name__ == "__main__":
    main()