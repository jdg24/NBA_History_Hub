from base_crawler import BaseCrawler

url = "https://www.basketball-reference.com/teams/LAL/2019_games.html"

c = BaseCrawler()
blob = c.get_html(url)
text = c.get_response_text(blob)
soup = c.get_soup(text)
print(soup)
