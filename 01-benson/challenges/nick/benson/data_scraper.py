import requests
from pprint import pprint
import bs4
import urllib2

root_url = 'http://web.mta.info/developers/'
index_url = root_url + 'turnstile.html'

def get_mta_txt_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text)
    urls = [root_url + a.attrs.get('href') for a in soup.select('div.span-84 a[href^=]')]
    with open("all_mta_data.txt", "w") as mta_data:
      for url in urls:
        webfile=urllib2.urlopen(url).read()
        mta_data.write(webfile)


def export_to_txt(text_file_url):
    webfile=urllib2.urlopen(text_file_url)
    locfile=open("all_mta_dat.txt","w")
    locfile.write(webfile.read())
    locfile.close()
    webfile.close()

def write_em_all():
  url_list = get_mta_txt_urls()
  for url in url_list:
    pprint("In Goes The Data")
    pprint(url)
    export_to_txt(url)

# write_em_all()

# pprint(get_mta_txt_urls())
get_mta_txt_urls()