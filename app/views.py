from django.shortcuts import render
from django.http import HttpRequest
import random
from dataclasses import dataclass
from typing import List

@dataclass
class Team:
    title: str
    members: List[str]
    desc: str


# Create your views here.

def home_view(request):
    context = {
        "teams": ["Management", "Documentation", "Community", "Procurement"],
    }

    return render(request, "home.html", context)

def teams_view(request, team):
    context = {
        "team": team,
        "LP":{
            "Management": Team("Management", ["Will", "Logan C.", "Michelle", "Rylee", "Daelan", "Dylan G."], "Keeps Basecamp running like a well oiled machine!"),

            "Procurement": Team("Procurement", ["Ethan", "Richard", "Dylan S.", "Mariann", "Quinton", "Gary/Trey"], "Responsible for ordering supplies, works closely with each team."),

            "Documentation": Team("Documentation", ["Randy", "Ryan", "Ben", "Ma'kyla", "Isaac"], "Maintains Basecamp's social media"),

            "Community": Team("Community", ["Jacen", "Justin", "Ariyana", "RJay", "Logan W."], "Organizes fun events to keep the Basecamp community strong.")
        }
    }
    return render(request, "teams.html", context)

