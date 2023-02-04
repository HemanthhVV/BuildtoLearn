from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4
lnk="https://www.nature.com/articles/s41598-023-28880-x"
'''get_lnk=requests.get(lnk)
soup=bs4(get_lnk.text,'html.parser')
div_bs4 = soup.find('div', id = "Abs1-content")
print(div_bs4.string)
for paraa in div_bs4.findall("p"):
    print(para.get_text())
#print(BeautifulSoup(get_lnk.content).select('div.c-article-section__content'))
'''
url=urlopen(lnk)
content=url.read()
soup=bs4(content,'lxml')
table=soup.findAll('div',attrs={"class":"c-article-section__content","id":"Abs1-content"})
li=[]
count=0
str1=""
for x in table:
    li.append((x.find('p').text))
for i in li:
    str1+=i
a=str1.split()
count=len(a)
with open ("read_csv.csv","a",encoding="utf-8") as file:
    file.write("\n\nAbstarct of the page:")
    file.write("\t"+str1)
    file.write("count of the word:")
    file.write(count)