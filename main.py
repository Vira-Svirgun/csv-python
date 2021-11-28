import csv

with open("acme_worksheet.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")

    for row in file_reader:
        print(f'{row}')

with open('acme_worksheet_finally.csv', mode="w", encoding='utf-8') as file:
    file_writer = csv.writer(file, delimiter=",", lineterminator="\r")



