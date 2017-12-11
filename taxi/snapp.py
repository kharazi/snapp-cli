import os.path
import shelve
import requests
import pprint


pp = pprint.PrettyPrinter(indent=4)
c_path = os.path.expanduser("~") + '/.config/snapp-cli/cook'
db = shelve.open(c_path)
session = requests.session()

cook, token = None, None


if 'cook' in db.keys():
    cook = db['cook']

if 'token' in db.keys():
    token = db['token']


def save_session(session, token):
    db['cook'] = requests.utils.dict_from_cookiejar(session.cookies)
    db['token'] = token
    db.sync()


def price(origin_lat, origin_lng, destination_lat, destination_lng, rount_trip=0, waiting=0):
    data = {
        'origin_lat': origin_lat,
        'origin_lng': origin_lng,
        'destination_lat': destination_lat,
        'destination_lng': destination_lng,
        'round_trip': rount_trip,
        'waiting': waiting
    }

    headers = {
        'Authorization': token
    }

    r = session.post(
        'https://web-api.snapp.ir/api/v1/ride/price',
        json=data,
        cookies=cook,
        headers=headers)
    
    if r.status_code >= 200 or r.status_code < 300:
        res = r.json()['prices']
        return [
            [
                s['service']['name'],
                s['final'],
                s['distance'],
            ] for s in res
        ]
    else:
        return False


def login(username, password):
    data = {
        'username': username,
        'password': password
    }
    r = session.post(
        'https://web-api.snapp.ir/api/v1/auth/login',
        json=data,
        cookies=cook
    )
    if r.status_code >= 200 or r.status_code < 300:
        save_session(session, token=r.json()['token'])
        return True
    else:
        return False
