#!/usr/bin/env python
import xlsxwriter
import xlrd
import re
import csv
from sys import argv, maxsize

input_file = argv[1]
output_file = argv[2]
template_file = argv[3]

decrement = True

# for OverflowError
while decrement:
    decrement = False
    try:
        csv.field_size_limit(maxsize)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

workbook = xlsxwriter.Workbook(output_file, {'constant_memory': True})
worksheet = workbook.add_worksheet("Raw data")
higest_col = None
auther_name = set()
auther_col = 'AR'

with open(input_file,'rt', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for r, row in enumerate(reader):
        if r == 1:
            for c,col in enumerate(row):
                if col == 'AF':
                    auther_col = xlsxwriter.utility.xl_col_to_name(c)
                worksheet.write(r,c,col)
                higest_col = c
        else:
            for c, col in enumerate(row):
                if col.isdigit():
                    col = int(col)
                elif re.match('^-?[0-9]+\.[0-9]+$', col):
                    col = float(col)
                worksheet.write(r,c,col)
                higest_col = c
                if(xlsxwriter.utility.xl_col_to_name(c) == auther_col):
                    auther_name |= set([author.strip() for author in col.split(';')])

        cell = xlsxwriter.utility.xl_rowcol_to_cell(r,higest_col+1)

        if (r==0):
            worksheet.write(cell,'# of co-authors')
        else:
            worksheet.write_formula(cell,'=LEN(AR%d)-LEN(SUBSTITUTE(AR%d,";",""))'%(r+1,r+1))




auther_name.discard('AF')
auther_name.discard('')

def get_formula(header, row, type=None):
    if type=='abs':
        if (header == 'Count of Auther\'s Name'):
            return '=COUNTIF(\'Raw data\'!AR:AR,"*"&Output!A%d&"*")'% (row)
        elif (header == 'Avg. of Betweenness Centrality'):
            return '=IFERROR(AVERAGEIFS(\'Raw data\'!K:K,\'Raw data\'!AR:AR, "*" & Output!A%d &"*"),0)' %(row)
        elif (header == 'Avg. of Inter-Cluster Connectivity'):
            return '=IFERROR(AVERAGEIFS(\'Raw data\'!W:W,\'Raw data\'!AR:AR, "*" & Output!A%d &"*"),0)'% (row)
        elif (header == 'Sum of Cited by'):
            return '=SUMIFS(\'Raw data\'!BX:BX,\'Raw data\'!AR:AR,"*" & Output!A%d & "*")'% (row)
        elif (header == 'Sum of Connections'):
            return '=SUMIFS(\'Raw data\'!CI:CI,\'Raw data\'!AR:AR,"*" & Output!A%d & "*")'% (row)
        else:
            return None
    elif type=='per':
        if (header == 'Count of Auther\'s Name'):
            return 'PERCENTRANK(B:B,B%d)'% (row)
        elif (header == 'Avg. of Betweenness Centrality'):
            return 'PERCENTRANK(C:C,C%d)' %(row)
        elif (header == 'Avg. of Inter-Cluster Connectivity'):
            return 'PERCENTRANK(D:D,D%d)'% (row)
        elif (header == 'Sum of Cited by'):
            return 'PERCENTRANK(E:E,E%d)'% (row)
        elif (header == 'Sum of Connections'):
            return 'PERCENTRANK(F:F,F%d)'% (row)
        else:
            return None
    else:
        if header == 'Total Score':
            return '=(G%d*Weights!$B$2) + (H%d*Weights!$B$3)+(I%d*Weights!$B$4)+(J%d*Weights!$B$5)+ (K%d*Weights!$B$6)' %(row,row,row,row,row)
        elif header == 'Overall Rank':
            return '=RANK(L%d,L:L)' %(row)



table_names = ['Names','Count of Auther\'s Name','Avg. of Betweenness Centrality', \
'Avg. of Inter-Cluster Connectivity','Sum of Cited by','Sum of Connections'\
]

wb_read = xlrd.open_workbook(template_file)
sheets = wb_read.sheets()
for sheet in sheets:
    if sheet.name == "Weights":
        ws = workbook.add_worksheet("Weights")
        for row in range(sheet.nrows):
            for col in range(sheet.ncols):
                ws.write(row,col,sheet.cell(row,col).value)
    elif sheet.name =="Output":
        worksheet2 = workbook.add_worksheet("Output")
        for row in range(2):
            for col in range(sheet.ncols):
                worksheet2.write(row,col,sheet.cell(row,col).value)

                #len_table_names = 13
        for r,val in enumerate(auther_name):
            max_col = 0
            for c,header in enumerate(table_names):
                if c == 0:
                    worksheet2.write_string(r+2,c,val)
                else:
                    formula = get_formula(header,r+3,'abs')
                    cell = xlsxwriter.utility.xl_rowcol_to_cell(r+2,c)
                    worksheet2.write_formula(cell, formula)
                    max_col = c
            for c,header in enumerate(table_names):
                if c == 0:
                    pass
                else:
                    max_col += 1
                    formula = get_formula(header,r+3,'per')
                    cell = xlsxwriter.utility.xl_rowcol_to_cell(r+2,max_col)
                    worksheet2.write_formula(cell, formula)
            worksheet2.write_formula(r+2,max_col+1,get_formula('Total Score',r+3))
            worksheet2.write_formula(r+2,max_col+2,get_formula('Overall Rank',r+3))
workbook.close()
