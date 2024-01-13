from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import os
try:
	driver = webdriver.Firefox()
except:
	driver = webdriver.Chrome(executable_path='chromedriver.exe')

def string2list(s):
	a = list()
	for i in s.split('\n'):
		a.append(i.split(' '))
	return a
def ChuanHoaDuLieu_vietstock_web(s,sl):
	a = list()
	sl+=1
	#Chuan hoa phan du lieu truoc cho de
	for i in range(len(s)-1,len(s)-sl,-1):
		temp = list()
		name_row = "" #Lay ten hang
		for j in range(0,len(s[i])-4):
			name_row+=s[i][j]+" "
		temp.append(name_row)
		for k in s[i][len(s[i])-4:len(s[i])]:
			temp.append(k)
		#print(temp)
		a.insert(0,temp)
	#print(a)
	#Chuan hoa phan du lieu tieu de
	temp = list()
	for i in range(len(s)-sl,2,-3):
		name_row = ' '.join(s[i-2]) + ' '.join(s[i-1]) + ' '.join(s[i])
		temp.insert(0,name_row)
	#
	name = s[0][len(s[0])-2]+ ' '+s[0][len(s[0])-1] + ''.join(s[1]) + ' ' + ''.join(s[2])
	temp.insert(0,name)
	temp.insert(0,' '.join(s[0][0:len(s[0])-2]))
	a.insert(0,temp)
	#print(s[1])
	#print(s[2])
	return a
#Lay Du Lieu theo nam
def vietstock_web_year(thongso:list):
	#vietstock_web_pd = pd.DataFrame()
	kqkd = driver.find_element(By.ID,"table-0")
	kqkd = string2list(kqkd.text)
	table_kdkd=ChuanHoaDuLieu_vietstock_web(kqkd,thongso[0])
	table_kdkd_pd = pd.DataFrame(table_kdkd)
	#vietstock_web_pd.concat(table_kdkd_pd)
	#print(table_kdkd_pd)

	cdkt = driver.find_element(By.ID,"table-1")
	cdkt= string2list(cdkt.text)
	table_cdkt=ChuanHoaDuLieu_vietstock_web(cdkt,thongso[1])
	table_cdkt_pd = pd.DataFrame(table_cdkt)
	#vietstock_web_pd.concat(table_cdkt_pd)
	#print(table_cdkt_pd)

	cstc = driver.find_element(By.ID,"table-2")
	cstc = string2list(cstc.text)
	table_cstc=ChuanHoaDuLieu_vietstock_web(cstc,thongso[2])
	table_cstc_pd = pd.DataFrame(table_cstc)
	#vietstock_web_pd.concat(vietstock_web_pd)
	#print(table_cstc_pd)
	vietstock_web_pd = pd.concat([table_kdkd_pd,table_cdkt_pd,table_cstc_pd])
	return vietstock_web_pd
	#vietstock_web_pd.to_csv("./vietstock_web.csv", sep=',', index=False, encoding='utf-8')
#Lay du lieu tu web https://finance.vietstock.vn/PTV-ctcp-thuong-mai-dau-khi.htm
def vietstock_web_CTCP():
	driver.get('https://finance.vietstock.vn/PTV-ctcp-thuong-mai-dau-khi.htm')
	kqkd_l = driver.find_elements(By.CLASS_NAME,"btn")
	day1 = vietstock_web_year([5,5,6])
	#Tien hanh lay them du lieu
	driver.execute_script("arguments[0].click();", kqkd_l[21])
	day2 = vietstock_web_year([5,5,6])
	pd.concat([day2,day1]).to_csv("./1.vietstock_web_PTV.csv", sep=',', index=False, encoding='utf-8')
	print("Thanh Cong")
	os.system("pause")
def vietstock_web_BIDV():
	driver.get('https://finance.vietstock.vn/BID-ngan-hang-tmcp-dau-tu-va-phat-trien-viet-nam.htm')
	kqkd_l = driver.find_elements(By.CLASS_NAME,"btn")
	day1 = vietstock_web_year([5,9,5])
	#Tien hanh lay them du lieu
	driver.execute_script("arguments[0].click();", kqkd_l[21])
	day2 = vietstock_web_year([5,9,5])
	pd.concat([day2,day1]).to_csv("./2.vietstock_web_BIDA.csv", sep=',', index=False, encoding='utf-8')
	print("Thanh Cong")
	os.system("pause")
def vietstock_web_VCB():
	driver.get('https://finance.vietstock.vn/VCB-ngan-hang-tmcp-ngoai-thuong-viet-nam.htm')
	kqkd_l = driver.find_elements(By.CLASS_NAME,"btn")
	day1 = vietstock_web_year([5,9,5])
	#Tien hanh lay them du lieu
	driver.execute_script("arguments[0].click();", kqkd_l[21])
	day2 = vietstock_web_year([5,9,5])
	pd.concat([day2,day1]).to_csv("./3.vietstock_web_VCB.csv", sep=',', index=False, encoding='utf-8')
	print("Thanh Cong")
	os.system("pause")
if __name__ == '__main__':
	vietstock_web_CTCP()
	vietstock_web_BIDV()
	vietstock_web_VCB()
	driver.close()