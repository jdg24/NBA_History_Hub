import getpass

import db_utility as db
from base_crawler import BaseCrawler

url = "https://www.basketball-reference.com/teams/LAL/2019_games.html"

c = BaseCrawler()
blob = c.get_html(url)
text = c.get_response_text(blob)
soup = c.get_soup(text)
print(soup)

conn = db.connect(
        database="postgres", 
        username="galimijohn", 
        password=getpass.getpass('RDS Password:'),
        host="database-2.c4u4qfois9er.us-east-2.rds.amazonaws.com",
        port='5432')
print(conn)
