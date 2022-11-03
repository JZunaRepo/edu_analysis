import csv

from numpy import number
list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)
#Total rows in list_date
num_rows = 0
for num in list_data:
  num_rows += 1
print(num_rows)

#Filtering rows with NEW_YORK as STATE
state_data = [row for row in list_data if row["STATE"] == "NEW_YORK"]

#Filtering rows with values in column "AVG_MATH_4_SCORE"
avg_score = [row for row in state_data if row["AVG_MATH_4_SCORE"] != ""]

#Counting how many rows have AVG_MATH_4_SCORE values 
rows_in_avg = 0
for num in avg_score:
  rows_in_avg += 1
print(rows_in_avg)