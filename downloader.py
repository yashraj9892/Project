import urllib.request as ur
from fake_useragent import UserAgent

class download:
    def __init__(self):
        self.url=''
        try:
            ua = UserAgent(cache=False)
        except FakeUserAgentError:
            pass
        self.headers=ua.random

    def download(self):
        url_file = open('urls_download.txt','r')
        for line in url_file:
            self.url = line
            req= ur.urlopen(self.url)
            file_name = self.url.split('/')[-1]
            f = open(file_name,'ab')
            file_size = (req.info().values()[3])    #req.info() returns a dictionary
            print( "Downloading : {} Bytes: {} ".format(file_name,file_size/1024/1024)
            
            download_status=0
            block_size= 1205862.4
            while True:

                buff= req.read(block_size)
                if not buff:
                   break;
                downloaded_status += len(buff)
                f.write(buff)
                download_status = "{%3.2f}".format(downloaded *100.00/ file_size)
                print(download_status)
            f.close()
            print(file_name," downlaoded ")     
                   
                       
        
