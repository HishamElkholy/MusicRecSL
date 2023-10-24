import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

st.title("SHAP Analysis")

"""The SHAP (SHapley Additive exPlanations) technique significantly enhanced our understanding of feature importance and interactions. After calculation, it is expected to visualize how the different features of the model contributed to the results either increasing or decreasing the predictions. However, it is relevant to know that SHAP have some limitations such as Feature Dependencies. Values of one feature are dependent on the values of another feature. In addition, independence of features is assumed which is not always true and can lead to unrealistic predictions. SHAP also calculates how a model feature is important regarding a prediction which has not to be confused with the importance of the feature to the actual target variable. In other words, SHAP may represent how a model feature is important for the model, but the model is simply a model, a representation. Conclusions apply only for the model and sometimes can not be extended to real life."""

"""From the three SHAP plots we can conclude for the given model that:"""

"""- Among the content features, "language English” and “tz_North America & South America”' stand out as the most crucial contributor to music appreciation predictions when observing the plot of the absolute mean SHAP values.The figure displays the features which made a significant contribution to the model predictions.It is important to note that the majority of entries are for the English language and for the North America & South America time zone. This may lead to the importance of these features for the calculation of the model."""

st.image("SHAP1.png", caption = "Bar plot using the SHAP values for a specific instance. Absolute mean contribution of the features")

"""- Languages, time zones and musical features: The SHAP Values of the Waterfall plot in Figure 21 describe how every model feature contributes to the difference between the prediction f(x) = 1.389 and the average prediction E[f(x] = -1.039. Besides this number it is important to state that the red values (positive) describe a higher probability to predict a positive sentiment score whereas the blue values (negative) increase the probability to predict a negative sentiment score."""

st.image("SHAP2.png", caption = "Waterfall plot using the SHAP values for a specific instance")

"""The time zone Europe contributes positively, increasing the value towards f(x) 1.389 as well as the "language_English”' feature. In other words songs in English allow more positive predictions. In contrast, the "language_Japanese'' feature has a slightly negative impact on predictions, suggesting that songs with certain languages tend to be associated with lower appreciation levels in the dataset (at least for this model). Instrumentalness is a musical feature which also contributes positively is the most salient musical feature. The former assumptions are based on the model and it is important to stress that this (language and time zone) may be a proxy variable. It works for the model but by no means can be extended to real life. However, it is possible to expect that some cultural factors(regarding the time zones) and language of the lyrics (associated with emotional reaction to the language of the song) might not resonate well compared with the English language and influence the outcomes of the model."""

"""- Features related to time zones such as "tz_Asia & Australia," "tz_North America & South America," and "tz_Europe'' rank among the most important. However, they contribute sometimes negatively to predictions. As stated before, this could explain the model but the variables related with time zones and languages are probably proxy variables. It means these explain the models but are not the real life features that explain why the target variable produces a specific result. The last figure presents the same information as Figure 20 additionally displaying the negative contributions of the most important features."""

st.image("SHAP3.png", caption = "Beeswarm plot using the SHAP values for a specific instance")

"""The modeling results highlight the importance of considering the language and time zone preferences of the target audience. By understanding the impact of different languages and time zones on music appreciation, businesses can tailor their content which better suit the preferences and cultural background of their audience."""
