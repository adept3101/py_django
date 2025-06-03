# users/templatetags/permission_tags.py
from django import template
from django.contrib.auth.models import Permission

register = template.Library()

@register.filter(name='has_permission')
def has_permission(user, permission_id):
    return user.user_permissions.filter(id=permission_id).exists() or \
           user.groups.filter(permissions__id=permission_id).exists()