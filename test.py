import requests
import json

def test_search_album():
    album_name = "Dangerous"
    response = requests.get("http://127.0.0.1:5000/search_album/" + album_name)
    dict_response = json.loads(response.text)
    print(dict_response)
    return dict_response

def test_get_album_cover_image(album_id):
    response = requests.get("http://127.0.0.1:5000/get_album_cover_image/" + album_id)
    with open("test_album_cover_image.jpg", 'wb') as file:
        file.write(response.content)

def test_get_album_artist_image(album_id):
    response = requests.get("http://127.0.0.1:5000/get_album_artist_image/" + album_id)
    with open("test_album_artist_image.jpg", 'wb') as file:
        file.write(response.content)

if __name__ == '__main__':
    album_names_info = test_search_album()
    test_get_album_cover_image(album_names_info[0]['album_id'])
    test_get_album_artist_image(album_names_info[0]['album_id'])

