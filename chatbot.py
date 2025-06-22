import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

faqs = {
    "What is the delivery time?": "The average delivery time is 30-45 minutes.",
    "How can I cancel my order?": "You can cancel your order from the 'My Orders' section before it is dispatched.",
    "What payment methods are accepted?": "We accept credit/debit cards, UPI, and net banking.",
    "How to contact customer support?": "You can reach us via the Help section in the app or call our hotline.",
    "Is contactless delivery available?": "Yes, we provide contactless delivery for your safety."
}

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return " ".join(tokens)

processed_questions = [preprocess(q) for q in faqs.keys()]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_questions)

def get_response(user_question):
    user_question_clean = preprocess(user_question)
    user_vec = vectorizer.transform([user_question_clean])
    similarities = cosine_similarity(user_vec, X)
    max_sim_index = similarities.argmax()
    if similarities[0, max_sim_index] < 0.3:
        return "Sorry, I couldn't find a relevant answer."
    matched_question = list(faqs.keys())[max_sim_index]
    return faqs[matched_question]
