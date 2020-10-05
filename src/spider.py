# first import all necessary dependencies.
import requests
import re
from bs4 import BeautifulSoup
from src.db import DB


def scrape(id):
  '''Scrape function fetches the page record with the page_id provided,
  Raise an exception if page with the isn't found,
  Updates the page’s is_scraping attribute to true,
  Fetch the HTML content at the page url using requests,
  Parses the fetched HTML content to extract hyperlinks (Maximum 10),
  Deletes existing links that may have been previously saved for the page,
  Saves the newly extracted links to the database for the page,
  Updates the page’s is_scraping attribute to false,
  passes the scraped links to the links table on the database.
  '''
  try:
    the_url = DB.pages().fetch(id)
    if len(the_url) == 0:
      raise Exception
    the_url = the_url[0]
    address = the_url[0]
    DB().pages().update(id, 'True')
    web_request = requests.get(address)
    soup = BeautifulSoup(web_request.text, features='html.parser')
    list_of_links = []
    for link in soup.find_all('a', href = True):
      links = link['href']
      if re.search("^https", links):
        list_of_links.append(links)
    linksy = (list_of_links[:10])
    DB().links().delete(id)
    for url in linksy:
      DB().links().insert(url, id)
    DB().pages().update(id, 'False')
    return '===============Successfully scraped================'
  except Exception as e:
    print(e)