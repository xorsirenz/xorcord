def setup():
    try:
        with open('config.py', 'r') as file:
            file.close()
    except FileNotFoundError:
        print('no config file found')
        user_token = input('Enter discord token:\n > ')
        callback_channel = input('Enter private discord channel id:\n > ')
        with open('config.py', 'a') as file:
            file.write(f"from urllib import parse\nAPI_URL = 'https://discord.com/api/v10/channels/'\nTOKEN = '{user_token}'\nCALLBACK_CHANNEL = '{callback_channel}'")
            file.close()
        with open('raiders.txt', 'a') as f:
            f.write(user_token)
            f.close()
