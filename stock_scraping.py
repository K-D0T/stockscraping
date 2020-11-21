import bs4 
import requests
from splinter import Browser
import time

while True:
	time.sleep(5)
	def buy():
		print("Time to buy")
		print("The price for",stock1[0], "is 20% below the mean.")
		yesno = input("Do you want to buy? y/n: ")
		if yesno == "y":
			executable_path = {'executable_path':'/Users/Kaiden Thrailkill/Desktop/Environment/geckodriver/geckodriver.exe'}
			b = Browser('firefox', **executable_path)
			b.visit('https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https://www.yahoo.com')
			b.fill('username', 'kaiden.thrailkill@yahoo.com')
			b.find_by_xpath('//*[@id="login-signin"]').click()
			b.fill('password', 'KEka2407!')
			b.find_by_xpath('//*[@id="login-signin"]').click()
			b.visit(url)
			b.quit()
		else:
			print("Okay sounds good :)")
			pass

	def sell():
		print("Time To Sell")
		print("The price for",stock[0], "is at least 50% Above the mean.")
		yesno = input("Do you want to sell? y/n:  ")
		if yesno == "y":
			executable_path = {'executable_path':'/Users/Kaiden Thrailkill/Desktop/Environment/geckodriver/geckodriver.exe'}
			b = Browser('firefox', **executable_path)
			b.visit('https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https://www.yahoo.com')
			b.fill('username', 'kaiden.thrailkill@yahoo.com')
			b.find_by_xpath('//*[@id="login-signin"]').click()
			b.fill('password', 'KEka2407!')
			b.find_by_xpath('//*[@id="login-signin"]').click()
			b.visit(url)
			b.quit()
		else:
			print("Okay sounds good :)")
			pass


	def owned():
		print("")
		print("")
		print("CHECKING OWNED STOCK CODES... ")
		print("")
		print("")
		f = open("owned_stock_codes.txt","r")
		for codes in f:
			global stock
			stock = []
			stock.append(codes.strip())

			try:
		
				print("")
				global url
				url = ('https://finance.yahoo.com/quote/' + stock[0] + '/history?period1=1554249600&period2=1585872000&interval=1d&filter=history&frequency=1d')

				r = requests.get('https://finance.yahoo.com/quote/' + stock[0] + '/history?period1=1554249600&period2=1585872000&interval=1d&filter=history&frequency=1d').text
				soup = bs4.BeautifulSoup(r, 'lxml')
				

				current = soup.findAll('td', class_='Py(10px) Pstart(10px)')

				#print(current)
				price = []
				for i in current:
					price.append(str(i.get_text()))

				
				updated_price = price[3::6]
				
				for x in updated_price:
					float_price = map(lambda a:float(a.replace(",","")),updated_price)


				close = (list(float_price))

				Sum = sum(close)

				percent_below_mean = ((Sum / len(close))*0.20)
				percent_above_mean = ((Sum / len(close))*0.50)

				above_mean = ((Sum / len(close))- percent_above_mean)
				above_mean1 = above_mean

				below_mean = ((Sum / len(close))- percent_below_mean)
				below_mean1 = below_mean
				if close[0] >= above_mean1:
					sell()
				else:
					print(stock[0], "is not ready to sell")

			except:
				print("Something Went Wrong")

		wanted()
	def wanted():
		print("")
		print("")
		print("CHECKING WANTED STOCK CODES... ")
		print("")
		print("")
		k = open("wanted_stock_codes.txt","r")
		for codes1 in k:
			global stock1
			stock1 = []
			stock1.append(codes1.strip())

			try:
		
				print("")
				global url
				url = ('https://finance.yahoo.com/quote/' + stock1[0] + '/history?period1=1554249600&period2=1585872000&interval=1d&filter=history&frequency=1d')

				r = requests.get('https://finance.yahoo.com/quote/' + stock1[0] + '/history?period1=1554249600&period2=1585872000&interval=1d&filter=history&frequency=1d').text
				soup = bs4.BeautifulSoup(r, 'lxml')
				

				current = soup.findAll('td', class_='Py(10px) Pstart(10px)')

				#print(current)
				price = []
				for i in current:
					price.append(str(i.get_text()))

				
				updated_price = price[3::6]
				
				for x in updated_price:
					float_price = map(lambda a:float(a.replace(",","")),updated_price)


				close = (list(float_price))

				Sum = sum(close)

				percent_below_mean = ((Sum / len(close))*0.20)
				percent_above_mean = ((Sum / len(close))*0.50)

				above_mean = ((Sum / len(close))- percent_above_mean)
				above_mean1 = above_mean

				below_mean = ((Sum / len(close))- percent_below_mean)
				below_mean1 = below_mean
				
				if close[0] <= below_mean1:
					buy()
				else:
					print(stock1[0], "is not ready to be bought")
				
			except:
				print("Something Went Wrong")
	owned()
























