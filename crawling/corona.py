import requests
from bs4 import BeautifulSoup
import csv
file = open("corona.csv", mode = "w", newline='')
writer = csv.writer(file)

hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'

hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")
tbody = hospital_soup.find("tbody",{"class":"tb_center"})
tboxes= tbody.find_all("tr")
cnt = 0
results = []
for tbox in tboxes:
    print(cnt, "번째줄 크롤링 하는중")
    table = tbox.find_all("td")
    data = []
    for row in range(len(table)):
        if(row == 2):
            data.append(table[row].text.replace("*(검체채취 가능)",""))
        else:
            data.append(table[row].string)
    results.append(data)
    cnt +=1

writer.writerow(["시도","시군구","선별진료소","전화번호"])
for result in results:
    writer.writerow(result)       