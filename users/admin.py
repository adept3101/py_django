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

