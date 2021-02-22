from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
        "title":"Main Store Page",
        "content":"Welcome to Kalle's first ecommerce store",

    }
    if request.user.is_authenticated():
        context["premium_content"] = "Premium Content"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About Page",
        "content":"About this online store"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":"Please contact us for any enquiries",
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method  == "POST":
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    print("User logged in:")
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated())
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            #redirects to success page
            context["form"] = LoginForm()
            return redirect("/login")
        else: 
            #returns invalid login error message
            print("Error")
    
    return render(request, "auth/login.html", context)

def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})



# OLD CODE
#
#
# def home_page_old(request):
#     html_ = """
#     <!doctype html>
#     <html lang="en">
#     <head>
#         <!-- Required meta tags -->
#         <meta charset="utf-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1">

#         <!-- Bootstrap CSS -->
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

#         <title>Kalle's Online Store</title>
#     </head>
#     <body>
#         <div class="text-center">
#         <h1>Kalle's Online Store</h1>
#         </div>
#         <!-- Optional JavaScript; choose one of the two! -->

#         <!-- Option 1: Bootstrap Bundle with Popper -->
#         <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>

#         <!-- Option 2: Separate Popper and Bootstrap JS -->
#         <!--
#         <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.6.0/dist/umd/popper.min.js" integrity="sha384-KsvD1yqQ1/1+IA7gi3P0tyJcT3vR+NdBTt13hSJ2lnve8agRGXTTyNaBYmCR/Nwi" crossorigin="anonymous"></script>
#         <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.min.js" integrity="sha384-nsg8ua9HAw1y0W1btsyWgBklPnCUAFLuTMS2G72MMONqmOymq585AcH49TLBQObG" crossorigin="anonymous"></script>
#         -->
#     </body>
#     </html>
#     """
#     return HttpResponse(html_)
