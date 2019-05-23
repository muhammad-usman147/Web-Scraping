import urllib3.request
from urllib.error import URLError,HTTPError,ContentTooShortError

def Download(url):
	print('Downloading',url)
	try:
		html=urllib3.request.urlopen(url).read()
	except (URLError,HTTPError,ContentTooShortError) as e:
		print("Download Error ",e)
		html=None
	return html
Download('http://www.quotes.toscrape.com')