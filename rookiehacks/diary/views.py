from django.shortcuts import render
import pprint
from datetime import date

pretty = pprint.PrettyPrinter(width=30, sort_dicts=False)
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

def add_report():
    new_dict = {}
    user_rating = int(input("How do you feel from 1-10? "))
    user_content = str(input("Why do you feel this way? "))
    new_dict["Rating"] = user_rating
    new_dict["Content"] = user_content
    new_dict["Date posted"] = date.today()
    report.append(new_dict)
    pretty.pprint(new_dict)

def show_report(report):
    pretty.pprint(report)