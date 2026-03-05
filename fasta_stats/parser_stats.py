import matplotlib.pyplot as plt
import numpy as np

def compute_stats(records):
    total_length = 0
    num_sequences = 0
    longest_sequence = 0
    gc_count = 0
    lengths = []

    for _, sequence in records:
        seq_len = len(sequence)
        total_length += seq_len
        num_sequences += 1
        longest_sequence = max(longest_sequence, seq_len)
        gc_count += sequence.upper().count("G") + sequence.upper().count("C")
        lengths.append(seq_len)

    average_length = total_length / num_sequences if num_sequences else 0
    gc_content = (gc_count / total_length * 100) if total_length else 0

    return {
        "count_sequences": num_sequences,
        "total_length": total_length,
        "average_length": average_length,
        "gc_content": gc_content,
        "longest_sequence": longest_sequence,
        "lengths": lengths  # pour N50 et histogramme
    }

def compute_n50(lengths):
    if not lengths:
        return 0
    sorted_lengths = sorted(lengths, reverse=True)
    cumsum = np.cumsum(sorted_lengths)
    half = sum(sorted_lengths) / 2
    for l, cs in zip(sorted_lengths, cumsum):
        if cs >= half:
            return l

def plot_length_distribution(lengths, output="length_hist.png"):
    plt.hist(lengths, bins=50)
    plt.xlabel("Sequence length")
    plt.ylabel("Count")
    plt.title("Length distribution")
    plt.savefig(output)
    plt.close()