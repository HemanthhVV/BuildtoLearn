import requests
from bs4 import BeautifulSoup
def getdata(url):
    r = requests.get(url)
    return r.text

count=0
htmldata = getdata("https://www.nature.com/articles/s41598-023-28880-x")
soup = BeautifulSoup(htmldata, 'html.parser')
for i in soup.find_all("img"):
    count=count+1
a="\n\nCount of the images:{0}".format(count)
print(a)
with open ("read_csv.csv","a") as file:
    file.write(a)