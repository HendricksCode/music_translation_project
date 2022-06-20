from django.shortcuts import render
from django.http import HttpResponse #(imported during video)

# Create your views here.
def home_view(request, *args, **kwargs): #LOOK UP ARGS AND KWARGS!!!
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def terms_view(request, *args, **kwargs): 
    my_context = {
        "my_text": "This is some text",
        "my_number": 1234,
        "my_list": [12, 43463, 35463, 321, "ABC"],
        "this_is_true": True
    }


    return render(request, "terms.html", my_context)