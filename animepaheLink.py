import bs4, requests, traceback
import lxml

baseURL = 'https://animepahe.com'
directoryURL = 'https://animepahe.com/anime'


def getAnimePahe(name):
    try:
        res = requests.get(directoryURL)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')
        for div in soup.findAll('div', attrs={'class': 'col-12 col-md-6'}):
            if div.find('a')['title'] == name:
                urlextension = div.find('a')['href']
                return baseURL + urlextension

    except (requests.HTTPError, requests.ConnectionError, requests.Timeout):
        errorfile = open('animepahePortal_err_log.txt', 'a')
        errorfile.write(traceback.format_exc())
        errorfile.close()
        print('A connection error has occured. Traceback information was recorded in animepahePortal_err_log.txt')
