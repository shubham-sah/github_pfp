import requests 
from bs4 import BeautifulSoup as bs

github_user = input ('Input Github User: ')
url = 'https://github.com/' + github_user
request = requests.get(url)
soup = bs(request.content, 'html.parser')
profile_img = soup.find('img', {'alt' : 'Avatar'})['src']

print(profile_img)


