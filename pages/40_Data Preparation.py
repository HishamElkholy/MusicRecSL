import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

st.title("Data Cleaning & Transformation")

st.write("The datasets underwent meticulous cleaning and processing:")

st.write("- From the sentiment_values.csv dataset, we selected the VADER lexicon and dropped unnecessary columns.")

st.write("- The user_track_hashtag_timestamp.csv dataset had only one missing value for the hashtag variable, which was removed. It was then merged with the sentiment dataset.")

"""- A more extensive preprocessing was performed on the context_content_features.csv dataset, including:
	- Dropping columns with high missing value percentages: Coordinates, geo and place columns were dropped as these variables contained around 99% of missing values.
	- Limiting the lang variable to the top eight languages with more than 50000 entries."""

#cont_df = pd.read_csv('context_content_features.csv', usecols=range(0, 22))

#fig, ax2 = plt.subplots(1, figsize=(8, 8))

#lang_counts = cont_df['lang'].value_counts().nlargest(15)
#ax2.bar(lang_counts.index, lang_counts.values)
#ax2.set_yscale('log')
#ax2.set_title('Top 15 Languages')
#ax2.set_xlabel('Language')
#ax2.set_ylabel('Count')
#ax2.tick_params(axis='x', rotation=90)
#txt="Top 15 Languages for lang feature which describe the language song. The first 8 languages have more than 50000 entries"
#plt.figtext(0.5, -0.1, txt, wrap=True, horizontalalignment='center', fontsize=12, fontstyle = 'italic');
#st.pyplot(plt.gcf());
#plt.show();

"""		
	- Merging it with the previous dataset.
- Spotify dataset was not further incorporated in this study as no way was found to merge it with the previous dataset."""



st.title("Addressing Class Imbalance")

st.write("The dataset exhibited a significant class imbalance for the target variable (sentiment_score), with nearly 99% of the data belonging to class 1.")

percentage_1 = 96
percentage_0 = 4

labels = ['1', '0']
values = [percentage_1, percentage_0]
colors = ['yellow', 'blue']

fig2, ax1 = plt.subplots(1, figsize=(8, 8))

ax1.bar(labels, values, color=colors)

ax1.set_xlabel('Sentiment_score')
ax1.set_ylabel('Percentage (%)')
ax1.set_title('Percentage of Sentiment Values')

txt="Original Class 1 and Class 0 percentage in the final data set after merging"
plt.figtext(0.5, -0.01, txt, wrap=True, horizontalalignment='center', fontsize=12, fontstyle = 'italic');
st.pyplot(plt.gcf());
#plt.show();

"""To mitigate this issue, we employed several strategies:

Initially we used RandomOverSampler to oversample class 0 and RandomUnderSampler to undersample class 1, ultimately achieving a balanced dataset, then data was normalized with failed results. 

We addressed the class imbalance by oversampling class 0 to match the number of items in class 1, utilizing the 'resample' parameter from the sklearn.utils library. This balancing technique resulted in a dataset with equitable class distribution, which was then employed for our machine learning modeling.

At the end we chose SMOTE for resampling the dataset Train and Test sets after splitting in order to avoid leakage. The results were similar. However, resampling the dataset with SMOTE we obtained slightly better results."""


