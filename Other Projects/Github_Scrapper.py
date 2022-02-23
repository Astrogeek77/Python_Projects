import requests
from bs4 import BeautifulSoup as bs

github_username = input('Enter github username: ')
# github_username = 'astrogeek77'
url = 'https://github.com/' + github_username

r = requests.get(url)
soup = bs(r.content, 'html.parser')

profile_image_src = soup.find('img', {'alt': 'Avatar'})['src']
# profile_markdown = soup.find('article', {'class': 'markdown-body'}).get_text()
profile_name = soup.find('span', {'class' : 'vcard-fullname'}).get_text()

markdown_name = 'markdown_' + github_username

# f = open("{}".format(markdown_name), 'w')
# f.write(profile_markdown)
print(profile_image_src)
print(profile_name)
