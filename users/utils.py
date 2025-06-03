from django.contrib.auth.models import Permission

def check_user_permission(user, permission_id):
    return user.user_permissions.filter(id=permission_id).exists()