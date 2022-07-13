from bs4 import BeautifulSoup

el = """
<ellipse cx="18.412" cy="36.504" data-name="Ellipse 11" fill="#50bf79" fill-opacity="0.46" id="4-l" rx="18.412" ry="36.504" transform="translate(52.353 710.423)"></ellipse>
"""

soup = BeautifulSoup(el, 'xml')
# p = soup.find(id='test1')
c = soup.find(id ="4-l")

print(c)