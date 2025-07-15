from spotipy.oauth2 import SpotifyClientCredentials
import re
import matplotlib.pyplot as plt
import spotipy
import mysql.connector

s=spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id='4921d1577b874b7e86bb2104138db4c0',
        client_secret='d0fbcd0298c3429191a742e7e81d94c5'))

connection=mysql.connector.connect(
    host='localhost',
    password='keerthi@0330kamalesh',
    database='spotify',
    user='root')
cursor=connection.cursor()

file=r"C:\Users\kamal\OneDrive\Documents\Desktop\Project Git\Spotify-Project\playlist.txt"
with open(file,'r') as fp:
    urls=fp.readlines()
track_data_list=[]
for i in urls:
    i=i.strip()
    try:
        r=re.search(r'track/([a-zA-Z0-9]+)',i)
        if not r:
            print(f"Skipped the {i}")
            continue
        track_id=r.group(1)
        track=s.track(track_id)
        t_data={
            'Track Name':track['name'],
            'Artist':','.join([a['name'] for a in track['artists']]),
            'Album':track['album']['name'],
            'Popularity':track['popularity'],
            'Duration':track['duration_ms']/6000
            }
        query="insert into songs(track,artist,album,popularity,duration) values(%s, %s, %s, %s, %s)"
        cursor.execute(query,(t_data['Track Name'],t_data['Artist'],t_data['Album'],t_data['Popularity'],t_data['Duration']))
        connection.commit()
        print(f"Iserted and Collected: {t_data['Track Name']}")
        track_data_list.append(t_data)

    except Exception as e:
        print(f"Error:{e}")
connection.close()
cursor.close()

for t_data in track_data_list:
    feature=['Popularity','Duration']
    values=[t_data['Popularity'],t_data['Duration']]
    plt.figure(figsize=(4,5))
    plt.bar(feature,values,color='purple',edgecolor='black')
    plt.ylabel('Value')
    plt.title(t_data['Track Name'])
    plt.pause(2)
    plt.close()
        
