import xlrd
from xlutils.copy import copy
from selenium import webdriver
excel=("C:\\Users\\AYUSH\\Downloads\\STP\\marks.xls")
driver=webdriver.Chrome("C:\\Driver\\chromedriver")
#driver.set_page_load_timeout(50)
driver.get("C:\\Users\\AYUSH\\OneDrive\\Documents\\student.html")
book = xlrd.open_workbook(excel)
sheet = book.sheet_by_index(0)
stud_obj = driver.find_elements_by_xpath(".//*[@id='student_name']")
marks_obj = driver.find_elements_by_class_name("marks")

for i in range(1,6):
    stud_obj[0].send_keys(str(sheet.cell_value(i,0)))
    del stud_obj[0]
for j in range(1,6):
    for k in range(1,sheet.ncols):
        marks_obj[0].send_keys(str(sheet.cell(j,k).value))
        del marks_obj[0]
driver.find_element_by_id("calculate").click()
total_obj = driver.find_elements_by_class_name("total")
per_obj = driver.find_elements_by_class_name("percentage")
res_obj = driver.find_elements_by_class_name("result")

total=[]
percentage=[]
result=[]
for i in total_obj:
    total.append(str(i.get_attribute("value")))
for j in per_obj:
    percentage.append(str(j.get_attribute("value")))
for k in res_obj:
    result.append(str(k.get_attribute("value")))
rb= xlrd.open_workbook(excel)
r_sheet = book.sheet_by_index(0)
c=r_sheet.ncols
wb=copy(rb)
sheet=wb.get_sheet(0)
sheet.write(0,c,"Total")
sheet.write(0,c+1,"Percentage")
sheet.write(0,c+2,"Result")
for i in range(1,6):
    sheet.write(i,c,total[i-1])
for j in range(1,6):
    sheet.write(j,c+1,percentage[j-1])
for k in range(1,6):
    sheet.write(k,c+2,result[k-1])
wb.save(excel)