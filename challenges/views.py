from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        raise Http404()
    
    redirect_month = months[month - 1]
    reverse_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(reverse_path)


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge,
            "month": month
        })
    except:
        raise Http404()
        
    

def challenges(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })
    
    