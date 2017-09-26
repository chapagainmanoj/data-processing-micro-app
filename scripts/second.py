#!/usr/bin/env python
import xlsxwriter
import csv
import re
import xlrd

from sys import argv

print(argv[0])
print(argv[1])
input_file = '/tmp/'+argv[1]
filename = '/tmp/output.xlsx'
template_file = './output/template2.xlsx'

table_names = ['Names','Count of Mentions','Avg. of Betweenness Centrality','Avg. of Inter-Cluster Connectivity','Sum of Social Engagement','Sum of Published Count']
# Populate contents of 'Raw data' tab (copy/paste from input file)
workbook = xlsxwriter.Workbook(filename,{'constant_memory':True})
worksheet = workbook.add_worksheet("Raw data")
higest_col = None
people_name = set()
with open(input_file,'rt', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for r, row in enumerate(reader):
        for c, col in enumerate(row):
            if col.isdigit():
                col = int(col)
            elif re.match('^-?[0-9]+\.[0-9]+$', col):
                col = float(col)
            worksheet.write(r,c,col)
            higest_col = c
            if(xlsxwriter.utility.xl_col_to_name(c)=='S'):
                result = re.sub(r'\([^)]*\)', '',col)
                people_name |= set([people.strip() for people in result.split(';')])

people_name.discard('People (Any Mention)')

def get_formula(header, row, type=None):
    if  type=='abs':
        if (header == 'Count of Mentions'):
            return '=COUNTIF($\'Raw data\'.S:S, "*" & A%d & "*")'%(row)
        elif (header == 'Avg. of Betweenness Centrality'):
            return '=AVERAGEIF($\'Raw data\'.S:S,"*" & A%d & "*",$\'Raw data\'.AU:AU)' %(row)
        elif (header == 'Avg. of Inter-Cluster Connectivity'):
            return '=AVERAGEIF($\'Raw data\'.S:S,"*" & A%d & "*",$\'Raw data\'.AX:AX)'%(row)
        elif (header == 'Sum of Social Engagement'):
            return '=SUMIF($\'Raw data\'.S:S,"*" & A%d & "*",$\'Raw data\'.I:I)' %(row)
        elif (header == 'Sum of Published Count'):
            return '=SUMIF($\'Raw data\'.S:S,"*" & A%d & "*",$\'Raw data\'.E:E)' %(row)
        else:
            return None
    elif type =='per':
        if (header == 'Count of Mentions'):
            return 'PERCENTRANK(B:B,B%d)'%(row)
        elif (header == 'Avg. of Betweenness Centrality'):
            return 'PERCENTRANK(C:C,C%d)' %(row)
        elif (header == 'Avg. of Inter-Cluster Connectivity'):
            return 'PERCENTRANK(D:D,D%d)'%(row)
        elif (header == 'Sum of Social Engagement'):
            return 'PERCENTRANK(E:E,E%d)' %(row)
        elif (header == 'Sum of Published Count'):
            return 'PERCENTRANK(F:F,F%d)' %(row)
        else:
            return None
    else:
        if header == 'Total Score':
            return '=(G%d*$Weights.$B$2) + (H%d*$Weights.$B$3)+(I%d*$Weights.$B$4)+(J%d*$Weights.$B$5)+ (K%d*$Weights.$B$6)' %(row,row,row,row,row)
        elif header == 'Overall Rank':
            return '=RANK(L%d,L:L)' %(row)


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
        for r,val in enumerate(people_name):
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
