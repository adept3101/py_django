from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            is_superuser = request.POST.get('is_superuser', False)
            if is_superuser:
                if not User.objects.filter(is_superuser=True).exists():
                    user.is_superuser = True
                    user.is_staff = True
                else:
                    pass
            
            user.save()
            login(request, user)
            return redirect('login')
            #return redirect('users/login.html')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('unified-feeds')
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required # edit
def unified_feeds_view(request):
    # Параметры пагинации
    items_per_page = 50
    active_tab = request.GET.get('tab', 'fincert')
    # Фильтрация по дате фиксации
    date_filter = request.GET.get('date_filter', '')

    # ФинЦерт - базовые запросы
    fincert_dates = FeedsFinCertDateDownloads.objects.select_related('feedstype').order_by('-date')[:10]

    # Создаем QuerySet для каждого типа данных с фильтрацией
    def get_filtered_queryset(model, date_field='dateFixed'):
        queryset = model.objects.select_related('datedownloads').all()
        if date_filter:
            queryset = queryset.filter(**{f'{date_field}__icontains': date_filter})
        return queryset.order_by(f'-{date_field}')

    # ФинЦерт данные
    account_numbers = get_filtered_queryset(FeedsAccountNumbers)
    card_numbers = get_filtered_queryset(FeedsCardNumbers)
    ewallet_numbers = get_filtered_queryset(FeedsEwalletNumbers)
    fastpay_numbers = get_filtered_queryset(FeedsFastpayNumbers)
    inn_numbers = get_filtered_queryset(FeedsInn)
    passport_hashes = get_filtered_queryset(FeedsPassportHash)
    phone_numbers = get_filtered_queryset(FeedsPhoneNumbers)
    snils_hashes = get_filtered_queryset(FeedsSnilsHash)
    swift_data = get_filtered_queryset(FeedsSwift)

    # МВД данные (без пагинации)
    mvd_dates = FeedsMvdDateDownloads.objects.all().order_by('-date')[:10]
    mvd_accounts = get_filtered_queryset(FeedsMvdAccountNumbers, 'datedownloads__date')
    mvd_cards = get_filtered_queryset(FeedsMvdCardNumbers, 'datedownloads__date')
    mvd_fastpay = get_filtered_queryset(FeedsMvdFastPayNumbers, 'datedownloads__date')
    mvd_inn = get_filtered_queryset(FeedsMvdInn, 'datedownloads__date')
    mvd_passports = get_filtered_queryset(FeedsMvdPassportHash, 'datedownloads__date')

    # IOC данные
    ioc_data = FinCertIocDateProcessing.objects.select_related('feedstype').order_by('-dateMailing')[:10]

    # Пагинация только для данных ФинЦерт
    def paginate_data(request, data, param_name):
        paginator = Paginator(data, items_per_page)
        page_number = request.GET.get(f'{param_name}_page')
        return paginator.get_page(page_number)

    # Контекст для шаблона
    context = {
        'active_tab': active_tab,
        'date_filter': date_filter,

        # ФинЦерт (с пагинацией)
        'fincert_dates': fincert_dates,
        'account_numbers_page': paginate_data(request, account_numbers, 'account'),
        'card_numbers_page': paginate_data(request, card_numbers, 'card'),
        'ewallet_numbers_page': paginate_data(request, ewallet_numbers, 'ewallet'),
        'fastpay_numbers_page': paginate_data(request, fastpay_numbers, 'fastpay'),
        'inn_numbers_page': paginate_data(request, inn_numbers, 'inn'),
        'passport_hashes_page': paginate_data(request, passport_hashes, 'passport'),
        'phone_numbers_page': paginate_data(request, phone_numbers, 'phone'),
        'snils_hashes_page': paginate_data(request, snils_hashes, 'snils'),
        'swift_data_page': paginate_data(request, swift_data, 'swift'),

        # МВД (без пагинации)
        'mvd_dates': mvd_dates,
        'mvd_accounts': mvd_accounts,
        'mvd_cards': mvd_cards,
        'mvd_fastpay': mvd_fastpay,
        'mvd_inn': mvd_inn,
        'mvd_passports': mvd_passports,

        # IOC
        'ioc_data': ioc_data,
    }

    return render(request, 'users/unified_view.html', context)