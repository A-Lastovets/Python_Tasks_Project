def create_user(username, email, password, **kwargs):
    if len(username) < 5:
        return "Error: Username must be at least 5 characters, email must contain '@', and password must be at least 8 characters long."
    
    if '@' not in email:
        return "Error: Username must be at least 5 characters, email must contain '@', and password must be at least 8 characters long."
    
    if len(password) < 8:
        return "Error: Username must be at least 5 characters, email must contain '@', and password must be at least 8 characters long."
    
    user_details = {
        'username': username,
        'email': email,
        'password': password
    }
    
    user_details.update(kwargs)
    
    return user_details

user1 = create_user('john123', 'john@example.com', 'securePass123', age=30)
user2 = create_user('jane', 'jane@example.com', 'short', age=25, address="123 Street")
user3 = create_user('alice123', 'alice@example', 'password123')

print(user1)
print(user2)
print(user3)
