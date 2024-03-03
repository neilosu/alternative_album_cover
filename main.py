from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message='Hello, World!')

@app.route('/search_album/<album_name>')
def search_album(album_name):
    return jsonify(message=f'Searching for album: {album_name}...')

if __name__ == '__main__':
    app.run()