import json
import requests


def get_api_token():
    """ prompts user to enter a token. in practice this will probably be coming from
    an environment variable or AWS via a settings.py file """
    return input("Enter Purecloud access token: ")

def get_access_token(basic_token):
    """ POST request to API to retrieve access token """
    url = "https://login.mypurecloud.com/oauth/token?grant_type=client_credentials"
    body_data = {} # for this example we aren't sending data along in the body. in some other situations you may need to pass info along here in JSON format
    headers = {'Authorization': f'Basic {basic_token}'} # we need to send the initial token to the API to log in

    """ call API and pull the access_token out of the response """
    response = requests.request("POST", url, headers=headers, data=body_data)
    print(f"received API response: {response.json()}")
    return response.json()["access_token"]

def get_user_count(access_token):
    """ GET request to API to retrieve user data - no paging through results"""
    print("getting list of users from API")
    url = "https://api.mypurecloud.com/api/v2/users"
    body_data = {}
    headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'} # use the access token after logging in

    response = requests.request("GET", url, headers=headers, data=body_data)
    print(f"found {response.json()['total']} users in purecloud API")

def get_user_list(access_token):
    """ GET request to API to retrieve user data - uses paging"""
    choice = input("retrieve full user list from API [y/n]? ")
    if choice.lower() == 'y':
        user_list = []
        print("getting list of users from API")
        url = "https://api.mypurecloud.com/api/v2/users"
        while url:
            body_data = {}
            headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'} # use the access token after logging in

            response = requests.request("GET", url, headers=headers, data=body_data)
            response_json = response.json()
            for obj in response_json["entities"]:
                user_list.append(obj["name"])

            url = "https://api.mypurecloud.com" + response_json["nextUri"] if "nextUri" in response_json else None # use the provided 'next' page URL and continue looping until there is no 'next' page

        print(f"found {len(user_list)} user entries in purecloud API")
        list_choice = input("list all user names [y/n]? ")
        if list_choice.lower() == 'y':
            print(user_list)

def main():
    """ main program """
    basic_token = get_api_token()
    access_token = get_access_token(basic_token=basic_token)
    get_user_count(access_token=access_token)
    get_user_list(access_token=access_token)

if __name__ == "__main__":
    main()
