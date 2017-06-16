# Takes Gutenberg Project URL and converts it to APA reference.
# No, I have made no effort to make the code denser or simpler, and I am not going to make the effort, but feel free to send me your suggestions.

import requests, re
from bs4 import BeautifulSoup as bs

ebook = input("eBook URL: ")
soup = bs(requests.get(ebook).text, "xml")
titles = soup.find('table', {'class':'bibrec'}).findAll('th')
content = soup.find('table', {'class':'bibrec'}).findAll('td')

for x in range(0,len(titles)):
	# AUTHOR
	if titles[x].contents[0] == 'Author':
		author = content[x].find('a').contents[0].split(',')
		author = author[0].strip() + ', ' + author[1].lstrip()[0] + '.'
	# TITLE
	elif titles[x].contents[0] == 'Title':
		title = content[x].contents[0].strip()
	# YEAR
	elif titles[x].contents[0].replace('\xa0', ' ') == 'Release Date':
		year = content[x].text
		year = re.findall('\d{4}', year)[0]

ref = author + ' (' + year + '). ' + title + '. Retrieved from: ' + ebook + '.'
print(ref)
