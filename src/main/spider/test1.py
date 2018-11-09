import urllib.request as urlrequest
from bs4 import BeautifulSoup

douban_url = 'https://movie.douban.com/subject/3319755'

page = urlrequest.urlopen(douban_url).read()
soup = BeautifulSoup(page,'html.parser')

title = soup.find('h1').span.get_text()
score = soup.find(class_ = 'll rating_num').get_text()
daoyan = soup.find(id = 'info').find_all('span')[0].get_text()
date = soup.find(id='info').find_all('span')[16].get_text()
address = soup.find(id='info').find_all('span')[17].get_text()
print('{},{},{},{},{}'.format(title,score,daoyan,date,address))