from django.shortcuts import render
from datetime import date

report = [
    {
        'rating' : 7, 
        'content' : 'I want to live',
        'date_posted' : date.today()
    },
    {
        'rating' : 2, 
        'content' : 'I want to die',
        'date_posted' :"September 2013"
    }
]
# Create your views here.
def home(request):
    history = {
        'reports' : report
    }
    return render(request, 'diary/home.html', history)
    # Render is a shortcut to call on the html template
    # 1st arguement is request and second is the directory followed by template name

def about(request):
    return render(request, 'diary/about.html')

def add_report(reports):
    user_rating = int(input("How do you feel out of 10? "))
    user_content = str(input("Why do you feel this way? "))
    report["rating"] = user_rating
    report["content"] = user_content
    report["date_posted"] = date.today()
