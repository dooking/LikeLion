import requests
import csv
from bs4 import BeautifulSoup
from note import extract_info
final_result = []
file = open("notes.csv", mode = "w", newline='')
writer = csv.writer(file)

for i in range(5):
    print(f'{i+1} 번째 페이지 크롤링 중...')
    note_html = requests.get(
        f'https://search.shopping.naver.com/search/all.nhn?origQuery=%EB%85%B8%ED%8A%B8&pagingIndex={i+1}&pagingSize=80&viewType=list&sort=rel&frm=NVSHPAG&query=%EB%85%B8%ED%8A%B8')
    note_soup = BeautifulSoup(note_html.text, "html.parser")
    note_list_box = note_soup.find("ul", {"class": "goods_list"})
    note_list = note_list_box.find_all("li", {"class": "_itemSection"})
    final_result += extract_info(note_list)
writer.writerow(["title","price","img_src","link"])
for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['img'])
    row.append(result['link'])
    writer.writerow(row)
print("크롤링 끝")

# print(extract_info(note_list))
#title = note_list[0].find("div", {"class": "tit"}).find("a").string
#price = note_list[0].find("span", {"class": "price"}).text.strip()
#img_src = note_list[0].find("img",{"class" : "_productLazyImg"})['data-original']
