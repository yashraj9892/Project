################ URL opener ############
import bs4
import urllib.request as ur
import requests

   
class pro:

  def __init__(self):
    self.url = ''
    self.header = { 'USER_AGENT' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}

  def latest(self):
    file_name='resource_1.txt'
    new_f = open( file_name,'w')
    with open('urlnew.txt') as f:
      for line in f:
##        print(line)
        line = line.strip('\n')
        len1 = line.find('serial')
        if(len1 !=-1):
          len1 = line[0:len1+6]
          if( "..." not in line) :
            new_f.write(len1+'/')
            new_f.write('\n')
        elif (line.find('Serial')!=-1):
          len1 = line[0:line.find('Serial')+6]
          if( "..." not in line) :
            new_f.write(len1+'/')
            new_f.write('\n')
        elif (line.find('Show')!=-1):
          len1 = line[0:line.find('Show')+4]
          if( "..." not in line) :
            new_f.write(len1+'/')
            new_f.write('\n')
        elif (line.find('show')!=-1):
          len1 = line[0:line.find('show')+4]
          if( "..." not in line) :
            new_f.write(len1+'/')
            new_f.write('\n')
        elif (line.find('series')!=-1):
          len1 = line[0:line.find('series')+6]
          if( "..." not in line) :
            new_f.write(len1+'/')
            new_f.write('\n')
        elif (line.find('Series')!=-1):
          len1 = line[0:line.find('Series')+6]
          if( "..." not in line) :
            new_f.write(len1+'/')
            new_f.write('\n')
        else:
          print(line)
        
    new_f.close()
    print("done")  
        
   
r=pro()
r.latest()
