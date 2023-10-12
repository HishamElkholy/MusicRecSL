import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

"""The original main task was: “Predict whether a piece of music will be more or less appreciated based on Twitter analyzes and feedback.” The presented model predicts with an overall higher accuracy the appreciation of different musical pieces based on the target score (sentiment_score). Some of the relevant conclusions after exploration and modeling of the database are the following:"""

st.header("Scientific Conclusions")

st.subheader("Significance of the Study")

"""This study explored the predictive capabilities of various machine learning and deep learning models in the context of music appreciation. It demonstrated that machine learning models, particularly the Random Forest model, can effectively predict music appreciation based on diverse features."""

st.subheader("Feature Importance")

"""SHAP analysis revealed critical features influencing music appreciation, such as language preferences, and time zones. Understanding these factors can enhance our grasp of music consumer behavior."""

st.subheader("Deep Learning Potential")

"""While traditional machine learning models performed exceptionally well, the Deep Learning for Tabular Data model showcased the potential of deep learning techniques in tabular data analysis, providing a competitive alternative for predictive tasks. The model was further improved from the beginning, the chosen model was the best compromise between accuracy and calculation time."""

st.header("Business Conclusions")

st.subheader("Recommendation Systems")

"""The insights gained from this study can be leveraged to improve recommendation systems on music streaming platforms. Tailoring music recommendations based on user preferences, language, and geographical factors can enhance the user experience and engagement."""

st.subheader("Content Curation")

"""The findings from this study can inform content curation strategies. By considering factors such as musical features (especially instrumentalness, mode and key), language (especially english), and time zones (North & South America and Europa), streaming platforms can tailor their content to better match user preferences and cultural contexts."""

st.subheader("Globalization Strategies")

"""Understanding the impact of language and time zones on music appreciation allows for better market penetration on a global scale. Music platforms can adapt their offerings to cater to diverse audiences worldwide."""

st.header("Overall Conclusion")

"""This research delved into the intricate world of music appreciation prediction using advanced machine learning and deep learning techniques. The study not only demonstrated the efficacy of these models but also shed light on the critical factors that influence music appreciation.
The decision to undertake this subject was driven by the growing importance of understanding consumer preferences in the music industry, which has witnessed radical transformation due to digitization and globalization. The research aimed to bridge the gap between technology and music, providing valuable insights for businesses and music enthusiasts alike.

While the results are promising and interesting, there is always room for improvement. Given more computing power, we could have explored even more complex deep learning architectures and performed extensive hyperparameter tuning. This could potentially yield even better predictive performance."""