#stock.py
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req

def thaistock(code):

	url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={}&ssoPageId=10&selectPage=2'.format(code)
	webopen = req(url)
	page_html = webopen.read()
	webopen.close()
	data = soup(page_html,'html.parser')

	price = data.findAll('div',{'class':'col-xs-6'})

	title = price[0].text
	stockprice = price[2].text

	change = price[3].text
	change = change.replace('\n','')
	change = change.replace('\r','')
	change = change.replace('\t','')
	change = change.replace(' ','')
	change = change[11:]

	pchange = price[4].text
	pchange = pchange.replace('\n','')
	pchange = pchange.replace('\r','')
	pchange = pchange.replace(' ','')
	pchange = pchange[12:]

	update = data.findAll('span',{'class':'stt-remark'})
	stockupdate = update[0].text
	stockupdate = stockupdate[13:]

	print([title,stockprice,change,pchange,stockupdate])

	return [title,stockprice,change,pchange,stockupdate]



