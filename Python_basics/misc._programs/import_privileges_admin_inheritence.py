from privileges_admin_inheritence import (User, Privileges,Admin)
admin1 = Admin("Vikas","Singh")
admin1.emailID = "Vikas.singh@gmail.com"
admin1.greet_user
admin1.describe_user
print(f"The privilages given to {admin1.first_name} {admin1.last_name} are {admin1.privileges.show_privileges()}")