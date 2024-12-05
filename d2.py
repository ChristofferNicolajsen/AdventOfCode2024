import numpy as np
with open('readings.txt', 'r') as file:
    # Convert each line into a list of integers
    data = [list(map(int, line.split())) for line in file]
# Determine the maximum length of the rows
max_length = max(len(row) for row in data)
# Pad each row to the maximum length
padded_data = [row + [-999] * (max_length - len(row)) for row in data]
# Convert the padded data to a NumPy array
array = np.array(padded_data)
dimensions = array.shape
rows, columns = dimensions
assending_numbers = 0
number_of_invalid_rows = 0
c=0
# Iterer gennem hver række
for r in range(rows):
    if (array[r, 0] < array[r, 1]):
        print('Assending: '+ str(array[r, 0])+' ' + str(array[r, 1]))
        assending_numbers = True
    else:
        assending_numbers = False
    for c in range(columns-1):
        if array[r, c+1] == -999:  # Ignorer padding
            break
        print(str(r)+','+str(c)+' '+str(assending_numbers))
        if (assending_numbers and not (0 < (array[r, c+1] - array[r, c]) < 4)):  # Tjek gyldighed
            number_of_invalid_rows +=1
            print(f"Counting")
            print('INVALID ROW: '+str(r)+' -->> '+ str(array[r, c])+' '+str(array[r, c + 1])+' = '+str((array[r, c+1] - array[r, c]))+' Assending: '+str(assending_numbers))
            break
        if (not assending_numbers and not(0 > (array[r, c+1] - array[r, c]) > -4)):  # Tjek gyldighed
            number_of_invalid_rows +=1
            print(f"Counting")
            print('INVALID ROW: '+str(r)+' -->> '+ str(array[r, c])+' '+str(array[r, c + 1])+' = '+str((array[r, c+1] - array[r, c]))+' Assending: '+str(assending_numbers))
            break
print('number of valid rows: '+str(rows-number_of_invalid_rows))