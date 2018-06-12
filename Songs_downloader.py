import requests
from bs4 import BeautifulSoup

import  os

os.chdir("C:" + os.path.join(os.environ["HOMEPATH"], "Desktop"))


def download_song(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    song_name = ""
    for name in soup.find_all('h1', {'class': 'title'}):
        song_name = str(name.text).replace("Download","").replace("Mp3","").replace("\"","").strip()
    for song in soup.find_all('a', {'id': 'dn'}, href=True):
        link = song.get('href').replace(" ","%20")
        print("Downloading song ...")
        respons = requests.get(str(link))

        with open(song_name+".mp3" , "wb") as f:
            f.write(respons.content)
            print("done downloading")

# yt2converter.com/yt-dd.php?id=hbnPkK76Ask&hash=cdb9e7b5644e7abe209835f1fc7fd110&t=306&name=Beyonc%C3%A9%20-%20Ego

def get_path(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for num, down_link in enumerate(soup.find_all('div', {'class': 'meta'})):
        print(str(num)+":)",down_link.text.replace("play","").replace("download",""))
    song_id = int(input('choose song id : \n'))
    songes_links = soup.find_all('a', {'class': 'downnow'})
    song_link = songes_links[song_id].get("href")
    download_song(song_link)


search_word = str(input('Enter your image name for search on \n'))
get_path('http://www.instamp3.tv/download/' + search_word + '.html')
