import csv
import glob

# Specify the path pattern for the CSV files to be merged
csv_files = glob.glob("*.csv")

# Specify the output file name
output_file = "merged_file.csv"

# Open the output file in write mode
with open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)

    # Flag to track if the header has been written
    header_written = False

    # Iterate over each CSV file
    for file in csv_files:
        with open(file, "r", encoding="utf-8") as infile:
            reader = csv.reader(infile)

            # Skip the header row if it has already been written
            if header_written:
                next(reader)

            # Iterate over each row in the CSV file and write it to the output file
            for row in reader:
                writer.writerow(row)

        # Set the flag to True after writing the header once
        if not header_written:
            header_written = True

print(f"CSV files merged successfully into '{output_file}'.")
