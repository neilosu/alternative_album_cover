from flask import Flask, jsonify, send_file
from internal_spotify import *

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message='Hello, World!')

@app.route('/search_album/<album_name>')
def api_search_album(album_name):
    album_search_info = search_album(album_name)
    search_album_names = []
    for album in album_search_info['albums']['items']:
        search_album_names.append({"album_name": album['name'], "album_id": album['id']})
    return jsonify(search_album_names)
    # return jsonify(message=f'Search results are: {search_als

@app.route('/get_album_cover_image/<album_id>')
def api_get_album_cover_image(album_id):
    album_info = get_album_info(album_id)
    album_image = get_album_cover_image(album_info, file_save_path = "album_cover.jpg")
    return send_file(album_image, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()