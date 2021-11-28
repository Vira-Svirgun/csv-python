import csv

name_of_category = []
name = []
date = []
work_hours = []

with open("acme_worksheet.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f'{row}')
            for i in row:
                name_of_category.append(i)
        else:
            name.append(row[0])
            date.append(row[1])
            work_hours.append(row[2])
            print(f'{row[0]} - {row[1]} - {row[2]}')
        count += 1
    print(f'Всего в файле {count} строк.')

print('name_of_category:', name_of_category)
print('name:', name)
print('date:', date)
print('work_hours:', work_hours)


with open('acme_worksheet_finally.csv', mode="w", encoding='utf-8') as file:
    file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
    file_writer.writerow(name_of_category)
    file_writer.writerow(name)
    file_writer.writerow(date)
    file_writer.writerow(work_hours)



