import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

st.image(r'innomatics-footer-logo.webp')
st.title("E-mail Spam or Ham Classification")
st.image(r"spamorhamclassification.jpg")
model=pickle.load(open(r"nb.pkl",'rb'))
Vectorizer=pickle.load(open(r'count_vectorizer.pkl', 'rb'))

Message=st.text_input("Enter the mail")
if Message:
    transformed_message = Vectorizer.transform([Message])
    result = model.predict(transformed_message)[0]

    if st.button("Classify"):
        st.write("Classification(SPAM/HAM) Result: This is a",result.upper(),"Mail")  
        if result=="spam":
            st.image(r"spammmm.png")
        elif result=="ham":
            st.image(r"hammmm.png")
