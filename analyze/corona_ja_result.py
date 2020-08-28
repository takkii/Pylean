import re
import threading
from requests_html import HTMLSession
from bs4 import BeautifulSoup

class corona_ja_result(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
      session = HTMLSession()
      response = session.get('https://corona-stats.online/Japan')
      soup = BeautifulSoup(response.text,"lxml")
      [s.decompose() for s in soup('style')]
      pat = re.compile(r"<[^>]*?>")
      corona_ja_result = (pat.sub("", soup.text))
      print(corona_ja_result)

thread = corona_ja_result()
thread.run()
