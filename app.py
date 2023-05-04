import streamlit as st
from transformers import pipeline

# Define the summarization pipeline
hub_model_id = "VinayakMane47/mt5-small-finetuned-amazon-en-es"
summarizer = pipeline("summarization", model=hub_model_id)

# Create the Streamlit app
def main():
    st.title("Text Summarizer")
    text = st.text_area("Enter some text to summarize")
    if st.button("Summarize"):
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
        st.write(summary)

if __name__ == "__main__":
    main()
