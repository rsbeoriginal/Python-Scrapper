import urllib2
from bs4 import BeautifulSoup
link='http://blog.aiesec.in/'
def scrap(link):
	response = urllib2.urlopen(link)
	html = response.read()
	soup=BeautifulSoup(html)
	print 'Page Title: '+soup.title.string
	print 'Page Link: '+link
	for post in soup.find_all('div',{'class':'post-item'}):
		print '\tArticle'
		for div in post.find_all('div',{'class':'post-header'}):
			for h2 in div.find_all('h2'):
				for a in h2.find('a'):
					print '\t\tHeader: '+a
		date=post.find('span',{'class':'date'})
		print "\t\tDate:"+date.text
		try :
			img=post.find('img')
			print "\t\timgURL="+img['src']		
		except Exception,e :
			pass
def findpagelinks(link):
	response = urllib2.urlopen(link)
	html = response.read()
	soup=BeautifulSoup(html)
	sidebar=soup.find('div',{'class':'row-fluid-wrapper row-depth-1 row-number-5 '})
	div=sidebar.find('div',{'class':'block'})
	list_links=div.find('ul')
	for list_item in list_links.find_all('li'):
		a=list_item.find('a')
		#print "Link: "+ a['href']
		scrap(a['href'])
findpagelinks(link)