from setuptools import setup, find_packages

setup(
    name="fasta-stats",  # <-- le nom du package / commande CLI
    version="0.1",
    author="ndaosif / Mamadou Ndao",
    description="Bioinformatics tool for FASTA/FASTQ statistics",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.25.0",
        "matplotlib>=3.8.0",
    ],
    entry_points={
        "console_scripts": [
            "fasta-stats = fasta_stats.cli:main"  # <-- CLI nommée fasta-stats
        ]
    },
    python_requires=">=3.8",
)