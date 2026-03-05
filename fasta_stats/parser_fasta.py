import gzip

def parser_fasta(filepath: str):
    """Generator: yield (header, sequence) from FASTA or FASTA.gz"""
    open_func = gzip.open if filepath.endswith(".gz") else open
    header, sequence = "", ""
    
    with open_func(filepath, "rt") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith(">"):
                if header and sequence:
                    yield (header, sequence)
                header = line[1:]  # remove '>'
                sequence = ""
            else:
                sequence += line
        if header and sequence:
            yield (header, sequence)