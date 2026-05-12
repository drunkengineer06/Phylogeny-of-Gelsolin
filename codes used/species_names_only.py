from pathlib import Path
import re

# Input treefile
input_tree = "renamed_tree.treefile"

# Output cleaned treefile
output_tree = "cleaned_tree.treefile"

# Read tree
tree_text = Path(input_tree).read_text()

# Regex:
# tr|A0A1S4HE98|A0A1S4HE98_ANOGA
# becomes:
# ANOGA

pattern = r"(sp|tr)\|[^|]+\|[^_]+_([A-Z0-9]+)"

# Replace with only species code
cleaned_text = re.sub(pattern, r"\2", tree_text)

# Write cleaned tree
Path(output_tree).write_text(cleaned_text)

print(f"Cleaned tree written to: {output_tree}")
from Bio import Phylo
Phylo.draw(Phylo.read("cleaned_tree", "newick"))