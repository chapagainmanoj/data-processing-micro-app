import xlsxwriter
import csv

# TODO: input file handle
input_file = './input/quid_KOL_webofscience_input.csv'
filename = './output/test.xlsx'
# Populate contents of 'Raw data' tab (copy/paste from input file)
workbook = xlsxwriter.Workbook(filename,{'constant_memory':True})
worksheet = workbook.add_worksheet("Raw data")
with open(input_file,'rt', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for r, row in enumerate(reader):
        for c, col in enumerate(row):
            worksheet.write(r,c,col)

# TODO: 
# Ensure formula in the last column of 'Raw data' tab extends all the way to the last row
# Split out all the authors separated by semi colons in column AR of 'Raw data' tab (name of the column is 'AF') into separate rows, and paste that de-duplicated list into column A of 'Output' tab
# Ensure all formulas in columns B through M of 'Output' tab extend all the way to the last row
# That's it - all the formulas that I've built in Excel should auto-populate the ranking stuff in the 'Output' tab

workbook.close()
