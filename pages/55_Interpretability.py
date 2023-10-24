import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

st.title("SHAP Analysis")

#""" The SHAP (SHapley Additive exPlanations) technique significantly enhanced our understanding of feature importance and interactions. After calculation, it is expected to visualize how the different features of the model contributed to the results either increasing or decreasing the predictions. However, it is relevant to know that SHAP have some limitations such as Feature Dependencies. Values of one feature are dependent on the values of another feature. In addition, independence of features is assumed which is not always true and can lead to unrealistic predictions. SHAP also calculates how a model feature is important regarding a prediction which has not to be confused with the importance of the feature to the actual target variable. In other words, SHAP may represent how a model feature is important for the model, but the model is simply a “model” a representation. Conclusions apply only for the model and sometimes can not be extended to “real life”."""
