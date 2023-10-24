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

