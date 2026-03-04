def parser_fasta(filepath: str):
    
    header = ""
    sequences = ""
    try:
        with open(filepath) as f:
            for line in f:
                line = line.rstrip()
                if line.startswith(">"):
                    if header and sequences:
                        yield (header, sequences)
                    header = line
                    sequences = ""
                else:
                    sequences += line
            if header and sequences:
                yield (header, sequences)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filepath} not found")   
    
    return header, sequences