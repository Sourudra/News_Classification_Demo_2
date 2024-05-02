import streamlit as st
import joblib
from newspaper import Article

# Loading the trained model
model = joblib.load("news-classification-model-2.pkl")

# Defining sentiment labels
news_labels = {0: 'tech', 1: 'business', 2: 'sport', 3: 'entertainment', 4: 'politics'}


# Creating Streamlit app
st.title("News Classification")

# Input selection: text area or URL
input_option = st.radio("Select Input Option:", ('Paste News Article', 'Enter URL Of News Article'))

# Function to classify news
def classify_news(text):
    predicted_label = model.predict([text])[0]
    predicted_news_label = news_labels[predicted_label]
    return predicted_news_label

# Function to fetch text from URL
def fetch_text_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

if input_option == 'Paste News Article':
    # Input text area
    user_input = st.text_area('Enter news here')

    # Prediction button
    if st.button("Classify"):
        if user_input.strip() != "":
            predicted_news_label = classify_news(user_input)
            # Display classification
            st.info(f"Predicted News Category: {predicted_news_label}")
        else:
            st.error("Please enter some news article text.")
else:
    # Input URL
    url_input = st.text_input("Enter The URL of the News Article:")

    # Prediction button
    if st.button("Classify"):
        if url_input.strip() != "":
            try:
                text_from_url = fetch_text_from_url(url_input)
                predicted_news_label = classify_news(text_from_url)
                # Display classification
                st.info(f"Predicted News Category: {predicted_news_label}")
            except Exception as e:
                st.error(f"Error occurred: {e}")
        else:
            st.error("Please enter a valid URL.")

