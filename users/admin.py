from django.contrib import admin
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

# Регистрация простых моделей
admin.site.register(FeedsTypeNavigation)
admin.site.register(FeedsFinCertDateDownloads)
admin.site.register(FinCertIocDateProcessing)
