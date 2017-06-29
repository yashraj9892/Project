######### module for searching ###########
import urllib.parse as ub
import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent  ## https://pypi.python.org/pypi/fake-useragent
try:
  ua = UserAgent(cache=False)
except:
  pass

   
class pro:

  def __init__(self):
    self.url = ''
    self.header = { 'USER_AGENT' : ua.random}
      
  def latest(self):
    show=input("showname: ")
    show =ub.urlencode({'q': show})# results q=abc+defg replace spaces by + and append q= to the starting of the string
    print(show)
    self.url = 'https://www.google.co.in/search?'+show 
    print(self.url)
    abc= []
    
    for start in range(1):
        print ('########### page {} ############'.format(start+1))
        time.sleep(2)
        req=requests.get(self.url,headers=self.header)
        if( req.status_code == requests.codes.ok):      
            soup=BeautifulSoup(req.text,'lxml')
##            print(soup.find(id="fprs"))
##            print(soup.prettify())            
            for url in soup.find_all('a'):
               if (url.get("class") == ['spell']):
                   print(url.text)
                   break
               
##            print(abc[24])
##            if(soup.find(id="sp_requery")):
##                print(soup.find(id="sp_requery").text)
##            else:
##                print(" no spelling error")
        else:
            print("503")
        

r=pro()
r.latest()
