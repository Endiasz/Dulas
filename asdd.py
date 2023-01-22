import csv


# Open the CSV file
with open('sklep.csv', 'r') as csv_file:
  # Create a CSV reader object
  reader = csv.reader(csv_file)
  number = 10
  row_number = 10
  # Loop through the rows
  for row in reader:
    # If the row number is the one you want
    if reader.line_num == row_number:
      # Loop through the columns in the row
      for column in row:
        # If the column value is the number you are looking for
        if column == number:
            data = row.split(",")
            # print(f'Number found at row {row_number}, column {row.index(column)+1}')
            break
      break