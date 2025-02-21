import csv
from spanish_utils import Spanish_Utils
from datetime import date

filename = f'DCAL-output-{date.today()}.csv'
with open(filename, 'r', encoding='utf-16') as inFile:
    reader = csv.reader(inFile)
    count = 1
    with open(f"spanish-{filename}", 'a+', encoding='utf-16', newline='') as outfile:
        writer = csv.writer(outfile)
        for r in reader:
            if count == 1:
                writer.writerow(r)
                count += 1
            else:
                new_data_list = []
                for index in range(0, len(r)):
                    value = r[index]
                    if index == 6:
                        try:
                            value = Spanish_Utils.add_spanish[value.strip()]
                        except:
                            value = r[index]
                    new_data_list.append(value)
                writer.writerow(new_data_list)



