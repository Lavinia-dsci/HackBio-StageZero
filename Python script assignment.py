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

#Print the Table heading
print("Team_Leucine Information\n") #\n is used to create a space between the table heading and the table itself

#Import IPython.display to present team information in a well-structured table
from IPython.display import display
display(df_team_leucine) #code to print and display the table with the team members' information
