import csv

# Function to read the CSV file and store the data in a list
def read_csv(file_name):
    data = []
    with open(file_name, mode='r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row
        data.append(headers)
        for row in reader:
            data.append(row)
    return data

# Function to add a new column 'Status' with a default value of 'Pending' to all rows if it doesn't exist
def add_status_column(data):
    headers = data[0]
    if 'Status' not in headers:
        headers.append('Status')
        for row in data[1:]:
            row.append('Pending')
    else:
        status_index = headers.index('Status')  # Get the index of existing Status column
        for row in data[1:]:
            if len(row) <= status_index:  # If the row is shorter than the header length
                row.append('Pending')
            elif row[status_index] == '':  # If the Status field is empty
                row[status_index] = 'Pending'
    return data

# Function to save the modified data to a new CSV file
def save_csv(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Main function to process the security incidents CSV
def main():
    input_file = 'security_incidents.csv'
    output_file = 'security_incidents_modified.csv'
    
    # Read the CSV file
    data = read_csv(input_file)
    
    # Add 'Status' column if not present
    modified_data = add_status_column(data)
    
    # Save the modified data to a new CSV file
    save_csv(output_file, modified_data)
    print("Modified data has been saved to", output_file)

# Run the main function
if __name__ == "__main__":
    main()
