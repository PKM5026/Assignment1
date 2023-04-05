import json

# Create dictionary of Indian states and their capitals
indian_7_states = {
    "Uttar Pradesh": "Lucknow",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bengaluru",
    "Gujarat": "Gandhinagar",
    "Andhra Pradesh": "Hyderabad",
    "West Bengal": "Kolkata" }

# Write the dictionary to a JSON file
with open("indian_states.json", "w") as f:
    json.dump(indian_7_states, f)

# Read the contents of the JSON file and print it
with open("indian_states.json", "r") as f:
    data = json.load(f)
    print(data)