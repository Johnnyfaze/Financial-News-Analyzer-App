# create flask app
from flask import Flask, request, jsonify, render_template
import joblib
import os

# create the app
app = Flask(__name__)

# Get the absolute path to the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')

# load the model and vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# define routes
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Use .get() for safer access to form data and add validation
    news_text = request.form.get('news')
    if not news_text or not news_text.strip():
        return jsonify({'error': 'No news text provided or text is empty'}), 400

    news_vector = vectorizer.transform([news_text])
    prediction = model.predict(news_vector)
    sentiment_map = {2: 'positive', 1: 'negative', 0: 'neutral'}
    # Use .get() for safer dictionary access in case of an unexpected prediction
    sentiment = sentiment_map.get(prediction[0], 'unknown')
    return jsonify({'news': news_text, 'sentiment': sentiment})

# run the app
if __name__== '__main__':
    app.run(debug=True)
