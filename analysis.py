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
years = []
for row in avg_score:
  years.append(row["YEAR"])
print(years)

def percent_change(data,year1,year2,column):
  old = 0
  new = 0
  for row in data: 
    if row["YEAR"] == year1:
      old = float(row[column])
    if row["YEAR"] == year2:
      new = float(row[column])
  perc_change = (old - new)/old * 100
  return perc_change
  
for i in range(len(years)):
  if i + 1 >=len(years):
    break
  year1 = years[i]
  year2 = years[i+1]
  change = percent_change(avg_score,year1,year2,"AVG_MATH_8_SCORE")
  print(f"Percent cahnge from {year1}-{year2} is {change}")