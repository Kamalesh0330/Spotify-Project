from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import re
import mysql.connector

s=spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='4921d1577b874b7e86bb2104138db4c0',client_secret='d0fbcd0298c3429191a742e7e81d94c5'))

connection=mysql.connector.connect(host='localhost',database='spotify',user='root',password='keerthi@0330kamalesh')
cursor=connection.cursor()

file='playlist.txt'
with open(file,'r') as fp:
    urls=fp.readlines()

for i in urls:
    i=i.strip()
    try:

        r=re.search(r'track/([a-zA-Z0-9]+)',i).group(1)
        track=s.track(r)
        t_data={'Track Name':track['name'],'Artist':','.join([a['name'] for a in track['artists']]),'Album':track['album']['name'],'Popularity':track['popularity'],'Duration':track['duration_ms']/60000}
        query="Insert Into songs(track,artist,album,popularity,duration) values(%s, %s, %s, %s, %s)"
        cursor.execute(query,(t_data['Track Name'],t_data['Artist'],t_data['Album'],t_data['Popularity'],t_data['Duration']))
        connection.commit()

    except Exception as e:
        print(f'{t_data['Track Name']} is sing by {t_data['Artist']}') 

cursor.close()
connection.close()