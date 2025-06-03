from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def permission_id_required(*required_ids):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            user_perm_ids = request.user.user_permissions.values_list('id', flat=True)
            if any(perm_id in user_perm_ids for perm_id in required_ids):
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("У вас нет доступа к этой странице.")
        return _wrapped_view
    return decorator
