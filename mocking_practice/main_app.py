from database import get_user_from_db

def is_user_admin(user_id):
    try:
        # This call is what we need to MOCK.
        # If we run this real function, our test takes 5 seconds.
        user = get_user_from_db(user_id)
        
        if user and user['username'] == 'admin':
            return True
        return False
    except ConnectionError:
        # We want to test this line too!
        return "System Down"