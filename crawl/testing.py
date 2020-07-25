from base_crawler import BaseCrawler

c = BaseCrawler()
blob = c.get_html('https://www.basketball-reference.com/teams/LAL/2019_games.html')
text = c.get_response_text(blob)
soup = c.get_soup(text)
print(soup)
