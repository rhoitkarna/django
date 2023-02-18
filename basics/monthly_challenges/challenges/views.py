from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Work out everyday",
    "march": "Learn Django for 2 hours",
    "april": "Study for Exams",
    "may": "Complete all given assignments",
    "june": "Revise Python",
    "july": "Learn data science",
    "august": "Complete a project",
    "september": "Prepare for interviews",
    "october": "Make other projects",
    "november": "Apply for internships",
    "december": "Find a job"
}


def index(request):
    list_items = """"""
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<h2><li><a href='{month_path}'>{month.capitalize()}</a></li></h2>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")

    redirected_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirected_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html", {
            "text": challenge_text,
            "month": month,
        })
    except KeyError:
        return HttpResponseNotFound("<h1>This month doesn't exist.</h1>")
