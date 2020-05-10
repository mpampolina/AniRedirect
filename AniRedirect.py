import pyperclip, webbrowser, re
import animepaheLink, anilistLink
from jikanpy import Jikan
jikan = Jikan()

animeFallback = 'https://animepahe.com'

MALRegex = re.compile(r'''
myanimelist.net/anime/
''', re.VERBOSE)

anilistRegex = re.compile(r'''
anilist.co/anime/
''', re.VERBOSE)

try:
    address = pyperclip.paste()

    if bool(MALRegex.search(address)):   # check if the link is MAL
        MALid = address.split('/')[4]
        search_result = jikan.anime(MALid)
        title = search_result['title']
        webbrowser.open(animepaheLink.getAnimePahe(title))

    elif bool(anilistRegex.search(address)):    # check if the link is Anilist
        ALid = address.split('/')[4]
        title = anilistLink.anilistTitle(ALid)
        webbrowser.open(animepaheLink.getAnimePahe(title))

    else:
        webbrowser.open(animeFallback)  # will launch animepahe's homepage if the selected link is invalid

except IndexError as error:
    print('Link is invalid. Please try again.')
