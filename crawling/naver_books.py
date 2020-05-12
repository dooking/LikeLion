import requests
import csv
from bs4 import BeautifulSoup
final_result = []
file = open("naver_books.csv", mode = "w", newline='')
writer = csv.writer(file)

def extract_info(note_list):
    result = []
    for note in note_list:
        title_box = note.find("a",{"class":"N=a:bta.title"})
        if title_box != None:
            title = title_box.string
        else:
            title ='없음'
        img_src_box = note.find("img")
        if img_src_box != None:
            img_src = img_src_box['src']
        else:
            img_src ='없음'
        link_box = note.find("a",{"class": "N=a:bta.title"})
        if link_box != None:
            link = link_box['href']
        else:
            link ='없음'
        author_box = note.find("a",{"class":"txt_name N=a:bta.author"})
        if author_box != None:
            author = author_box.string
        else:
            author ='없음'
        company_box = note.find("a",{"class":"N=a:bta.publisher"})
        if company_box != None:
            company = company_box.string
        else:
            company ='없음'
        price_box = note.find("em", {"class" : "price"})
        if price_box != None:
            price = price_box.string
        else:
            price ='없음'
        note_info = {
            'title': title,
            'img' : img_src,   
            'link' : link,
            'author' : author,
            'company' : company,
            'price': price, 
        }
        result.append(note_info)
        print(result)
    return result
    
for i in range(8):
    print(f'{i+1} 번째 페이지 크롤링 중...')
    note_html = requests.get(
        f'https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}')
    note_soup = BeautifulSoup(note_html.text, "html.parser")
    note_list_box = note_soup.find("ol", {"class": "basic"})
    note_list = note_list_box.find_all("li")
    final_result += extract_info(note_list)
writer.writerow(["title","img_src","link","author","company","price"])
for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['img'])
    row.append(result['link'])
    row.append(result['author'])
    row.append(result['company'])
    row.append(result['price'])
    writer.writerow(row)