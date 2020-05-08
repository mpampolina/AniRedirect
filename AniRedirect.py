import pyperclip, animepaheLink, webbrowser
from jikanpy import Jikan
jikan = Jikan()

try:
    MALaddress = pyperclip.paste()
    MALid = MALaddress.split('/')[4]

    search_result = jikan.anime(MALid)
    title = search_result['title']

    webbrowser.open(animepaheLink.getAnimePahe(title))

except IndexError as error:
    print('Link is invalid. Please try again.')
