import requests
import config
from flask import jsonify

API_URL = 'https://discord.com/api/v10/'

def get_token(code: str):
    data = {
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': config.REDIRECT_URI,
        'scope': 'identify guilds'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    print(r.json())
    r.raise_for_status()
    return r.json()['access_token']

def get_current_user(token):
    headers = { 'Authorization': f"Bearer {token}" }

    r = requests.get(f"{API_URL}users/@me", headers=headers)
    print(r.json())
    r.raise_for_status()
    return r.json()

def get_user_guilds(token: str):
    headers = { 'Authorization': f"Bearer {token}" }

    r = requests.get(f"{API_URL}users/@me/guilds", headers=headers)
    print(r.json())
    r.raise_for_status()
    return r.json()

def get_user_connections(token: str):
    headers = { 'Authorization': f"Bearer {token}" }

    r = requests.get(f"{API_URL}users/@me/connections", headers=headers)
    print(r.json())
    r.raise_for_status()
    return r.json()
