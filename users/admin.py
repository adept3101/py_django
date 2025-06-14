from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import (
    FeedsTypeNavigation,
    FeedsFinCertDateDownloads,
    FeedsAccountNumbers, FeedsCardNumbers, FeedsEwalletNumbers,
    FeedsFastpayNumbers, FeedsInn, FeedsPassportHash,
    FeedsPhoneNumbers, FeedsSnilsHash, FeedsSwift,
    FeedsMvdDateDownloads, FeedsMvdAccountNumbers,
    FeedsMvdCardNumbers, FeedsMvdFastPayNumbers,
    FeedsMvdInn, FeedsMvdPassportHash,
    FinCertIocDateProcessing
)


admin.site.register(FeedsTypeNavigation)
admin.site.register(FeedsFinCertDateDownloads)
admin.site.register(FinCertIocDateProcessing)
admin.site.register(FeedsAccountNumbers)
admin.site.register(FeedsCardNumbers)
admin.site.register(FeedsEwalletNumbers)
admin.site.register(FeedsFastpayNumbers)
admin.site.register(FeedsInn)
admin.site.register(FeedsPassportHash)
admin.site.register(FeedsPhoneNumbers)
admin.site.register(FeedsSnilsHash)
admin.site.register(FeedsSwift)
admin.site.register(FeedsMvdDateDownloads)
admin.site.register(FeedsMvdAccountNumbers)
admin.site.register(FeedsMvdCardNumbers)
admin.site.register(FeedsMvdFastPayNumbers)
admin.site.register(FeedsMvdInn)
admin.site.register(FeedsMvdPassportHash)

admin_group, _ = Group.objects.get_or_create(name='Admin')

permission = Permission.objects.get(codename='add_user')

admin_group.permissions.add(permission)

analyst_group, _ = Group.objects.get_or_create(name='Analyst')

network_admin_group, _ = Group.objects.get_or_create(name='Network Admin')

user_group, _ = Group.objects.get_or_create(name='User')

# try:
#     permission = Permission.objects.get(codename='add_user')
#     admin_group.permissions.add(permission)
# except Permission.DoesNotExist:
#     pass

# # Админ-классы с ограничением доступа по ролям
# def make_admin(model):
#     @admin.register(model)
#     class RoleBasedAdmin(admin.ModelAdmin):
#         def has_view_permission(self, request, obj=None):
#             return request.user.groups.filter(name__in=['Admin', 'Analyst']).exists()

#         def has_module_permission(self, request):
#             return self.has_view_permission(request)

#         def has_change_permission(self, request, obj=None):
#             return request.user.groups.filter(name='Admin').exists()

#         def has_add_permission(self, request):
#             return request.user.groups.filter(name='Admin').exists()

#         def has_delete_permission(self, request, obj=None):
#             return request.user.groups.filter(name='Admin').exists()
#     return RoleBasedAdmin

# # Применяем админ-классы ко всем моделям
# make_admin(FeedsTypeNavigation)
# make_admin(FeedsFinCertDateDownloads)
# make_admin(FinCertIocDateProcessing)
# make_admin(FeedsAccountNumbers)
# make_admin(FeedsCardNumbers)
# make_admin(FeedsEwalletNumbers)
# make_admin(FeedsFastpayNumbers)
# make_admin(FeedsInn)
# make_admin(FeedsPassportHash)
# make_admin(FeedsPhoneNumbers)
# make_admin(FeedsSnilsHash)
# make_admin(FeedsSwift)
# make_admin(FeedsMvdDateDownloads)
# make_admin(FeedsMvdAccountNumbers)
# make_admin(FeedsMvdCardNumbers)
# make_admin(FeedsMvdFastPayNumbers)
# make_admin(FeedsMvdInn)
# make_admin(FeedsMvdPassportHash)