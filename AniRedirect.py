import pyperclip, animepaheLink, webbrowser, re
from jikanpy import Jikan
jikan = Jikan()

animeFallback = 'https://animepahe.com'

MALRegex = re.compile(r'''
https://myanimelist.net/anime/
''', re.VERBOSE)

try:
    MALaddress = pyperclip.paste()

    if bool(MALRegex.search(MALaddress)):   # check if the link is MAL
        MALid = MALaddress.split('/')[4]

        search_result = jikan.anime(MALid)
        title = search_result['title']

        webbrowser.open(animepaheLink.getAnimePahe(title))

    else:
        webbrowser.open(animeFallback)  # will launch animepahe's homepage if the selected link is invalid

except IndexError as error:
    print('Link is invalid. Please try again.')
