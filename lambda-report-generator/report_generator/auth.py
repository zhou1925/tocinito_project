import json
import time
from requests import get, post
from requests.exceptions import ConnectionError

#endpoint = "https://tocinitov1.herokuapp.com/api/v1"
endpoint = "https://tocinpe.onrender.com/api/v1"


def get_token():
    """ 
    Hit the endpoint with credentials
    and return the access token
    retry if we get ConnectionError
    """
    username = "zhou"
    password = "produccion15"
    payload = {"username": username, "password":password}
    
    access_token = ""
    success = False
    while success is False:
        try:
            r = post(endpoint + "/token/", payload)
            if r.status_code == 200:
                success = True
                access_token = r.json()['access']
        except ConnectionError as e:
            time.sleep(10)

    return access_token
