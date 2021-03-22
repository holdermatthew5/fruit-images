from django.contrib.auth.models import User

user = User.objects.get(username='holdermatthew5')
user.is_staff = True # Set to False to revoke priviliges
user.is_admin = True # Set to False to revoke priviliges
user.save()