#Script Name: team_leucine_bioinformatics.py
#Author: Lavinia Dorothea F. Joseph
#Purpose:
   # This script stores information about team members (Team Leucine) and performs basic bioinformatics analysis on their favorite gene sequences.
    #Analyses include:
       # - Validating DNA sequences
       # - Computing GC content
        #- Translating DNA to protein


import pandas as pd

# ---------------------------------------------------------
#  Helper Functions
# ---------------------------------------------------------

def validate_dna(seq):
   # """Check if the sequence contains only valid DNA bases (A, T, C, G)."""
    valid_bases = set("ATCG")
    seq = seq.upper()
    if all(base in valid_bases for base in seq):
        return True
    else:
        return False

def gc_content(seq):
    #"""Calculate GC content percentage of a DNA sequence."""
    seq = seq.upper()
    gc = seq.count("G") + seq.count("C")
    return round((gc / len(seq)) * 100, 2) if len(seq) > 0 else 0

def translate_dna(seq):
   # """Translate a DNA sequence into its corresponding protein sequence."""
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'
    }
    seq = seq.upper()
    protein = ""
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        protein += codon_table.get(codon, 'X')  # 'X' for unknown codons
    return protein

# ---------------------------------------------------------
# 🧬 Team Data
# ---------------------------------------------------------
#Import the pandas library for data manipulation
import pandas as pd

#Define a list of dictionaries to store team information
team_leucine = [
    {
        "Name": "Chioma Nnadi",
        "Slack_username": "Chioma",
       "Country": "Nigeria",
        "Hobby": "Writing",
        "Affiliation": "None",
        "Fav_gene_sequence": "ACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCA"
    },
    {
       "Name": "Kashish Arora",
       "Slack_username": "Kashish",
       "Country": "India",
       "Hobby": "Reading",
        "Affiliation": "University of Glasgow",
        "Fav_gene_sequence": "GAACATGTCCCAACATGTTG"
    },
    {
       "Name": "Keola Merl Joanes",
        "Slack_username": "Keola",
        "Country": "India",
       "Hobby": "Reading",
        "Affiliation": "PCCAS",
       "Fav_gene_sequence": "GGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA"
    },
    {
         "Name": "Lavinia Dorothea F Joseph",
        "Slack_username": "Lavinia",
        "Country": "Antigua & Barbuda",
       "Hobby": "Sudoku",
        "Affiliation": "University Mohammed V, FMPH",
       "Fav_gene_sequence": "GTTCCAGGTAGTGCCTGAAACTACTTTTCTGAAGAAGTATAATTAAAAGTAATCTTGTTTTGAGAA"
    },
     {
       "Name": "Atairoro Joshua",
        "Slack_username": "Atairoro Joshua",
        "Country": "Nigeria",
       "Hobby": "Music",
        "Affiliation": "None",
       "Fav_gene_sequence": "ATGGAAGTTGTCATTTTATAAAGTCAGTAGTTTCTTTGGCAGCAATGCCAGGAAAGGCTCTGAGGAA"
    },
     {
       "Name": "Bezaleel Akinbami",
        "Slack_username": "B3z",
        "Country": "Nigeria",
       "Hobby": "Gaming",
        "Affiliation": "None",
       "Fav_gene_sequence": "" #empty to denote that the individual does not have a favourite gene sequence
    },
     {
       "Name": "Sharon Addy",
        "Slack_username": "Sharon Addy",
        "Country": "Ghana",
       "Hobby": "Repairing damaged electronics",
        "Affiliation": "None",
       "Fav_gene_sequence": "UGGAAUGUAAAGAAGUAUGUAU"
    },
    {
       "Name": "Jegede Joseph.O",
        "Slack_username": "Joseph",
        "Country": "Nigeria",
       "Hobby": "Gaming",
        "Affiliation": "Obafemi Awolowo University",
       "Fav_gene_sequence": "" #empty to denote that the individual does not have a favourite gene sequence
    }
]

#Convert the list of dictionaries into a pandas DataFrame
df_team_leucine = pd.DataFrame(team_leucine)

# ---------------------------------------------------------
# 🔬 Add Scientific Analysis Columns
# ---------------------------------------------------------

# Validate DNA
df_team_leucine['is_valid_DNA'] = df_team_leucine['Fav_gene_sequence'].apply(validate_dna)

# Calculate GC Content
df_team_leucine['GC_content_%'] = df_team_leucine['Fav_gene_sequence'].apply(gc_content)

# Translate DNA → Protein
df_team_leucine['protein_sequence'] = df_team_leucine['Fav_gene_sequence'].apply(
    lambda seq: translate_dna(seq) if validate_dna(seq) else "Invalid DNA"
)

#Print the Table heading
print("Team_Leucine Information\n") #\n is used to create a space between the table heading and the table itself

#Import IPython.display to present team information in a well-structured table
from IPython.display import display
display(df_team_leucine) #code to print and display the table with the team members' information
