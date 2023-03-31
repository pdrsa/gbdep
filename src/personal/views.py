from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    context = {
        "some_string": "this is some string that I am passing to the view",
    }

    return render(request, "personal/home.html", context)