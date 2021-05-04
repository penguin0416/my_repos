import csv

test_list = ['a', 'b', 'c']

with open('listfile.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(test_list)

print(test_list)

test_list.append(input())

with open('listfile.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(test_list)

print(test_list)

with open('listfile.csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f)
    for i, line in enumerate(rdr):
        if i == 0:
            test_list = line

print(test_list)