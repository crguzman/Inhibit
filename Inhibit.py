#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=100, size=(800, 600))
display.start()

url = 'https://latammt.proscloud.com/UI/MasterTable.html'

print 'browsing with chrome2, ', url
try:
  browser = webdriver.Chrome()
  browser.get(url)
  print browser.title
  browser.quit()
except Exception as e:
  print e

display.stop()
