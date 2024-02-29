from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from django import forms


class NewLoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    confirm = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

# Create your views here.
def index(request):
    if "username" not in request.session:
        # request.session["username"] = ""
        return HttpResponseRedirect(reverse("sitecharlie:login"))
    return render(request, "sitecharlie/index.html", {"username":request.session["username"]})


def i_login(request):
    if "username" in request.session:
        del request.session['username']

    if request.method=="POST":
        form = NewLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            request.session["username"] = username
        return HttpResponseRedirect(reverse("sitecharlie:index"))
        # else:
        #     return render(request, "sitecharlie/login.html", {"form":form})
        
    # else:
    return render(request, "sitecharlie/login.html", {"form":NewLoginForm()})


def register(request):
    return render(request, "sitecharlie/register.html", {"form": RegisterForm()} )