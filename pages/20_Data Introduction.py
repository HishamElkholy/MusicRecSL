import streamlit as st
import pandas as pd

st.title("Twitter Datasets")

st.write("We collected three Twitter datasets (Table 1) containing a total of 11.6 million music listening events, involving 139,000 users and 346,000 tracks. These datasets provided valuable insights into user behavior, context, and sentiment related to music.")

df = pd.DataFrame([["user_track_hashtag_timestamp.csv", "Information about each listening event","Id, the user_id, hashtag, created_at","",""],
["context_content_features.csv","All context and content features","User_id, track_id, artist_id","Content features:\nInstrumentales, liveness, speechiness, among others \n \n Context features:\nCoordinates, place, geo, tweet_language, time_zone",""],
["sentiment_values.csv","Sentiment information for hashtags","Sentiment dictionaries: AFINN, Opinion Lexicon, Sentistrength Lexicon and Vader","For each dictionary: Minimum, maximum, sum and average values","Values can be equal as most hashtags only consist of a single token"]], 
columns = (["Dataset Name", "Content", "Features", "Additional Features or Details", "Observation"]))

st.table(df.set_index(df.columns[0]))

st.title("Spotify Dataset")

st.write("Additionally, we incorporated a dataset from Spotify, encompassing 125 different music genres. This dataset included essential information, such as user-track interactions and audio features like danceability and loudness.")