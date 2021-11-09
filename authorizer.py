import base64
import requests


class Authorizer():
    def get_bearer(self, consumer_key, consumer_secret):
        key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
        # Transform from bytes to bytes that can be printed
        b64_encoded_key = base64.b64encode(key_secret)
        # Transform from bytes back into text
        b64_encoded_key = b64_encoded_key.decode('ascii')

        base_url = 'https://api.twitter.com/'
        auth_url = '{}oauth2/token'.format(base_url)

        # Create header dictionaries
        auth_headers = {
            'Authorization': f'Basic {b64_encoded_key}',
        }

        auth_data = {
            'grant_type': 'client_credentials'
        }

        # request oauth2 tokens
        auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
        # return bearer token from response
        return auth_resp.json()['access_token']
