from django.shortcuts import render
from .models import Student


# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def blank(request):
    return render(request,'blank.html')

def MI(request):
    ss = {
        'name': 'Rohit Sharma',
        'titles_won': 5,
        'finals': [

                    {
                        'year': 2013,
                        'player': 'Kieron Pollard',
                        'opposite_team': 'Chennai Super Kings',
                        'opposite_captain': 'MS Dhoni',
                        'won_by': '23 Runs',
                        'mi_score': '148/9',
                        'oppo_score': '125/9',
                        'diff': 23
                    },

                    {
                        'year': 2015,
                        'player': 'Rohit Sharma',
                        'opposite_team': 'Chennai Super Kings',
                        'opposite_captain': 'MS Dhoni',
                        'won_by': '41 Runs',
                        'mi_score': '202/5',
                        'oppo_score': '161/8',
                        'diff': 41
                    },

                    {
                        'year': 2017,
                        'player': 'Krunal Pandya',
                        'opposite_team': 'Rising Pune Supergiant',
                        'opposite_captain': 'Steve Smith',
                        'won_by': '1 Run',
                        'mi_score': '129/8',
                        'oppo_score': '128/6',
                        'diff': 1
                    },

                    {
                        'year': 2019,
                        'player': 'Jasprit Bumrah',
                        'opposite_team': 'Chennai Super Kings',
                        'opposite_captain': 'MS Dhoni',
                        'won_by': '1 Run',
                        'mi_score': '149/8',
                        'oppo_score': '148/7',
                        'diff': 1
                    },

                    {
                        'year': 2020,
                        'player': 'Trent Boult',
                        'opposite_team': 'Delhi Capitals',
                        'opposite_captain': 'Shreyas Iyer',
                        'won_by': '5 Wickets',
                        'mi_score': '157/5',
                        'oppo_score': '156/7',
                        'diff': 1
                    }
                ]
    }
    return render(request,'MI.html',{ 'ss': ss })

def GT(request):
    return render(request,'GT.html')

def CSK(request):
    return render(request,'CSK.html')

def get(request):
    return render(request,'get.html')

def show(request):
    n=request.GET.get('name')
    email=request.GET.get('email')
    age=request.GET.get('age')
    Student.objects.create(name=n,email=email,age=age)
    return render(request,'show.html',{'name':n,'email':email,'age':age})

def db(request):
    ob=Student.objects.all()
    return render(request,'db.html',{'students':ob})