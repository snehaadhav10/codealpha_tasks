# FAQ Chatbot

A simple chatbot to answer FAQs using NLP and cosine similarity.

## How it works
- FAQs are preprocessed using NLTK
- TF-IDF vectorization and cosine similarity match the user's question
- The best-matching answer is displayed

## Run Locally

```bash
pip install -r requirements.txt
streamlit run chatbot_ui.py
```
