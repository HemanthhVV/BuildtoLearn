from urllib.request import urlopen
from bs4 import BeautifulSoup

lnk='https://www.nature.com/articles/s41598-023-28880-x'
get_lnk=BeautifulSoup(urlopen(lnk))
title=get_lnk.title.get_text()
print(title)
with open ("read_csv.csv","w") as file:
    file.write("Title of the web page:\n")
    file.write("\t"+title)