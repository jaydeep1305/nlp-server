# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = "Hello, world!"
document = language_v1.types.Document(
    content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment


# Construct a document
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Call the Google Cloud NLP API for entity analysis
response = client.analyze_entities(document=document)

print("entites anaylsis :- ",response)
print(f"Text: {text}")
print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")




# import os
# from flask import Flask, request, jsonify
# from google.cloud import language_v1
# from flasgger import Swagger, swag_from

# app = Flask(__name__)
# swagger = Swagger(app)

# client = language_v1.LanguageServiceClient()

# # Define the schema for text input payload
# class TextInputSchema:
#     """Define the structure of the request body for the text parameter"""
#     def __init__(self, text):
#         self.text = text

# @app.route('/entities', methods=['POST'])
# @swag_from({
#     'parameters': [
#         {
#             'name': 'text',
#             'in': 'body',
#             'required': True,
#             'type': 'string',
#             'description': 'Text to be analyzed for entities.',
#             'schema': {
#                 'type': 'object',
#                 'properties': {
#                     'text': {
#                         'type': 'string',
#                         'description': 'Text to analyze for entities.'
#                     }
#                 },
#                 'required': ['text']
#             }
#         }
#     ],
#     'responses': {
#         200: {
#             'description': 'Entities analysis results',
#             'schema': {
#                 'type': 'object',
#                 'properties': {
#                     'entities': {
#                         'type': 'array',
#                         'items': {
#                             'type': 'object',
#                             'properties': {
#                                 'name': {'type': 'string'},
#                                 'type': {'type': 'string'},
#                                 'salience': {'type': 'number'},
#                                 'metadata': {'type': 'object'}
#                             }
#                         }
#                     }
#                 }
#             }
#         },
#         400: {
#             'description': 'No text provided in the request body'
#         },
#         500: {
#             'description': 'Internal server error'
#         }
#     }
# })
# def analyze_entities():
#     """
#     Analyze entities in the provided text.
#     This endpoint will take a text input and return the detected entities, 
#     their types, salience, and metadata.
#     """
#     try:
#         text = request.json.get('text', '')

#         # Check if the input text is empty
#         if not text:
#             return jsonify({'error': 'No text provided'}), 400

#         # Construct a document
#         document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

#         # Call the Google Cloud NLP API for entity analysis
#         response = client.analyze_entities(document=document)

#         # Prepare the result
#         entities = []
#         for entity in response.entities:
#             entities.append({
#                 'name': entity.name,
#                 'type': language_v1.Entity.Type(entity.type_).name,
#                 'salience': entity.salience,
#                 'metadata': dict(entity.metadata) if entity.metadata else {}  # Convert metadata to a dictionary
#             })

#         return jsonify({'entities': entities})

#     except Exception as e:
#         return jsonify({'errors': str(e)}), 500


# @app.route('/sentiment', methods=['POST'])
# @swag_from({
#     'parameters': [
#         {
#             'name': 'text',
#             'in': 'body',
#             'required': True,
#             'type': 'string',
#             'description': 'Text to be analyzed for sentiment.',
#             'schema': {
#                 'type': 'object',
#                 'properties': {
#                     'text': {
#                         'type': 'string',
#                         'description': 'Text to analyze for sentiment.'
#                     }
#                 },
#                 'required': ['text']
#             }
#         }
#     ],
#     'responses': {
#         200: {
#             'description': 'Sentiment analysis results',
#             'schema': {
#                 'type': 'object',
#                 'properties': {
#                     'sentiments': {
#                         'type': 'object',
#                         'properties': {
#                             'score': {'type': 'number'},
#                             'magnitude': {'type': 'number'}
#                         }
#                     }
#                 }
#             }
#         },
#         400: {
#             'description': 'No text provided in the request body'
#         },
#         500: {
#             'description': 'Internal server error'
#         }
#     }
# })
# def analyze_sentiments():
#     """
#     Analyze sentiment in the provided text.
#     This endpoint will take a text input and return the sentiment score and magnitude.
#     """
#     try:
#         text = request.json.get('text', '')

#         if not text:
#             return jsonify({'error': 'No text provided'}), 400
        
#         document = language_v1.types.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        
#         # Detects the sentiment of the text
#         sentiment = client.analyze_sentiment(
#             request={"document": document}
#         ).document_sentiment

#         sentiments = {"score": sentiment.score, "magnitude": sentiment.magnitude}
#         return jsonify({'sentiments': sentiments})

#     except Exception as e:
#         return jsonify({'errors': str(e)}), 500


# @app.route('/categories', methods=['POST'])
# @swag_from({
#     'parameters': [
#         {
#             'name': 'text',
#             'in': 'body',
#             'required': True,
#             'type': 'string',
#             'description': 'Text to be classified into categories.',
#             'schema': {
#                 'type': 'object',
#                 'properties': {
#                     'text': {
#                         'type': 'string',
#                         'description': 'Text to classify into categories.'
#                     }
#                 },
#                 'required': ['text']
#             }
#         }
#     ],
#     'responses': {
#         200: {
#             'description': 'Category classification results',
#             'schema': {
#                 'type': 'object',
#                 'properties': {
#                     'categories': {
#                         'type': 'array',
#                         'items': {
#                             'type': 'object',
#                             'properties': {
#                                 'name': {'type': 'string'},
#                                 'confidence': {'type': 'number'}
#                             }
#                         }
#                     }
#                 }
#             }
#         },
#         400: {
#             'description': 'No text provided in the request body'
#         },
#         500: {
#             'description': 'Internal server error'
#         }
#     }
# })
# def analyze_categories():
#     """
#     Classify text into categories.
#     This endpoint will take a text input and return the detected categories 
#     along with the confidence level.
#     """
#     try:
#         text = request.json.get('text', '')

#         if not text:
#             return jsonify({'error': 'No text provided'}), 400
        
#         document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

#         # Call the Google Cloud NLP API for category classification
#         category_response = client.classify_text(document=document)

#         categories = []
#         for category in category_response.categories:
#             categories.append({
#                 'name': category.name,
#                 'confidence': category.confidence
#             })

#         return jsonify({'categories': categories})

#     except Exception as e:
#         return jsonify({'errors': str(e)}), 500


# if __name__ == '__main__':
#     app.run(debug=True)