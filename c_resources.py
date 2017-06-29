############RESOURCES#############
import urllib.parse as ub
import requests
import time
from bs4 import BeautifulSoup
##from fake_useragent import UserAgent  ## https://pypi.python.org/pypi/fake-useragent
##ua = UserAgent(cache=False)

   
class pro:

  def __init__(self):
    self.url = ''
    self.header={}
    self.header['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)   AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
      
  def set_url(self):
    url_file=open('set_of_url.txt','w')
    
    heads=['INDEX of serial','INDEX of tv shows','Index of tv series']
    for i in heads:
        url_file=open('set_of_url.txt','a')
        show=i
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
    url_file.close()

  def unique_set(self):
    file_name='resource_1.txt'
    new_f = open( file_name,'w')
    abc=[]
    with open('set_of_url.txt') as f:
      for line in f:
##        print(line)
        len1=0
        line = line.strip('\n')
        len1 = line.find('serial')
        if(len1 !=-1):
          len1 = line[0:len1+6]
          
        elif (line.find('Serial')!=-1):
          len1 = line[0:line.find('Serial')+6]
          
        elif (line.find('Show')!=-1):
          len1 = line[0:line.find('Show')+4]
          
        elif (line.find('show')!=-1):
          len1 = line[0:line.find('show')+4]
          
        elif (line.find('series')!=-1):
          len1 = line[0:line.find('series')+6]
          
        elif (line.find('Series')!=-1):
          len1 = line[0:line.find('Series')+6]
          
        else:
          print(line)

        if( "..." not in line) :
           abc.append(len1)
    print(abc)
    seen = set()
    result = []
    for item in abc:
      if item not in seen:
        seen.add(item)
        result.append(item)
    print(result)
   
    for i in result:
      new_f.write(i+'/')
      new_f.write('\n')
 
    new_f.close()
    print("done")

       
   
r=pro()
r.set_url()
r.unique_set()


    

        
