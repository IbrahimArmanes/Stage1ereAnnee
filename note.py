import xlsxwriter
table1=['7 (2) 2,5 /5 10','','7 (2) 2,5 /5 10']
notes=table1[0].split(' ')

outWorkbook = xlsxwriter.Workbook("TestNotes.xlsx")
worksheet = outWorkbook.add_worksheet()

#format
coef = outWorkbook.add_format()
coef.set_font_script(1)
noteSur = outWorkbook.add_format()
noteSur.set_font_script(2)
##
ligne = 1
col = 1
for j in range(len(notes)):
     if notes[j].startswith('('):
          worksheet.write_rich_string(ligne, col,notes[j-1],coef,notes[j])
          col += 1
     elif notes[j].startswith('/'):
          worksheet.write_rich_string(ligne, col,notes[j-1],noteSur,notes[j])
          col += 1



outWorkbook.close()