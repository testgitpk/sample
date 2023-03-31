r=requests.get('http://bola.kompas.com/')
soup=BeautifulSoup(r.content,'html.parser')
link=[]
for i in soup.find('div',{'class','most__warp'}.find_all('a'):
   i['herf']=i['herf']+'?page=all'
   limk.append(i['herf'])
documen=[]
for i in link:
    r=reqest.get(i)
    soup=BeautifulSoup(r.content,'html.parser')
    sen=[]
    for i in soup.find('div',{'class':'read__content'}.find_all('p'):
       sen.append(i.text)
       documents.append(' '.join(sen))
               
