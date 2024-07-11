import streamlit as st
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer

# Display the logo and title
try:
    st.image('innomatics-footer-logo.webp')
    st.title("E-mail Spam or Ham Classification")
    st.image('spamorhamclassification.jpg')

    # Load the trained model and vectorizer
    model = pickle.load(open('nb.pkl', 'rb'))
    Vectorizer = pickle.load(open('count_vectorizer.pkl', 'rb'))

    # Input text box for the email message
    Message = st.text_input("Enter the mail")

    # Button to classify the input message
    if Message and st.button("Classify"):
        transformed_message = Vectorizer.transform([Message])
        result = model.predict(transformed_message)[0]

        # Display the result
        st.write("Classification (SPAM/HAM) Result: This is a", result.upper(), "Mail")
        if result == "spam":
            st.image('spammmm.png')
        elif result == "ham":
            st.image('hammmm.png')

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.write(os.listdir('.'))  # List directory contents for debugging
