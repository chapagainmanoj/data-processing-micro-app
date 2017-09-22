import xlsxwriter
import csv

# TODO: input file handle
filename = 'test.xlsx'

workbook = xlsxwriter.Workbook(filename,{'constant_memory':True})
worksheet = workbook.add_worksheet("Raw data")
with open('./input/quid_KOL_webofscience_input.csv','rt', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for r, row in enumerate(reader):
        for c, col in enumerate(row):
            worksheet.write(r,c,col)
workbook.close()
