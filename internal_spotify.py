import requests
import json
import base64

CLIENT_ID = ""
CLIENT_SECRET = ""
ALBUM_NAME = "Global Warming"
ALBUM_COVER_IMAGE_DEFAULT_PATH = "album_cover.jpg"
ARTIST_IMAGE_DEFAULT_PATH = "artist_image.jpg"

def get_access_token(client_id = CLIENT_ID, client_secret = CLIENT_SECRET):    
    encoded = base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + encoded
    }
    payload = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers)
    json_string = response.text
    dict_response = json.loads(json_string)
    access_token = dict_response['access_token']
    # print("access_token: " + access_token)
    return access_token

def get_album_info(album_id):
    response = requests.get("https://api.spotify.com/v1/albums/" + album_id, headers={"Authorization": "Bearer " + get_access_token()})
    json_string = response.text
    dict_response = json.loads(json_string)
    return dict_response

def save_album_cover_image(album_info, file_save_path = ALBUM_COVER_IMAGE_DEFAULT_PATH):
    print("Saving album cover image to: " + file_save_path)
    album_cover_image_url = album_info['images'][0]['url']
    album_cover_image = requests.get(album_cover_image_url).content
    with open(file_save_path, 'wb') as file:
        file.write(album_cover_image)

def get_album_artist(album_info):
    artist_id = album_info['artists'][0]['id']
    artist_name = album_info['artists'][0]['name']
    return artist_id, artist_name

def get_artist_info(artist_id):
    response = requests.get("https://api.spotify.com/v1/artists/" + artist_id, headers={"Authorization": "Bearer " + get_access_token()})
    json_string = response.text
    dict_response = json.loads(json_string)
    return dict_response

def save_artist_image(artist_info, file_save_path = ARTIST_IMAGE_DEFAULT_PATH):
    print("Saving artist image to: " + file_save_path)
    artist_image_url = artist_info['images'][0]['url']
    artist_image = requests.get(artist_image_url).content
    with open(file_save_path, 'wb') as file:
        file.write(artist_image)

def search_album(album_name, result_limit = 5):
    print("Searching for album: " + album_name)
    response = requests.get("https://api.spotify.com/v1/search?q=" + album_name + f"&type=album&limit={result_limit}", headers={"Authorization": "Bearer " + get_access_token()})
    json_string = response.text
    dict_response = json.loads(json_string)
    print("Search result album names are:")
    for album in dict_response['albums']['items']:
        print(" " + album['name'])
    return dict_response

def get_album_id(album_search_info, desired_item = 0):
    print(f"Getting album id for the {desired_item}th item: {album_search_info['albums']['items'][desired_item]['name']} in the search result.")
    album_id = album_search_info['albums']['items'][desired_item]['id']
    return album_id

if __name__ == '__main__':
    album_name = ALBUM_NAME
    album_search_info = search_album(album_name)
    album_id = get_album_id(album_search_info)
    album_info = get_album_info(album_id)
    save_album_cover_image(album_info)
    artist_id, artist_name = get_album_artist(album_info)
    artist_info = get_artist_info(artist_id)
    save_artist_image(artist_info)
