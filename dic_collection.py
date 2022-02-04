# Create a sample collection
users = {'Rama': 'active', 'Hanuma': 'inactive', 'Ganesh': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print("Strategy:  Iterate over a copy")
print(users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print("\nStrategy:  Create a new collection")
print(active_users)   