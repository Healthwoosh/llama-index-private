from flask import Flask, request, jsonify
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

app = Flask('app')

documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

@app.route('/query', methods=['GET'])
def query_index():
    query = request.args.get('q')
    if query:
        response = index.query(query)
        return jsonify(response)
    else:
        return jsonify({'error': 'No query parameter provided'}), 400

if __name__ == "__main__":
    app.run()

