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
    url_file=open('urlnew2.txt','a')
    show ='INDEX of Serials '+show+' 720p'
    show =ub.urlencode({'q': show})# results q=abc+defg replace spaces by + and append q= to the starting of the string
    print(show)
    self.url = 'https://www.google.co.in/search?'+show+'&start='         # &start= is basically the page number in *10 format so for page 1 it
                                                                       # will be (1-1)*10 =0 and for page 2 it will be (2-1)*10 =10  inshort n-1*10
    print(self.url)
    
    
    for start in range(2):
        print ('########### page {} ############'.format(start+1))
        time.sleep(2)
        req=requests.get(self.url+str(start*10),headers=self.header)
        if( req.status_code == requests.codes.ok):      
            soup=BeautifulSoup(req.text,'lxml') 
            for url in soup.find_all('cite'):
              if( url.text[0:2] == 'dl'):
                print(url.text)  
                url_file.write(url.text)
                url_file.write('\n')
        else:
            print("503")
    url_file.close()

        

r=pro()
r.latest()
