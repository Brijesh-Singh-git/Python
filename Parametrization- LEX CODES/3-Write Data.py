import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("WriteData")

# sheet.write(0,0,"Hello")
# workbook.save("WriteData_Sample.xls")

# for r in range(0 , 4):
#     for c in range(0,3):

sheet.write(0,1,"EMP_Name")
sheet.write(0,2,"EMP_Id")
sheet.write(0,3,"Designation")

sheet.write(1, 1, "Priya Gupta")
sheet.write(1, 2, "778812")
sheet.write(1, 3, "Tester")

sheet.write(2, 1, "Rohan Das")
sheet.write(2, 2, "225666")
sheet.write(2, 3, "Develoepr")

sheet.write(3, 1, "Akash Kumar")
sheet.write(3, 2, "11447899")
sheet.write(3, 3, "Dockers")

workbook.save("WriteData_Sample.xls")



