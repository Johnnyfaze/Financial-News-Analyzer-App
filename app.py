# create flask app
from flask import Flask, request, jsonify, render_template
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# create the app
app = Flask(__name__)

# load the model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# define routes
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# predict route
@app.route('/predict', methods=['POST'])
def predict():
    news_text = request.form['news']
    news_vector = vectorizer.transform([news_text])
    prediction = model.predict(news_vector)
    sentiment_map = {2: 'positive', 1: 'negative', 0: 'neutral'}
    sentiment = sentiment_map[prediction[0]]
    return jsonify({'news': news_text, 'sentiment': sentiment})

# run the app
if __name__== '__main__':
    app.run(debug=True)