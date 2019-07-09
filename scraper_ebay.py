from bs4 import BeautifulSoup
import requests
import smtplib
import python_generate_password as pgp
import time
header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
url='https://www.ebay.com/itm/Google-Chrome-Pixel-book-Core-I7-7y75-touch-screen-webcam-16GB-RAM-512GB-SSD/273907328322?hash=item3fc6262542:g:OgIAAOSwyNtdFREJ'
def EbayParser():
    
    page=requests.get(url,headers=header)
    soup=BeautifulSoup(page.content,'html.parser')
    titletext=soup.find(id='itemTitle').get_text()
    price=soup.find(id='prcIsum').get_text()
    if float(price[4:]) >= 500:
        send_mail()
    
def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('ushakeel808@gmail.com',pgp.password)
    subject='PRICE FELL DOWN'
    body='PRICE FELL DOWN \n CLICK THE LINK BELOW \n https://www.ebay.com/itm/Google-Chrome-Pixel-book-Core-I7-7y75-touch-screen-webcam-16GB-RAM-512GB-SSD/273907328322?hash=item3fc6262542:g:OgIAAOSwyNtdFREJ'
    msg=f'Subject: {subject} \n\n {body}'
    server.sendmail(   'ushakeel808@gmail.com', 'ushakeel909@gmail.com',  msg )
    print("EMAIL HAS BEEN SEND")
    server.quit()
while True:
    EbayParser()
    time.sleep(60)