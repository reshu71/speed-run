import requests

def get_user_status(user_id):
    # In reality, this hits a server.
    # If the internet is down, this crashes.
    response = requests.get(f"https://api.example.com/users/{user_id}")
    if response.status_code == 200:
        return "active"
    return "inactive"