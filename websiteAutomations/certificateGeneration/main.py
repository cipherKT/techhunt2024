import csv
import json
import pprint

# Load the username_index_dict from previous JSON parsing
with open('leaderboard.json', 'r') as file:
    leaderboard_data = json.load(file)
    index = 1
    username_index_dict = {}

    for (i, entry) in enumerate(leaderboard_data):
        if (entry['username'] == "32_Bit_Savvy"):
            continue

        username_index_dict[entry['username']] = index
        index += 1

# Output array to store team standings
team_standings = []

# Read the CSV file
with open('registrations.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        team_name = row['Team Name']


        # Skip teams not in username_index_dict
        if team_name not in username_index_dict:
            continue

        team_id = row['Team ID']
        candidate_name = row["Candidate's Name"]
        candidate_email = row["Candidate's Email"]
        standing = username_index_dict[team_name]

        team_standings.append({
            'team_id': team_id,
            'team_name': team_name,
            'name': candidate_name,
            'email': candidate_email,
            'standing': standing
        })

# Print or further process the team_standings array
pprint.pprint(team_standings)

team_standings.sort(key=lambda x: x['standing'])

with open('standings.json', 'w') as file:
   json.dump(team_standings, file, indent=2)