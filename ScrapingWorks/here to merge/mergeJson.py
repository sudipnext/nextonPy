import json
import glob

# Create an empty list to hold the merged data
merged_data = []

# Get a list of all JSON files in the directory
file_list = glob.glob("*.json")

# Iterate over each file
for file_path in file_list:
    # Read the JSON file
    with open(file_path, 'r') as file:
        try:
            # Parse the JSON data
            data = json.load(file)

            # Append the data to the merged_data list
            merged_data.append(data)
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON file: {file_path}")
            continue

# Convert the merged_data list to a JSON string
merged_json = json.dumps(merged_data)

# Specify the output file path
output_file = "merged.json"

# Write the merged JSON string to the output file
with open(output_file, 'w') as file:
    file.write(merged_json)

print("Merged JSON file created successfully.")
