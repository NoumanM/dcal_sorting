import csv

file_name = 'New-with-spanish-translation--DCAL-output-2023-07-01.csv'
with open(file_name, 'r') as inFile:
    reader = csv.reader(inFile)
    item = {}
    count = 0
    for row in reader:
        if count == 0:
            count += 1
            continue
        item.update({row[7]: {row[6]: 'None'}})

    for group_name in sorted(item.keys()):
        with open('g_name_and_spec.csv', 'a+', newline='') as outfile:
            writer = csv.writer(outfile)
            spec = [v for v in item[group_name].keys()]
            writer.writerow([group_name, spec[0]])
