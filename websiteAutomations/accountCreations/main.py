import csv
from pprint import pprint

# Basic reading
# with open('file.csv', 'r') as file:
#     csv_reader = csv.reader(file)
#     # Skip header row if needed
#     next(csv_reader)
#     for row in csv_reader:
#         print(row)  # row is a list of values

# Reading as dictionaries (if you have headers)
with open('./input.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    final = []
    for row in csv_reader:
        finalDict = {}
        if (row["Candidate Type"] == "Leader" and row["Reg. Status"] == "Complete"):
            finalDict["Team ID"] = row["Team ID"]
            finalDict["Team Name"] = row["Team Name"]
            finalDict["Candidate Type"] = row["Candidate Type"]
            finalDict["Candidate's Name"] = row["Candidate's Name"]
            finalDict["Candidate's Email"] = row["Candidate's Email"]
            finalDict["Candidate's Mobile"] = row["Candidate's Mobile"]
            final.append(finalDict)

with open('output.csv', 'w', newline='') as file:
    # Get fieldnames from the first dictionary
    pprint(final)
    fieldnames = final[0].keys()

    # Create DictWriter object
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header row
    writer.writeheader()

    # Write data rows
    writer.writerows(final)

    file.close()
