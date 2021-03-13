import re
from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://standb.herokuapp.com')
soup = BeautifulSoup(response.text, "lxml")
[s.decompose() for s in soup('style')]
pat = re.compile(r"<[^>]*?>")
rss_result = (pat.sub("", soup.text))
print(rss_result)
