from flask import Flask, render_template, jsonify
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

reaction_count = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/react', methods=['POST'])
def react():
    global reaction_count
    reaction_count += 1
    return ('', 204)

@app.route('/reaction-count')
def reaction_count_route():
    return jsonify({'count': reaction_count})

if __name__ == "__main__":
    app.run(debug=True)

