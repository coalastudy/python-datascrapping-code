import openpyxl

wb2 = openpyxl.load_workbook('test.xlsx')
ws = wb2["이름 변경"]

ws.append(range(10))

wb2.save('test2.xlsx')
