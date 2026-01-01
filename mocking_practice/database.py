import time

def get_user_from_db(user_id):
    print(f"Connecting to heavy database for user {user_id}...")
    # Simulate a slow network call
    time.sleep(5) 
    
    if user_id == 1:
        return {"id": 1, "username": "admin", "active": True}
    elif user_id == 99:
        raise ConnectionError("Database Connection Failed!")
        
    return None