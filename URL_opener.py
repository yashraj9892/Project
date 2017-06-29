################ URL opener ############
import bs4
import urllib.request as ur
import requests

   
class pro:

  def __init__(self):
    self.url = ''
    self.header = { 'USER_AGENT' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}

  def latest(self):
    url_file=open('resource_2.txt','a')
    with open('resource_1.txt') as f:
      for line in f:
##        print(line)
        self.url ='http://'+ line.strip('\n')
        try:
          req = requests.get(self.url,headers = self.header)
##              print(req.status_code)
          if(req.status_code==200):
            url_file.write(self.url)
            url_file.write('\n')
            print(self.url)
          else :
            pass
        except Exception as e:
              print(str(e))
    url_file.close()
        


   
r=pro()
r.latest()
