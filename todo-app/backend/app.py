from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = []

@app.route('/todos', methods=['GET', 'POST'])
def handle_task_requests():
    if request.method == 'POST':
        new_todo = request.json
        todos.append(new_todo)
        return jsonify(todos), 201
    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)