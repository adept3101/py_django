# Generated by Django 5.2 on 2025-05-10 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedsAccountNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumbers', models.IntegerField(verbose_name='Номер счета')),
                ('bic', models.IntegerField(verbose_name='БИК')),
                ('dateFixed', models.CharField(max_length=30, verbose_name='Дата и время фиксации инцидента')),
                ('count', models.SmallIntegerField(verbose_name='Количество')),
                ('country', models.CharField(max_length=15, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsCardNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNumbers', models.IntegerField(verbose_name='Номер карты')),
                ('dateFixed', models.CharField(max_length=30, verbose_name='Дата и время фиксации инцидента')),
                ('count', models.SmallIntegerField(verbose_name='Количество')),
                ('country', models.CharField(max_length=15, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsEwalletNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ewalletNumbers', models.IntegerField(verbose_name='Номер кошелька')),
                ('paymentSystem', models.CharField(max_length=100, verbose_name='Название платежной системы')),
                ('dateFixed', models.CharField(max_length=30, verbose_name='Дата и время фиксации инцидента')),
                ('count', models.SmallIntegerField(verbose_name='Количество')),
                ('country', models.CharField(max_length=15, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsFastpayNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fastpayNumber', models.IntegerField(verbose_name='Номер телефона')),
                ('dateFixed', models.CharField(max_length=30, verbose_name='Дата и время фиксации инцидента')),
                ('count', models.SmallIntegerField(verbose_name='Количество')),
                ('country', models.CharField(max_length=15, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsFinCertDateDownloads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Время скачивания фидов')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsInn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.IntegerField(verbose_name='ИНН')),
                ('dateFixed', models.CharField(max_length=30, verbose_name='Дата и время фиксации инцидента')),
                ('count', models.SmallIntegerField(verbose_name='Количество')),
                ('country', models.CharField(max_length=15, verbose_name='Страна')),
                ('datedownloads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsfincertdatedownloads')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsMvdAccountNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumbers', models.IntegerField(verbose_name='Номер счета')),
                ('bic', models.IntegerField(verbose_name='БИК')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsMvdCardNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNumbers', models.IntegerField(verbose_name='Номер карты')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsMvdDateDownloads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Время скачивания фидов МВД')),
                ('nameFeedsTrim', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FeedsMvdFastPayNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fastpayNumber', models.IntegerField(verbose_name='Номер телефона')),
                ('datedownloads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsmvddatedownloads')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsMvdInn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.IntegerField(verbose_name='ИНН')),
                ('datedownloads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsmvddatedownloads')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsMvdPassportHash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passportHash', models.CharField(max_length=150, verbose_name='Хеш паспорта')),
                ('datedownloads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsmvddatedownloads')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsPassportHash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passportHash', models.CharField(max_length=150, verbose_name='Хеш паспорта')),
                ('dateFixed', models.CharField(max_length=30, verbose_name='Дата и время фиксации инцидента')),
                ('count', models.SmallIntegerField(verbose_name='Количество')),
                ('country', models.CharField(max_length=15, verbose_name='Страна')),
                ('datedownloads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsfincertdatedownloads')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsPhoneNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumbers', models.IntegerField(verbose_name='Номер телефона')),
                ('dateFixed', models.CharField(max_length=30, verbose_name='Дата и время фиксации инцидента')),
                ('count', models.SmallIntegerField(verbose_name='Количество')),
                ('country', models.CharField(max_length=15, verbose_name='Страна')),
                ('datedownloads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsfincertdatedownloads')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsSnilsHash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashSnils', models.CharField(max_length=200, verbose_name='Хеш СНИЛСа')),
                ('dateFixed', models.CharField(max_length=30, verbose_name='Дата и время фиксации инцидента')),
                ('count', models.SmallIntegerField(verbose_name='Количество')),
                ('country', models.CharField(max_length=15, verbose_name='Страна')),
                ('datedownloads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsfincertdatedownloads')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsSwift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumbersSwift', models.CharField(max_length=150, verbose_name='Номер счета')),
                ('swiftBIC', models.CharField(max_length=50, verbose_name='SWIFT БИК')),
                ('dateFixed', models.CharField(max_length=30, verbose_name='Дата и время фиксации инцидента')),
                ('count', models.SmallIntegerField(verbose_name='Количество')),
                ('country', models.CharField(max_length=15, verbose_name='Страна')),
                ('datedownloads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsfincertdatedownloads')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsTypeNavigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeds_name', models.CharField(max_length=20, verbose_name='Название фидов')),
                ('feeds_description', models.TextField(verbose_name='Описание фидов')),
            ],
        ),
        migrations.CreateModel(
            name='FinCertIocDateProcessing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateMailing', models.DateField(verbose_name='Дата рассылки IOC')),
                ('dateProccesing', models.DateTimeField(verbose_name='Дата и время обработки IOC')),
                ('iocTrim', models.CharField(max_length=50, verbose_name='Индентификатор IOC')),
                ('feedstype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedstypenavigation')),
            ],
        ),
        migrations.DeleteModel(
            name='Feeds',
        ),
        migrations.AddField(
            model_name='feedsfastpaynumbers',
            name='datedownloads',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsfincertdatedownloads'),
        ),
        migrations.AddField(
            model_name='feedsewalletnumbers',
            name='datedownloads',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsfincertdatedownloads'),
        ),
        migrations.AddField(
            model_name='feedscardnumbers',
            name='datedownloads',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsfincertdatedownloads'),
        ),
        migrations.AddField(
            model_name='feedsaccountnumbers',
            name='datedownloads',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsfincertdatedownloads'),
        ),
        migrations.AddField(
            model_name='feedsmvdcardnumbers',
            name='datedownloads',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsmvddatedownloads'),
        ),
        migrations.AddField(
            model_name='feedsmvdaccountnumbers',
            name='datedownloads',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedsmvddatedownloads'),
        ),
        migrations.AddField(
            model_name='feedsmvddatedownloads',
            name='feedstype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedstypenavigation'),
        ),
        migrations.AddField(
            model_name='feedsfincertdatedownloads',
            name='feedstype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.feedstypenavigation'),
        ),
    ]
