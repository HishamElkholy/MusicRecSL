import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns


"""We evaluated a range of machine learning models to predict music appreciation. Key models considered included:"""

models = st.selectbox("Please choose a model", ["-","Decision Tree Classifier", "Logistic Regression", "Classification by Decision Tree", "Classification by Random Forest", "Classification by Boosting Algorithms: AdaBoost", "Classification by Bagging Algorithm", "Gradient Boosting", "Random Forest GridSearchCV", "Deep Learning for tabular data: Dense Neural Network (DNN)"])

if models == "-":
            '''Whats up this is me'''
            """Yeah whats up"""
else:
            """No its not""""

st.title("Decision Tree Classifier")

"""The Decision Tree Classifier yielded F1 scores of 0.69 for Class 0 and 0.40 for Class 1. It achieved moderate performance but struggled to accurately predict Class 1 instances, as evidenced by the lower F1 score for Class 1."""

st.title("Logistic Regression")

"""Logistic Regression displayed robust performance with high F1 scores of 0.81 for both Class 0 and Class 1. It effectively balanced precision and recall for both classes, resulting in accurate predictions. The confusion matrix illustrates the model's ability to classify instances correctly, with a balanced distribution of true positives and true negatives."""

conf_matrix = [[111446,25273],[27378,109341]]

plt.figure(figsize=(4,3))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='OrRd', 
            xticklabels=['Predicted\n Negative', 'Predicted\n Positive'], 
            yticklabels=['Actual\n Negative', 'Actual\n Positive'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Test set')
txt="Confusion Matrix for Logistic Regression model"
plt.figtext(0.5, -0.2, txt, wrap=True, horizontalalignment='center', fontsize=6, fontstyle = 'italic');
st.pyplot(plt.gcf());

st.title("Classification by Decission Trees")

"""Classification by Decision Tree achieved F1 scores of 0.72 for both Class 0 and Class 1. While it performed better than the initial Decision Tree Classifier, it still faced challenges in accurately predicting Class 1 instances."""

conf_matrix = [[98279,38440],[38018,98701]]

plt.figure(figsize=(4,3))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='OrRd', 
            xticklabels=['Predicted\n Negative', 'Predicted\n Positive'], 
            yticklabels=['Actual\n Negative', 'Actual\n Positive'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Test set')
txt="Confusion Matrix for Decission Tree model"
plt.figtext(0.5, -0.2, txt, wrap=True, horizontalalignment='center', fontsize=6, fontstyle = 'italic');
st.pyplot(plt.gcf());

"""It was also possible to calculate the most important scores for the features of the model. It is easy to see the importance of the different time zones for the calculation of this model."""

df = pd.DataFrame([['tz_Asia & Australia',0.488828], 
['instrumentalness',0.189137],
['tz_North America', 0.172875],
['tz_Middle East',0.068357],
['tz_Asia',0.035728],
['language_Japanese', 0.028487],
['energy', 0.010705],
['speechiness', 0.004461],
['mode',0.001423],
['tz_North America & South America', 0.00000],
['tz_North America & Central America',0.000000]], 
columns = (["Features", "Importance"]))

st.table(df.set_index(df.columns[0]))

st.title("Classification by Random Forest")

"""Classification by Random Forest demonstrated significant improvement with high F1 scores of 0.90 for Class 0 and 0.91 for Class 1. It outperformed previous models and showcased remarkable accuracy in classifying both classes. The Confusion Matrix for this model is shown."""

conf_matrix = [[118089,18630],[6526,130193]]

plt.figure(figsize=(4,3))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='OrRd', 
            xticklabels=['Predicted\n Negative', 'Predicted\n Positive'], 
            yticklabels=['Actual\n Negative', 'Actual\n Positive'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Test set')
txt="Confusion Matrix for Random Forest model"
plt.figtext(0.5, -0.2, txt, wrap=True, horizontalalignment='center', fontsize=6, fontstyle = 'italic');
st.pyplot(plt.gcf());

"""Using Random Forest, the different scores for the relevant features were calculated and presented as a bar plot. Here remains the time zone of Asia & Australia as very important for the calculations. However, it is easy to observe that the “musical” scores are more valuable and relevant to the calculation of the model."""

st.title("Classification by Boosting algorithms: AdaBoost")

"""Classification by AdaBoost achieved competitive F1 scores of 0.85 for Class 0 and 0.84 for Class 1. It provided accurate predictions for both classes, although slightly lower than the Random Forest model. The Confusion Matrix for this model is shown"""

conf_matrix = [[121116,15603],[26123,110596]]

plt.figure(figsize=(4,3))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Greens_r', 
            xticklabels=['Predicted\n Negative', 'Predicted\n Positive'], 
            yticklabels=['Actual\n Negative', 'Actual\n Positive'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Test set')
txt="Confusion Matrix for Adaboost model"
plt.figtext(0.5, -0.2, txt, wrap=True, horizontalalignment='center', fontsize=6, fontstyle = 'italic');
st.pyplot(plt.gcf());

st.title("Classification by Bagging Algorithm")

"""Classification by Bagging Algorithm delivered outstanding F1 scores of 0.90 for both Class 0 and Class 1. It consistently demonstrated high accuracy and precision in classifying both music appreciation classes. The Confusion Matrix for this model is shown."""

conf_matrix = [[117974,18745],[8405,128314]]

plt.figure(figsize=(4,3))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Predicted\n Negative', 'Predicted\n Positive'], 
            yticklabels=['Actual\n Negative', 'Actual\n Positive'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Test set')
txt="Confusion Matrix for Bagging model"
plt.figtext(0.5, -0.2, txt, wrap=True, horizontalalignment='center', fontsize=6, fontstyle = 'italic');
st.pyplot(plt.gcf());

"""Again here in this model the scores of the features such as Time Zone Asia & Australia as the Instrumentalness value play an important role in the model. The relevance of the scores of the other “musical” values is very similar to the Random Forest classification."""

st.title("Gradient Boosting")

"""The Gradient Boosting model achieved F1 scores of 0.78 for Class 0 and 0.75 for Class 1. While it provided a reasonable balance between precision and recall, it performed slightly below the Random Forest and Bagging models."""

st.title("Random Forest GridSearchCV")

"""The Random Forest GridSearchCV model achieved high F1 scores of 0.90 for Class 0 and 0.91 for Class 1, similar with the Classification by Random Forest. It demonstrated consistent and robust performance. Confusion Matrix for this model is shown"""

conf_matrix = [[117955,18764],[6452,130267]]

plt.figure(figsize=(4,3))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Predicted\n Negative', 'Predicted\n Positive'], 
            yticklabels=['Actual\n Negative', 'Actual\n Positive'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Test set')
txt="Confusion Matrix for Random Forest GridSearchCV model"
plt.figtext(0.5, -0.2, txt, wrap=True, horizontalalignment='center', fontsize=6, fontstyle = 'italic');
st.pyplot(plt.gcf());

st.title("Deep Learning for tabular data: Dense Neural Network (DNN)")

"""The Deep Learning model designed for tabular data achieved respectable F1 scores of 0.88 for Class 0 and 0.89 for Class 1. While it delivered strong results, it's essential to note that it slightly trailed behind some of the traditional ML models, such as the Classification by Random Forest. The Confusion Matrix for this model is shown"""

df = pd.DataFrame([['dense (Dense)','(None, 128)',3840], 
['dense_1 (Dense)', '(None, 256)',33024],
['dense_2 (Dense)', '(None, 512)', 131584],
['dropout (Dropout)', '(None, 512)',0],
['dense_3 (Dense)', '(None, 256)', 131328],
['dense_4 (Dense)', '(None, 128)', 32896],
['dense_5 (Dense)', '(None, 2)', 258]], 
columns = (["Layer (type)", "Output Shape", "Param #"]))

st.table(df.set_index(df.columns[0]))

conf_matrix = [[114917,21802],[8554,128165]]

plt.figure(figsize=(4,3))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Predicted\n Negative', 'Predicted\n Positive'], 
            yticklabels=['Actual\n Negative', 'Actual\n Positive'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Test set')
txt="Confusion Matrix for DNN model"
plt.figtext(0.5, -0.2, txt, wrap=True, horizontalalignment='center', fontsize=6, fontstyle = 'italic');
st.pyplot(plt.gcf());

"""Among the various machine learning models evaluated, it's evident that the Deep Learning for Tabular Data model, while achieving commendable F1 scores, did not outperform some of the traditional ML models, specifically the Classification by Random Forest.

Classification by Random Forest model demonstrated the highest overall accuracy with F1 scores of 0.90 for Class 0 and 0.91 for Class 1, surpassing the Deep Learning model. It proved to be a robust and reliable choice for accurately classifying music appreciation

While the Deep Learning model showcased the potential of deep learning techniques for tabular data, it fell slightly short in achieving the same level of accuracy as the Random Forest model.
In summary, while the Deep Learning model provided competitive results, it did not surpass the performance of the Classification by Random Forest model."""
