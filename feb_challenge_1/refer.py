from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4
'''lnk="https://www.nature.com/articles/s41598-023-28880-x"
url=urlopen(lnk)
soup = bs4(url, 'lxml')
l=[]
str1=''
all_links = soup.findAll("div",attrs={"class":"c-article-section__content","id":"Bib1-content"})
for link in all_links:
    l.append(link)
for i in l:
    str1+=str(i)
with open ("rra_csv.csv","w",encoding="utf-8") as file:
    file.write(str1)'''
str2=''
lnk="rra_csv.csv"
url=open(lnk)
soup= bs4(url,'lxml')
l2=[]
for i in soup.findAll('a'):
    l2.append(i.get("href"))
for i in l2:
    str2+="\n"
    str2+=str(i)
with open ("references.csv","w") as f1:
    f1.write(str2)
f1.close()