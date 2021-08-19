from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, UserInfo

class Browser():

	def __init__(self, url):

		# --------------------- Chrome Options ---------------------

		options = webdriver.ChromeOptions()
		options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

		path = "C:\\Users\\YourUserName\\Desktop\\Instagram Like Automation\\Chrome Driver"

		self.url = url
		self.browser = webdriver.Chrome(path, chrome_options=options)

		# --------------------- Chrome Options ---------------------

		# Profile Name
		UserInfo.Name = input("Enter A Profile Name: ")

		self.userName = UserInfo.Name

		# Call The Instagram Function
		self.Instagram()

	def Instagram(self):

		# Go To 'self.url' And Wait 1 Second
		self.browser.get(self.url)
		time.sleep(1)

		# Call The Login Function
		self.Login()

	def Login(self):

		# Select Email input and Password input And Wait 1 Second
		emailInput = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
		passwordInput = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")

		time.sleep(1)

		# Enter Email And Password And Wait 2 Second
		emailInput.send_keys(UserInfo.userName)
		passwordInput.send_keys(UserInfo.password)

		time.sleep(2)

		# Select And Click Login Button
		loginButton = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3)")
		loginButton.click()

		time.sleep(5)

		# Call The likeMessage Function
		self.likeMessage()

	def likeMessage(self):

		# Select And Click First Later Button And Wait 2 Second
		firstLaterButton = self.browser.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button")
		firstLaterButton.click()

		time.sleep(2)

		# Select And Click Second Later Button And Wait 2 Second
		secondLaterButton = self.browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
		secondLaterButton.click()

		time.sleep(2)

		# Go To Profile And Wait 5 Second
		self.browser.get(self.url + f"{self.userName}/")

		time.sleep(5)

		# Call The scrollDown Function And Wait 2 Second
		self.scrollDown()

		time.sleep(2)

		# Create A List Of Photos And Select Photos
		links = []
		containers = self.browser.find_elements_by_class_name("v1Nh3")

		# links Append Photos
		for link in containers:

			links.append(link.find_elements_by_tag_name("a"))

		# Select All Photos
		for likes in links:

			# Select 1 Photo And Click And Wait 3 Second
			for like in likes:

				like.click()

				time.sleep(3)

				# Select Like Button, Click And Wait 2 Second
				likeButton = self.browser.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")
				likeButton.click()

				time.sleep(2)

				# Select Exit Button, Click And Wait 1 Second
				exitButton = self.browser.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button")
				exitButton.click()
				
				time.sleep(1)

	def scrollDown(self):

		# Scroll Down Javascript Code
		javascriptCode = """

		page = document.querySelector(".js.logged-in.client-root.js-focus-visible.sDN5V");
		page.scrollTo(0, page.scrollHeight);
		var pageEnd = page.scrollHeight;
		return pageEnd;

		"""

		# Run Javascript Codes
		scroll = self.browser.execute_script(javascriptCode)

		while True:

			end = scroll

			time.sleep(1)

			scroll = self.browser.execute_script(javascriptCode)

			if end == scroll:

				break
