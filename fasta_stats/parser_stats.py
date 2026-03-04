def compute_stats(record):
    total_sequence = 0
    num_sequence = 0
    longest_sequence = 0
    gc_count = 0

    for _ , sequence in record:
        total_sequence += len(sequence)
        num_sequence += 1
        longest_sequence = max(longest_sequence, len(sequence))
        gc_count += sequence.count("G") + sequence.count("C")

    average_length = total_sequence / num_sequence if num_sequence > 0 else 0
    gc = (gc_count / total_sequence * 100) if total_sequence > 0 else 0
    return num_sequence, total_sequence, average_length, gc,  longest_sequence