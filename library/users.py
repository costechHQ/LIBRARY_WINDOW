users = {
    "chief": {
        "password": "chief123",
        "position": "chief_librarian",
        "failed_attempts": 0,
        "locked": False
    },
    "member": {
        "password": "member123",
        "position": "member",
        "failed_attempts": 0,
        "locked": False
    }
}

def authenticate(username, password):
    """this function validates login"""

    user = users.get(username)

    if user is None:
        return None

    if user["locked"]:
        return None

    if user["password"] != password:
        user["failed_attempts"] += 1

        if user["failed_attempts"] >= 3:
            user["locked"] = True

            return None
              
    user["failed_attempts"] = 0

    return user

def is_chief_librarian(user):
    """this handles authorization"""
    return user ["position"] == "chief_librarian"