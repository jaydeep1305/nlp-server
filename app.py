


import os
from flask import Flask, request, jsonify
from google.cloud import language_v1

app = Flask(__name__)

# Create a client for the Google Cloud NLP API
client = language_v1.LanguageServiceClient()

@app.route('/entities', methods=['POST'])
def analyze_entities():
    """Analyze entities in the provided text"""
    try:
        # Get the text from the incoming JSON payload
        data = request.get_json()
        text = data.get('text')

        if not text:
            return jsonify({'error': 'Missing required field "text"'}), 400

        # Construct a document
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

        # Call the Google Cloud NLP API for entity analysis
        response = client.analyze_entities(document=document)

        # Prepare the result
        entities = []
        for entity in response.entities:
            entities.append({
                'name': entity.name,
                'type': language_v1.Entity.Type(entity.type_).name,
                'salience': entity.salience,
                'metadata': dict(entity.metadata) if entity.metadata else {}  # Convert metadata to a dictionary
            })

        return jsonify({'entities': entities})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    """Analyze the sentiment of the provided text"""
    try:
        # Get the text from the incoming JSON payload
        data = request.get_json()
        text = data.get('text')

        if not text:
            return jsonify({'error': 'Missing required field "text"'}), 400

        # Construct the document
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

        # Call Google NLP API for sentiment analysis
        sentiment = client.analyze_sentiment(request={"document": document}).document_sentiment

        sentiments = {"score": sentiment.score, "magnitude": sentiment.magnitude}
        return jsonify({'sentiments': sentiments})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/categories', methods=['POST'])
def analyze_categories():
    """Analyze the categories of the provided text"""
    try:
        # Get the text from the incoming JSON payload
        data = request.get_json()
        text = data.get('text')

        if not text:
            return jsonify({'error': 'Missing required field "text"'}), 400

        # Construct the document
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

        # Call the Google Cloud NLP API for category classification
        category_response = client.classify_text(document=document)

        categories = []
        for category in category_response.categories:
            categories.append({
                'name': category.name,
                'confidence': category.confidence
            })

        return jsonify({'categories': categories})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

