from django.db import models
#Таблица для навигации
class FeedsTypeNavigation(models.Model):
    feeds_name = models.CharField('Название фидов', max_length=20)
    feeds_description = models.TextField('Описание фидов')
    class Meta:
        verbose_name = 'Типы фидов (данных)'
        verbose_name_plural = verbose_name

class FeedsFinCertDateDownloads(models.Model):
    feedstype = models.ForeignKey(FeedsTypeNavigation, on_delete=models.CASCADE)
    date = models.CharField('Время скачивания фидов',max_length=30)
#Таблицы фидов ФинЦерт
class FeedsAccountNumbers(models.Model):
    datedownloads = models.ForeignKey(FeedsFinCertDateDownloads, on_delete=models.SET_NULL, null=True)
    accountNumbers = models.CharField('Номер счета',max_length=64)
    bic = models.CharField('БИК',max_length=64)
    dateFixed = models.CharField('Дата и время фиксации инцидента', max_length=30)
    count = models.SmallIntegerField('Количество')
    country = models.CharField('Страна', max_length=15)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True )

class FeedsCardNumbers(models.Model):
    datedownloads = models.ForeignKey(FeedsFinCertDateDownloads, on_delete=models.SET_NULL, null=True)
    cardNumbers = models.CharField('Номер карты', max_length=64)
    dateFixed = models.CharField('Дата и время фиксации инцидента', max_length=30)
    count = models.SmallIntegerField('Количество')
    country = models.CharField('Страна', max_length=15)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsEwalletNumbers(models.Model):
    datedownloads = models.ForeignKey(FeedsFinCertDateDownloads, on_delete=models.SET_NULL, null=True)
    ewalletNumbers = models.CharField('Номер кошелька', max_length=64)
    paymentSystem = models.CharField('Название платежной системы', max_length=100)
    dateFixed = models.CharField('Дата и время фиксации инцидента', max_length=30)
    count = models.SmallIntegerField('Количество')
    country = models.CharField('Страна', max_length=15)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsFastpayNumbers(models.Model):
    datedownloads = models.ForeignKey(FeedsFinCertDateDownloads, on_delete=models.SET_NULL, null=True)
    fastpayNumber = models.CharField('Номер телефона', max_length=100)
    dateFixed = models.CharField('Дата и время фиксации инцидента', max_length=30)
    count = models.SmallIntegerField('Количество')
    country = models.CharField('Страна', max_length=15)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsInn(models.Model):
    datedownloads = models.ForeignKey(FeedsFinCertDateDownloads, on_delete=models.SET_NULL, null=True)
    inn = models.CharField('ИНН', max_length=30)
    dateFixed = models.CharField('Дата и время фиксации инцидента', max_length=30)
    count = models.SmallIntegerField('Количество')
    country = models.CharField('Страна', max_length=15)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsPassportHash(models.Model):
    datedownloads = models.ForeignKey(FeedsFinCertDateDownloads, on_delete=models.SET_NULL, null=True)
    passportHash = models.CharField('Хеш паспорта',max_length=150)
    dateFixed = models.CharField('Дата и время фиксации инцидента', max_length=30)
    count = models.SmallIntegerField('Количество')
    country = models.CharField('Страна', max_length=15)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsPhoneNumbers(models.Model):
    datedownloads = models.ForeignKey(FeedsFinCertDateDownloads, on_delete=models.SET_NULL, null=True)
    phoneNumbers = models.CharField('Номер телефона', max_length=64)
    dateFixed = models.CharField('Дата и время фиксации инцидента', max_length=30)
    count = models.SmallIntegerField('Количество')
    country = models.CharField('Страна', max_length=15)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsSnilsHash(models.Model):
    datedownloads = models.ForeignKey(FeedsFinCertDateDownloads, on_delete=models.SET_NULL, null=True)
    hashSnils = models.CharField('Хеш СНИЛСа', max_length=200)
    dateFixed = models.CharField('Дата и время фиксации инцидента', max_length=30)
    count = models.SmallIntegerField('Количество')
    country = models.CharField('Страна', max_length=15)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsSwift(models.Model):
    datedownloads = models.ForeignKey(FeedsFinCertDateDownloads, on_delete=models.SET_NULL, null=True)
    accountNumbersSwift = models.CharField('Номер счета', max_length=150)
    swiftBIC= models.CharField('SWIFT БИК', max_length=50)
    dateFixed = models.CharField('Дата и время фиксации инцидента', max_length=30)
    count = models.SmallIntegerField('Количество')
    country = models.CharField('Страна', max_length=15)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

#Таблицы фидов МВД
class FeedsMvdDateDownloads(models.Model):
    feedstype = models.ForeignKey(FeedsTypeNavigation, on_delete=models.CASCADE)
    date = models.CharField('Время скачивания фидов',max_length=30)
    nameFeedsTrim = models.CharField(max_length=50)

class FeedsMvdAccountNumbers(models.Model):
    datedownloads = models.ForeignKey(FeedsMvdDateDownloads, on_delete=models.SET_NULL, null=True)
    accountNumbers = models.CharField('Номер счета', max_length=64)
    bic = models.CharField('БИК', max_length=64)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsMvdCardNumbers(models.Model):
    datedownloads = models.ForeignKey(FeedsMvdDateDownloads, on_delete=models.SET_NULL, null=True)
    cardNumbers = models.CharField('Номер карты', max_length=64)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsMvdFastPayNumbers(models.Model):
    datedownloads = models.ForeignKey(FeedsMvdDateDownloads, on_delete=models.SET_NULL, null=True)
    fastpayNumber = models.CharField('Номер телефона', max_length=64)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsMvdInn(models.Model):
    datedownloads = models.ForeignKey(FeedsMvdDateDownloads, on_delete=models.SET_NULL, null=True)
    inn = models.CharField('ИНН', max_length=30)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

class FeedsMvdPassportHash(models.Model):
    datedownloads = models.ForeignKey(FeedsMvdDateDownloads, on_delete=models.SET_NULL, null=True)
    passportHash = models.CharField('Хеш паспорта', max_length=150)
    dateExcluded = models.DateTimeField("Дата удаления из списка", null=True)

#Таблица для даты обработки IOC
class FinCertIocDateProcessing(models.Model):
    feedstype = models.ForeignKey(FeedsTypeNavigation, on_delete=models.CASCADE)
    dateMailing = models.CharField("Дата рассылки IOC", max_length=30)
    date = models.CharField('Время скачивания фидов',max_length=30, null=True, blank=True)
    iocTrim = models.CharField('Индентификатор IOC',max_length=50)

class Resource(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ('can_view_mvd', 'Может просматривать МВД'),
            ('can_view_fincert', 'Может просматривать ФинСерт'),
            ('can_view_ioc', 'Может просматривать IOC'),
        ]

from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    can_view_fincert = models.BooleanField(default=False)
    can_view_mvd = models.BooleanField(default=False)
    can_view_ioc = models.BooleanField(default=False)
    @classmethod
    def get_for_user(cls, user):
        obj, created = cls.objects.get_or_create(user=user)
        return obj