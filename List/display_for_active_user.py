users = {'aman':'active','bitu':'inactive','chetan':'active','dinesh':'inactive','ela':'active'}
active_users,inactive_users = {},{}
for user,status in users.items():
    if status == 'active':
        active_users[user] = status
    elif status == 'inactive':
        inactive_users[user] = status
print(f"following are the active users {active_users}")
print(f"following are the inactive users {inactive_users}")
