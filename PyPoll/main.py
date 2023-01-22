import csv
import os
import pandas as pd

data_file = "/Users/aldosilva/python-challenge/PyPoll/Resources/election_data.csv"
data_file_df = pd.read_csv(data_file)
data_file_df.head()

votes = data_file_df["Ballot ID"].count()
print(votes)

candidates = data_file_df["Candidate"].unique()
print(candidates)

vote_count = data_file_df["Candidate"].value_counts()
print(vote_count)

vote_percentages = data_file_df["Candidate"].value_counts(normalize=True)*100
print(vote_percentages)

votes_df = pd.DataFrame({
    "Candidates" : candidates,
    "Votes" : vote_count
})
votes_df

winner = votes_df["Votes"].max()
print(winner)
winner_candidate = "Diana DeGette"

print("Total votes: " + str(votes))
print("--------------------------")
print(vote_percentages)
print("--------------------------")
print(winner_candidate)
print("--------------------------")

summary_df = pd.DataFrame({
    "Total votes" : [votes],
    "Percentages" : [vote_percentages],
    "Winner" : [winner_candidate],
})
summary_df

summary_df.to_csv('/Users/aldosilva/python-challenge/PyPoll/analysis/results.csv', index=None)
