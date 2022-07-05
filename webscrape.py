#Web scraping the coreyms.com website and storing the data in csv file

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scarpe.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

#For all the article
for article in soup.find_all('article'):
	headline = article.h2.a.text
	print(headline)

	summary = article.find('div', class_='entry-content').p.text
	print(summary)

	try:
		vid_src = article.find('iframe', class_='youtube-player')['src']
	
		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]
	
		yt_link = f'http://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link = None

	print(yt_link)

	print()

	csv_writer.writerow([headline,summary,yt_link])

csv_file.close()

#-----------------------------------------------------------

	#For single article
"""
article = soup.find('article')

#print(article.prettify())

#headline = article.h2.a.text
#print(headline)

#summary = article.find('div', class_='entry-content').p.text
#print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
#print(vid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
#print(vid_id)

yt_link = f'http://youtube.com/watch?v={vid_id}'
print(yt_link)
"""