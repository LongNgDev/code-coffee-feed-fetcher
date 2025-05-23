from flask import Flask, request, jsonify



app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Sempai! Flask bot server is running~ (๑˃ᴗ˂)ﻭ'

@app.route('/fetch', methods=['GET'])
def fetch():
    data = request.get_json()
    sources = data.get('sources')
    
    # Here you would call your news fetching logic
    # For demonstration, we'll just echo the sources back
    response = {
        'message': 'Fetched articles from sources',
        'sources': sources
    }
    
    return jsonify(response)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    
    # Here you would call your AI model to generate a response
    # For demonstration, we'll just echo the prompt back
    response = {
        'response': f'Generated response for: {prompt}'
    }
    
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)