from django.contrib.auth.mixins import PermissionRequiredMixin
#tfrom django.contrib.auth.mixins import PermissionMixin

class RolePermission(PermissionRequiredMixin):

    allowed_roles = []  # Список разрешённых ролей

    def has_permission(self, request, view):
        user = request.user

        # Проверяем, что пользователь аутентифицирован
        if not user.is_authenticated:
            return False

        # Проверяем, что роль пользователя входит в список разрешённых ролей
        if user.role and user.role.name in self.allowed_roles:
            return True

        return False