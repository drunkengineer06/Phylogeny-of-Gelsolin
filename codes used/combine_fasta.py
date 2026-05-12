from pathlib import Path

# Folder containing individual FASTA files
input_folder = "D:/synthetic bio lab iisc/raw_seq"

# Output combined FASTA file
output_file = "D:/synthetic bio lab iisc/combined_gelsolin.fasta"

# FASTA extensions to include
extensions = [".fasta", ".fa", ".faa", ".txt"]

# Collect all FASTA files
fasta_files = []

for ext in extensions:
    fasta_files.extend(Path(input_folder).glob(f"*{ext}"))

# Combine contents
with open(output_file, "w") as outfile:
    for fasta in fasta_files:
        with open(fasta, "r") as infile:
            content = infile.read().strip()

            # Ensure file is not empty
            if content:
                outfile.write(content + "\n")

print(f"Combined {len(fasta_files)} files into {output_file}")