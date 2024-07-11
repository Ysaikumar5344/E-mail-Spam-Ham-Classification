import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

st.image(r'C:\Users\Y SAI KUMAR\Music\innomatics-footer-logo.webp')
st.title("E-mail Spam or Ham Classification")
st.image(r"C:\Users\Y SAI KUMAR\Desktop\spamorhamclassification.jpg")
model=pickle.load(open(r"C:\Users\Y SAI KUMAR\New folder\nb.pkl",'rb'))
Vectorizer=pickle.load(open(r"C:\Users\Y SAI KUMAR\New folder\count_vectorizer.pkl", 'rb'))

Message=st.text_input("Enter the mail")
if Message:
    transformed_message = Vectorizer.transform([Message])
    result = model.predict(transformed_message)[0]

    if st.button("Classify"):
        st.write("Classification(SPAM/HAM) Result: This is a",result.upper(),"Mail")  
        if result=="spam":
            st.image(r"C:\Users\Y SAI KUMAR\Music\spammmm.png")
        elif result=="ham":
            st.image(r"C:\Users\Y SAI KUMAR\Music\hammmm.png")