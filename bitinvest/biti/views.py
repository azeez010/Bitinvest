import os, git
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from multiprocessing import parent_process
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from biti.helpers import forms, enums
from biti import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
from biti.helpers.utils import get_global_variables


# Create your views here.
@csrf_exempt
def git_update(request):
    if request.method == "POST":
        os.chdir("/home/turkeyapp")
        repo = git.Repo('./vipprotipsters')
        origin = repo.remotes.origin
        repo.create_head('master',
        origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        #repo.heads.master.set_tracking_branch(origin.refs.master)
        #all note
        origin.pull()
        # return 'success', 200
        return JsonResponse({'success':'True'})

@login_required
def trade(request):
    try:
        models.KGS.objects.get(user=request.user, used=True, product_type=enums.ProductType.TRADE.value)
        trades = models.Trade.objects.all()
        return render(request,'trade.html', context={"trades": trades})
    except models.KGS.DoesNotExist:
        return redirect(reverse("activate-key", kwargs={"key_type": enums.ProductType.TRADE.value}))

@login_required
def invest(request):
    try:
        models.KGS.objects.get(user=request.user, used=True, product_type=enums.ProductType.INVEST.value)
        invest = models.Invest.objects.all()
        messages.error(request, "ENJOY OUR PASTOR NETWORK")
        return render(request,'invest.html', context={"invest": invest})
    except models.KGS.DoesNotExist:
        return redirect(reverse("activate-key", kwargs={"key_type": enums.ProductType.INVEST.value}))

@login_required
def partner(request):
    try:
        models.KGS.objects.get(user=request.user, used=True, product_type=enums.ProductType.PARTNER.value)
        
        if request.user.wallet > get_global_variables(enums.Settings.PARTNER.value):
            pass
        else:
            messages.error(request, "OOPS! YOU ARE NOT ELIGIBLE")
            
        return render(request,'partner.html')
    except models.KGS.DoesNotExist:
        return redirect(reverse("activate-key", kwargs={"key_type": enums.ProductType.PARTNER.value}))

@login_required
def activate_key(request, key_type):
    try:
        models.KGS.objects.get(user=request.user, used=True, product_type=key_type)
        return redirect(reverse(key_type))
    except models.KGS.DoesNotExist:
        # messages.error(request, "You need a ref key")
        return render(request,'activate_key.html', context={"key_type": key_type})

def home_view(request):
    return render(request,'transocean/deepwater/index.html', context={})
    
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Login Successful")
            return redirect(reverse("home-menu"))

        else:
            messages.error(request, "wrong password or email Address")
            return redirect(reverse("login-view"))
    
    login_form = forms.Login()
    context = {"login" : login_form}
    return render(request, "login.html", context)

def signup_view(request):
    if request.method == "POST":
        user_sign_up = forms.SignUp(request.POST)
        if user_sign_up.is_valid():
            user = user_sign_up.save()
            user.set_password(user.password)
            user.save()
            # messages.success(request, "Signup Successful")
            return redirect(reverse("login-view"))
        else:
            messages.error(request, f"{user_sign_up.errors}" )
            return redirect(reverse("signup-view"))
    
    sign_up = forms.SignUp()
    context = {"sign_up" : sign_up}
    return render(request, "signup.html", context)
    
def change_password_view(request):
    if request.method == "POST":
        user_sign_up = forms.ChangePassword(request.POST)
        if user_sign_up.is_valid():
            User = get_user_model()
            user = User.objects.get(id=request.user.id)
            if user.check_password(user_sign_up.cleaned_data.get("password")):
                password = user_sign_up.cleaned_data.get("password")
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)
                
                messages.success(request, "Password Changed Successfully")
            else:
                messages.error(request, "Old Password incorrect")
            return redirect(reverse("paid"))
        else:
            messages.error(request, f"{user_sign_up.errors}" )
            return redirect(reverse("paid"))

@login_required
def home_menu(request):
    template_name = "home.html"
        
    return render(request, template_name, {} )