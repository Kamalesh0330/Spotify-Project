# 🎧 Spotify Track Info Extractor using Spotipy & MySQL

## 📝 Description

This project uses the Spotipy Python library (Spotify Web API) to extract real-time track information using only **Spotify track links** provided by the user. The fetched data — including artist name, duration, and popularity — is stored in a MySQL database for further analysis.

This project demonstrates how to collect and store music metadata from external APIs as part of a real-world data extraction and storage pipeline.

---

## ⚙️ Tech Stack

- **Language**: Python  
- **Library**: Spotipy (Spotify Web API client)  
- **Database**: MySQL  
- **Environment**: Localhost (Python environment + MySQL Connector)

---

## 🚀 Key Features

- ✅ Accepts **Spotify track links** from the user
- ✅ Fetches details like track name, artist, duration, and popularity
- ✅ Stores structured data into a MySQL database
- ✅ Handles OAuth2 authentication with Spotify via Spotipy
- ✅ Prepares the dataset for SQL-based analysis



```bash
🔗 Sample Input: 
https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3

📊 Output:
Track: Shape of You  
Artist: Ed Sheeran  
Duration: 233712 ms  
Popularity: 85  
🧠 What I Learned
How to authenticate with the Spotify API using OAuth2

Extracting data using Spotipy from Spotify track URLs

Writing Python code to connect and insert into MySQL

Structuring external API data into relational databases

Basic concepts of ETL (Extract → Transform → Load)

🔗 How to Run
Clone the repository

Install required libraries:

bash
Copy
Edit
pip install spotipy mysql-connector-python
Set your Spotify API credentials:

Create an app at: https://developer.spotify.com/dashboard

Add client_id and client_secret in your Python script

Run the script and paste a Spotify track link when prompted

Check your MySQL table for stored results

📌 Future Improvements
Add batch processing (multiple links at once)

Automate and schedule with cron or Airflow

Build a UI using Streamlit or Flask for user-friendly access

🚀 Built with curiosity and passion by Kamalesh D