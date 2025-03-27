from flask import Flask, jsonify
from classes import *

app = Flask(__name__)

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    produtos_json = [produto.to_dict() for produto in produtos]
    return jsonify(produtos_json)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')