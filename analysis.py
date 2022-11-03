import csv

from numpy import number
list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)
#Total rows in list_date
print(len(list_data))

#Filtering rows with NEW_YORK as STATE
state_data = [row for row in list_data if row["STATE"] == "NEW_YORK"]

#Filtering rows with values in column "AVG_MATH_4_SCORE"
avg_score = [row for row in state_data if row["AVG_MATH_4_SCORE"] != ""]

#Counting how many rows have AVG_MATH_4_SCORE values 
print(len(avg_score))

def filter(state, column):
  state_data = [row for row in list_data if row["STATE"] == state]
  filtered_column = [row for row in state_data if row[column] != ""]
  return filtered_column

#Example test
print(len(filter("NEW_YORK", "AVG_MATH_4_SCORE")))