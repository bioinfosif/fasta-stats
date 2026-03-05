import pytest
from fasta_stats.parser_stats import compute_stats

def test_count_sequences(tmp_path):
    fasta_file = tmp_path / "test.fasta"
    fasta_content = """>seq1
ATGC
>seq2
ATGCGG
"""
    fasta_file.write_text(fasta_content)

    stats = compute_stats(str(fasta_file))

    # Vérification du nombre de séquences
    assert stats["count_sequences"] == 2

    # Vérification de la longueur totale
    assert stats["total_length"] == 10

    # Vérification de la plus longue séquence
    assert stats["longest_sequence"] == 6

    # Vérification du GC content
    # seq1: ATGC → 2 GC, seq2: ATGCGG → 4 GC
    expected_gc = (2 + 4) / 10
    assert abs(stats["gc_content"] - expected_gc) < 1e-6