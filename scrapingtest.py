import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sorting(hnlist):
	return sorted(hnlist, key = lambda k:k['Votes'], reverse = True)

def create_hn(links, subtext):
	hs = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hs.append({'Title': title, 'Link': href, 'Votes': points})
	return sorting(hs)


pprint.pprint(create_hn(links, subtext))



