import gzip

def parser_fastq(filepath: str):
    """Generator: yield (header, sequence) from FASTQ or FASTQ.gz"""
    open_func = gzip.open if filepath.endswith(".gz") else open
    with open_func(filepath, "rt") as f:
        while True:
            header = f.readline().rstrip()
            if not header:
                break
            seq = f.readline().rstrip()
            f.readline()  # +
            f.readline()  # quality
            yield (header[1:] if header.startswith("@") else header, seq)