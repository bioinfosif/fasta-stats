from setuptools import setup, find_packages

setup(
    name="fasta-stats",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fasta-stats=fasta_stats.cli:main"
        ]
    }
)