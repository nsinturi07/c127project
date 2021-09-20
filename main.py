from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
read=requests.get(url)
soup=BeautifulSoup(read.content, "html.parser")
soupTable=soup.find("table")
#print(soupTable)
list=[]
tableRow=soupTable.find_all("tr")
for tr in tableRow:
    td=tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    list.append(row)
starName=[]

radius=[]
distance=[]
mass=[]
for i in range (1,len(list)):
    starName.append(list[i][1])
    radius.append(list[i][6])
    distance.append(list[1][3])
    mass.append(list[i][5])


df2 = pd.DataFrame(list(zip(starName,distance,mass,radius)),columns=['Star_name','Distance','Mass','Constellation'])
print(df2)

df2.to_csv('bright_stars.csv')