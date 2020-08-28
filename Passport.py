import sys
import file
import excel
import browser

# find file
clients = file.find_excel("data")

if clients = None or len(clients) == 0:
	print("excel file not found")
	sys.exit("excel file not found")

# ask credentials
email = input("Enter username: ")
pwd = input("Enter password: ")

# read data from excel
data = excel.read_excel("data/" + clients[0])

# login & compose drafts
browser.login_composedrafts(email,pwd, data)
