import json, os
from flask import Flask
from flask import request, make_response, jsonify
from hooks import data

app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

#https://pbs.twimg.com/profile_images/1162951608956624896/Ou-2MSNs_400x400.jpg
#tes

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/profile', methods=['GET'])
def profile():
    error_params = {"meta": { "http_status": 401}, "message": "parameter must required"}
    error_apikey = {"meta": { "http_status": 401},
                "status_message": "Invalid API key: You must be granted a valid key."}
    # yXgXZGnGr4Pzk8U7GAMjHsBadDhKnS
    try:
        id_user = request.args.get('id')
        apikey = request.args.get('key')

        if not apikey:
            return make_response(jsonify(error_apikey)), 401


        if not id_user:
            return make_response(jsonify(error_params)), 401
        
        if apikey == 'yXgXZGnGr4Pzk8U7GAMjHsBadDhKnS':

            limited = [k for k in data if k['user_id'] == id_user]

            username_at = '@'+limited[0]['user_screen_name']
            link_profil = limited[0]['user_profile_image_url_https']
            link_profil = link_profil[:-10] + '400x400.jpg'

            result = {
                'id': limited[0]['user_id'],
                'user_name': limited[0]['user_name'],
                'username_at': username_at,
                'total_posting': limited[0]['user_statuses_count'],
                'status_post': limited[0]['full_text'],
                'profile_image': link_profil,
                'likes': limited[0]['favorite_count'],
                'follower': limited[0]['user_followers_count'],
                'following': limited[0]['user_following_count']
            }

            return make_response(jsonify(result))
        else:
            return make_response(jsonify(error_apikey)), 401

        
    except Exception as e:
        return make_response(jsonify([]))

@app.route('/post', methods=['GET'])
def postingan():

    error_params = {"meta": { "http_status": 401}, "message": "parameter must required"}
    error_apikey = {"meta": { "http_status": 401},
                "status_message": "Invalid API key: You must be granted a valid key."}
    # yXgXZGnGr4Pzk8U7GAMjHsBadDhKnS
    try:
        pages = request.args.get('page')
        apikey = request.args.get('key')

        if not apikey:
            return make_response(jsonify(error_apikey)), 401


        if not pages:
            return make_response(jsonify(error_params)), 401
        
        if apikey == 'yXgXZGnGr4Pzk8U7GAMjHsBadDhKnS':
            index = int(pages)

            username_at = '@'+data[1]['user_screen_name']

            link_profil = data[index]['user_profile_image_url_https']
            link_profil = link_profil[:-10] + '400x400.jpg'
            
            
            result = {
                'id': data[index]['user_id'],
                'user_name': data[index]['user_name'],
                'username_at': username_at,
                'status_post': data[index]['full_text'],
                'profile_image': link_profil,
                'likes': data[index]['favorite_count']
            }

            return make_response(jsonify(result))
        else:
            return make_response(jsonify(error_apikey)), 401

        
    except Exception as e:
        return make_response(jsonify([]))


@app.errorhandler(404)
def error404(e):
    return make_response('Halaman belum tersedia hehe')



