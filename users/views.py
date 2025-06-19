from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .decorators import role_required, group_required
from django.views import View
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator

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
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def page(request):
    return render(request,'users/index.html')

class ViewMixin(View):
    items_per_page = 50

    @staticmethod
    def get_filtered_queryset(model, date_filter, date_field='dateFixed'):
        queryset = model.objects.select_related('datedownloads').all()
        if date_filter:
            queryset = queryset.filter(**{f'{date_field}__icontains': date_filter})
        return queryset.order_by(f'-{date_field}')

    @staticmethod
    def paginate_data(request, data, param_name, items_per_page=50):
        paginator = Paginator(data, items_per_page)
        page_number = request.GET.get(f'{param_name}_page')
        return paginator.get_page(page_number)

class GroupRequiredMixin:
    allowed_groups = []

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and (user.is_superuser or user.groups.filter(name__in=self.allowed_groups).exists()):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

class FincertView(GroupRequiredMixin, ViewMixin, View):
    allowed_groups=['Admin', 'Analyst']
    def get(self, request):
        active_tab = request.GET.get('tab', 'fincert')
        date_filter = request.GET.get('date_filter', '')

        fincert_dates = FeedsFinCertDateDownloads.objects.select_related('feedstype').order_by('-date')[:10]

        account_numbers = self.get_filtered_queryset(FeedsAccountNumbers,date_filter)
        card_numbers = self.get_filtered_queryset(FeedsCardNumbers, date_filter)
        ewallet_numbers = self.get_filtered_queryset(FeedsEwalletNumbers, date_filter)
        fastpay_numbers = self.get_filtered_queryset(FeedsFastpayNumbers, date_filter)
        inn_numbers = self.get_filtered_queryset(FeedsInn, date_filter)
        passport_hashes = self.get_filtered_queryset(FeedsPassportHash, date_filter)
        phone_numbers = self.get_filtered_queryset(FeedsPhoneNumbers, date_filter)
        snils_hashes = self.get_filtered_queryset(FeedsSnilsHash, date_filter)
        swift_data = self.get_filtered_queryset(FeedsSwift, date_filter)

        context = {
            'active_tab': active_tab,
            'date_filter': date_filter,

            'fincert_dates': fincert_dates,
            'account_numbers_page': self.paginate_data(request, account_numbers, 'account'),
            'card_numbers_page': self.paginate_data(request, card_numbers, 'card'),
            'ewallet_numbers_page': self.paginate_data(request, ewallet_numbers, 'ewallet'),
            'fastpay_numbers_page': self.paginate_data(request, fastpay_numbers, 'fastpay'),
            'inn_numbers_page': self.paginate_data(request, inn_numbers, 'inn'),
            'passport_hashes_page': self.paginate_data(request, passport_hashes, 'passport'),
            'phone_numbers_page': self.paginate_data(request, phone_numbers, 'phone'),
            'snils_hashes_page': self.paginate_data(request, snils_hashes, 'snils'),
            'swift_data_page': self.paginate_data(request, swift_data, 'swift'),
        }
        return render(request, 'users/fincert.html', context)
    
    # def post(self, request):
    #     if 'delete' in request.POST:
    #         selected_items = request.POST.getlist('selected_items')
    #         if selected_items:
    #             FeedsAccountNumbers.objects.filter(id__in=selected_items).delete()
    #             messages.success(request, "Выбранные записи успешно удалены.")
    #         else:
    #             messages.warning(request, "Не выбрано ни одной записи для удаления.")
    #     return redirect('fincert')
    
class MVDViews(GroupRequiredMixin, ViewMixin, View):
    allowed_groups=['Admin', 'Analyst']
    def get(self, request):
        active_tab = request.GET.get('tab', 'fincert')
        date_filter = request.GET.get('date_filter', '')

        mvd_dates = FeedsMvdDateDownloads.objects.all().order_by('-date')[:10]

        mvd_accounts = self.get_filtered_queryset(FeedsMvdAccountNumbers, date_filter, 'datedownloads__date')
        mvd_cards = self.get_filtered_queryset(FeedsMvdCardNumbers, date_filter, 'datedownloads__date')
        mvd_fastpay = self.get_filtered_queryset(FeedsMvdFastPayNumbers, date_filter, 'datedownloads__date')
        mvd_inn = self.get_filtered_queryset(FeedsMvdInn, date_filter, 'datedownloads__date')
        mvd_passports = self.get_filtered_queryset(FeedsMvdPassportHash, date_filter, 'datedownloads__date')
        
        context = {
            'active_tab': active_tab,
            'date_filter': date_filter,

            'mvd_dates': mvd_dates,
            'mvd_accounts': mvd_accounts,
            'mvd_cards': mvd_cards,
            'mvd_fastpay': mvd_fastpay,
            'mvd_inn': mvd_inn,
            'mvd_passports': mvd_passports,
        }
        return render(request, 'users/mvd.html', context)

class IOCViews(GroupRequiredMixin, ViewMixin, View):
    allowed_groups=['Admin', 'Network Admin']
    def get(self, request):
        active_tab = request.GET.get('tab', 'fincert')
        date_filter = request.GET.get('date_filter', '')

        ioc_data = FinCertIocDateProcessing.objects.select_related('feedstype').order_by('-dateMailing')[:10]

        context = {
            'active_tab': active_tab,
            'date_filter': date_filter,

            'ioc_data': ioc_data,
        }
        return render(request, 'users/ioc.html', context)
    
@login_required
@group_required(['Admin', 'Analyst'])
def delete_accounts(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items')
        if selected_items:
            FeedsAccountNumbers.objects.filter(id__in=selected_items).delete()
            messages.success(request, "Выбранные записи успешно удалены.")
        else:
            messages.warning(request, "Не выбрано ни одной записи для удаления.")
    
    return redirect('fincert')