from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

months = {
    "january": "Today is month 1",
    "february": "Today is month 2",
    "march": "Today is month 3",
    "abril": "Today is month 4",
    "may": "Today is month 5",
    "june": "Today is month 6",
    "july": "Today is month 7",
    "august": "Today is month 8",
    "september": "Today is month 9",
    "october": "Today is month 10",
    "november": "Today is month 11",
    "december": None
}

def index(request):
    month_all = list(months.keys())
    return render(request, "challenges/index.html", {
        "month_all": month_all
        })


def monthly_challenge_numbers(request, month):
    months_list = list(months.keys())
    if month > len(months_list):
        return HttpResponseNotFound("This month is not supported")
    else:
        redirect_month = months_list[month -1]
        redirect_patch = reverse("month-chalenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_patch)

def monthly_challenge(request, month):
    try:
        challenge_text = months[month]
        #months_list = list(months.keys())
        
        return render(request,"challenges/challenge.html", {
            "text": challenge_text,
            "challenge_month": month.capitalize()
        })
    
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")

    

