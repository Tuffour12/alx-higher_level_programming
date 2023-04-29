import requests
import sys
import base64

if __name__ == "__main__":
    # Get username and token from command line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # Create authentication string using Base64 encoding
    auth_str = f"{username}:{token}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    # Set request headers with Basic Authentication
    headers = {"Authorization": f"Basic {b64_auth_str}"}

    # Send GET request to GitHub API
    response = requests.get("https://api.github.com/user", headers=headers)

    # If request is successful, print user id
    if response.status_code == 200:
        user_id = response.json()["id"]
        print(user_id)
    # If request is unsuccessful, print error message
    else:
        print(f"Error: {response.status_code}")

