from django.shortcuts import render
from .models import Events
from datetime import date

# Create your views here.
def blank(req):
    return render(req,'base.html')
def events(requests):
    e={}
    query=requests.GET.get('search')
    if(query):
        e=Events.objects.filter(EventName__icontains=query)
    else:
        e=Events.objects.all()
    return render(requests,'events.html',{'e':e})
def add(req):
    event = [
        {"EventName": "Djangocon 2024", "EventDate": "2024-09-15", "Location": "Ahmedabad", "Category": "Conference"},
        {"EventName": "Tech Meetup", "EventDate": "2024-09-20", "Location": "Rajkot", "Category": "Meetup"},
        {"EventName": "Data Science Meetup", "EventDate": "2024-09-21", "Location": "Surat", "Category": "Meetup"},
        {"EventName": "Startup Pitch Seminar", "EventDate": "2024-09-23", "Location": "Vadodara", "Category": "Seminar"},
        {"EventName": "Innovation Expo", "EventDate": "2024-09-26", "Location": "Ahmedabad", "Category": "Exhibition"},
        {"EventName": "Security Hackathon", "EventDate": "2024-09-30", "Location": "Surat", "Category": "Hackathon"},
        {"EventName": "Machine Learning 101", "EventDate": "2024-10-01", "Location": "Vadodara", "Category": "Webinar"},
        {"EventName": "Python Workshop", "EventDate": "2024-10-05", "Location": "Ahmedabad", "Category": "Workshop"},
        {"EventName": "AI Hackathon", "EventDate": "2024-10-10", "Location": "Ahmedabad", "Category": "Hackathon"},
        {"EventName": "Cloud Computing Webinar", "EventDate": "2024-10-22", "Location": "Ahmedabad", "Category": "Webinar"},
    ]
    for i in event:
        Events.objects.create(
            EventName=i['EventName'],
            EventDate=date(int(i["EventDate"][:4]),int(i["EventDate"][5:7]),int(i["EventDate"][8:10])),
            Location=i['Location'],
            Category=i['Category']
    )
    return render(req,'base.html')