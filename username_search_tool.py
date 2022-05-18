#username search tool
import webbrowser
import time 
import os

#defs 
def tab():
	print("\t\t\t\t")
	
def webb():
	webbrowser.open_new(url)

def menu():
	a = "----------------------------------"
	aa = (a+a)
	print(aa)
	tab()
	print("\t\t\tusername_searching_tool")
	tab()
	print(aa)
	
	
#globle vareable
slash = "/"


#code here
#webbrowser.open_new("https://google.com/search?q=hantai")

#nav area
menu()


#✓
print("Instagram")
main_site = input("enter main site url:  ")

url = "https://" + main_site + slash + input("enter username: ")

#execution

webb()
