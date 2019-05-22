import urllib3
from bs4 import BeautifulSoup
def func1():
	http=urllib3.PoolManager()
	r=http.request('GET','http://bit.ly/1Ge96Rw.')
	bsobj=BeautifulSoup(r.data,features='html.parser')
	#namelist=bsobj.find_all('span',{"class":'red','class':'green'}) #retreive all the tag with this class
	namelist=bsobj.find_all('span',{'class':'green'}, limit=4) #it sets the limit of the retreiving values
	for i in namelist:
		print('--------------')
		print(i.get_text())
	print(namelist[1].get_text()) #you can also get specific text with this way also
def func2():
	http=urllib3.PoolManager()
	r=http.request('GET','http://bit.ly/1Ge96Rw.')
	bsobj=BeautifulSoup(r.data,features='html.parser')
	r=bsobj.find_all(text='the prince')#retreive the text in an array format
	print(r)
	print(len(r))
def func3():
	http=urllib3.PoolManager()
	html=http.request('GET','http://bit.ly/1Ge96Rw.')
	bsobj=BeautifulSoup(html.data,features='html.parser')
	r=bsobj.find_all(id='text')
	print(r) # showing all output with text
	print(r[0].get_text()) #printing only first tag
func3()