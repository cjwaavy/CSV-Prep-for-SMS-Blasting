import csv

def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile, open(output_file, 'w', newline='') as output_csv:
        reader = csv.reader(csvfile)
        writer = csv.writer(output_csv)
        
        for row in reader:
            new_row = []
            for i in range(len(row)):
                if i == 0 or "Mobile" in row[i]:
                    new_row.append(row[i])
            writer.writerow(new_row)

# Replace 'input.csv' and 'output.csv' with your file names
process_csv('input.csv', 'output.csv')