from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

from process import save_document_ocr,save_pgdocument
from metrics import mesure_tag,metriche
app = Flask(__name__)
CORS(app)

# Database connections
postgres_conn = psycopg2.connect(
    dbname="semantic_search",
    user="postgres",
    password="postgres",
    host="db"
)
mongo_client = MongoClient("mongodb://mongo:27017/")
mongo_db = mongo_client.semantic_search

# Load the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/api/documents/upload', methods=['POST'])
def upload_document():
    # Placeholder for document upload logic
    t1 = time
    save_pgdocument()
    save_document_ocr()
    t2 = time

    mesure_tag('t_save_doc',(t2-t1))

    return jsonify({"status": "success"}), 200

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    # Placeholder for search logic
    return jsonify({"results": []}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
