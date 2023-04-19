from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs,):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1>Home Page</h1>") # string of HTML code
    return render(request, "home.html", {})
def about_view(request,*args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number" : 923332103786,
        "my_list" : [1,2,3,4,5]
    }     
    return render(request, "about.html", my_context) # string of HTML code

def contact_view(request,*args, **kwargs):
    
    return render(request, "contact.html", {}) # string of HTML code

