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
        search_album_names.append({"album_name": album['name'], "album_id": album['id'], "album_artist": album['artists']})
    return jsonify(search_album_names)
    # return jsonify(message=f'Search results are: {search_als

@app.route('/get_album_cover_image/<album_id>')
def api_get_album_cover_image(album_id):
    album_info = get_album_info(album_id)
    save_album_cover_image(album_info)
    return send_file(ALBUM_COVER_IMAGE_DEFAULT_PATH, mimetype='image/jpeg')

@app.route('/get_album_artist_image/<album_id>')
def api_get_album_artist_image(album_id):
    album_info = get_album_info(album_id)
    artist_id, artist_name = get_album_artist(album_info)
    artist_info = get_artist_info(artist_id)
    save_artist_image(artist_info)
    return send_file(ARTIST_IMAGE_DEFAULT_PATH, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)