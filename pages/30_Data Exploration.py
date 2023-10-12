import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.title("Missing Values")

st.write("We conducted a comprehensive assessment of missing values using methods like isna and dropna. Columns with a high percentage of missing values were removed to ensure data quality.")

st.title("Dataset Integration")

st.write("We merged relevant datasets to create a unified dataset for analysis and modeling.")

st.title("Feature Engineering")

st.write("Language Preferences: We categorized song languages into the top eight languages, with values > 50000 entries and transformed them into quantitative variables.")

st.write("Sentiment Score Target: The VADER_average score was used to define the target variable sentiment_score, with a score greater than or equal to 0.5 representing positive sentiment (class 1) and class 0 otherwise. The vade average score is very similar to the vader min and max score. This assumption is supported with the correlation heatmap of the database sent_df.")

st.write("Feature Selection: We selected relevant audio features (e.g., instrumentalness, liveness, speechiness) as intrinsic properties for each song.")

st.title("Time Zone Standardization")

st.write("To reduce data complexity and enhance interpretability, we standardized the time_zone variable by converting values to Coordinated Universal Time (UTC).")

st.image("TZM.png", caption = "Time Zone Map and Cities")

st.write("All time zones with more than 1000 entries were selected. The following time zones and/ or continents were evaluated:")

tzm = {'Time Zone': ['North America & South America', 'North America', 'North America & Central America', 'Europe', 'Asia & Australia', 'Asia', 'Pacific', 'Middle East', 'Atlantic', 'Africa'], 
'Count': [1594515, 912066, 728307, 611216, 571797, 49186, 36677, 28957, 4825, 1856]}

tzm_df = pd.DataFrame(data=tzm)

#st.bar_chart(tzm_df, x = "Time Zone", y = "Count")

bar_chart = alt.Chart(tzm_df).mark_bar().encode(x=alt.X("Time Zone", sort = "-y"), y="Count")

st.altair_chart(bar_chart, use_container_width=True)

st.write("We conducted a deep dive into various dataset variables, including type, description, category, and missing values. The detailed variable descriptions can be found in Table 2 attached in the following link:")

st.write("https://docs.google.com/spreadsheets/d/1Nmor4kPkpkwikS4WESuT6rl3DUWBk46kSAO5XSXUpuY/edit#gid=0")

st.title("Feature Selection")

st.write("After rigorous analysis, we identified the following variables as particularly relevant for predicting music appreciation:")

st.write("Hashtag: An indicator of user emotional sentiment toward a specific piece of music.")

st.write("VADER_average: A quantitative sentiment score calculated using VADER (Valence Aware Dictionary and sentiment Reasoner), tailored for social media sentiment analysis.")

st.write("Among the four lexicons described in sentiment_values.csv dataset, Vader is the one which has been specifically designed for social media text analysis, including hashtags. Also, Vader lexicon can handle complexities of social media language, such as sarcasm, slang, and emoticons (Hutto and Gilbert 2014). Among the four Vader scores given in this dataset, “vader_average” seems to be useful for identifying the overall sentiment of the tweets related to a piece of music, while controlling for the number of tweets.")

sent_df = pd.read_csv('sentiment_values.csv', index_col = False)

# List of columns to plot
columns_to_plot = ["vader_avg", " afinn_avg", " ol_avg", " ss_avg"]

# Set up the figure
plt.figure(figsize=(6, 4))

# Define colors for each histogram
hist_colors = ['blue', 'green', 'red', 'black']

# Loop through the columns and create histograms with different colors
for i, column in enumerate(columns_to_plot):
    sns.histplot(data=sent_df, x=column, element='step', stat='frequency', common_norm=False, color=hist_colors[i], label=column)

plt.xlabel("Value Distribution")
plt.ylabel("Frequency")
plt.legend()
#plt.show()
txt="Average score for the four lexicons presented initially in sentiment_values.csv dataset"
plt.figtext(0.5, -0.1, txt, wrap=True, horizontalalignment='center', fontsize=12, fontstyle = 'italic')
st.pyplot(plt.gcf())

st.title("Audio Features")

st.write("The most relevant audio features are:")

st.write("- Instrumentalness: vocals or its absence in a music piece from 0 to 1")
st.write("- Liveness: presence of audience in a music recording. Higher values means higher probability of a live event or concert (from 0 to 1)")
st.write("- Speechness: presence of spoken word in a music track from 0 to 1")
st.write("- Danceability: values from 0 to 1 indication how danceable is a music piece being 0 no danceable")
st.write("- Valence: Level of “positivity” in a music track. A very positive track is 1")
st.write("- Loudness: Perceptual quality of sound which corresponds directly to the intensity or amplitude of the sound wave. Scale from -50 to 0 being 0 dB the maximal digital attachable loudness")
st.write("- Tempo: Estimated speed of a musical track measured in BPM beats per minute the majority of the “songs” are in the range from 50 bpm very slow to 200 bpm very fast")
st.write("- Energy: Measure which highly correlates with loudness. It is a subjective term describing excitement and overall level of activity of a music piece. Range from 0 to 1")
st.write("- Key: musical key of the track according to pitch")
st.write("- Mode: Related to the key of a musical track. It indicates if a track is in a minor key 0 or a major key 1")
st.write("- Acousticness: A measure in the range from 0 to 1 indicating the influence of acoustic instruments. 0 indicates only electronic instruments 1 indicate only acoustic instruments")

//cont_df = pd.read_csv('context_content_features.csv', usecols=range(0, 22))

//fig = plt.figure(figsize = (16, 16))

//plt.title('Histogram of all variables')

//plt.subplot(331)
//plt.hist(cont_df['instrumentalness'], bins = 20)  
//plt.xlabel('instrumentalness')
//plt.ylabel('counts')

//plt.subplot(332)
//plt.hist(cont_df['liveness'], bins = 20)  
//plt.xlabel('liveness')
//plt.ylabel('counts')

//plt.subplot(333)
//plt.hist(cont_df['speechiness'], bins = 20)  
//plt.xlabel('speechiness')
//plt.ylabel('counts')

//plt.subplot(334)
//plt.hist(cont_df['danceability'], bins = 20)  
//plt.xlabel('danceability')
//plt.ylabel('counts')

//plt.subplot(335)
//"""plt.hist(cont_df['valence'], bins = 20)  
plt.xlabel('valence')
plt.ylabel('counts')

plt.subplot(336)
plt.hist(cont_df['loudness'], bins = 20)  
plt.xlabel('loudness')
plt.ylabel('counts')

plt.subplot(337)
plt.hist(cont_df['tempo'], bins = 20)  
plt.xlabel('tempo')
plt.ylabel('counts')


plt.subplot(338)
plt.hist(cont_df['energy'], bins = 20)  
plt.xlabel('energy')
plt.ylabel('counts')

plt.subplot(339)
plt.hist(cont_df['key'], bins = 20)  
plt.xlabel('key')
plt.ylabel('counts');

st.pyplot(plt.gcf())

fig = plt.figure(figsize = (12, 3))

plt.title('Histogram of all variables')

plt.subplot(141)
plt.hist(cont_df['mode'], bins = 20)  
plt.xlabel('mode')
plt.ylabel('counts')

plt.subplot(142)
plt.hist(cont_df['acousticness'], bins = 20)  
plt.xlabel('acousticness')
plt.ylabel('counts')
txt="Content features regarding the track presented in context_content_features.csv"
plt.figtext(0.5, -0.1, txt, wrap=True, horizontalalignment='center', fontsize=12, fontstyle = 'italic');
st.pyplot(plt.gcf())"""


