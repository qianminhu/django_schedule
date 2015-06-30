from django.shortcuts import render, redirect
from .models import CurrentTask
from .days import Days
import datetime
import logging
from django.contrib.auth.models import User
from datetime import datetime as date

class TaskTypeForm():
    pass


def index(request):
    task_list = CurrentTask.objects.order_by('-date_due')[:5]

    #today = Day().today
    #daytwo = Day().daytwo

    context = {'task_list': task_list}
    context['TaskTypeForm'] = TaskTypeForm
    context['today'] = EachDay().today
    context['daytwo'] = EachDay().daytwo
    context['daythree'] = EachDay().daythree
    context['dayfour'] = EachDay().dayfour
    context['dayfive'] = EachDay().dayfive
    context['daysix'] = EachDay().daysix
    context['dayseven'] = EachDay().dayseven
    return render(request, 'tasks/index.html', context)

# todo: add a class to add objects -- do i need a class?

def add(request):
    u = User.objects.get(email='andrew@eatwith.com')
    u.email
    person_in_charge=request.POST['person_in_charge']
    task_type=request.POST['task_type']
    frequency=request.POST['frequency']
    date_due=request.POST['date_due']
    logging.error("I AM HERE")
    CurrentTask.objects.create(
        person_in_charge=person_in_charge,
        task_type=task_type,
        frequency=frequency,
        date_due=date_due
    )
    return redirect('/tasks/')

class CheckWeek():
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    entries = CurrentTask.objects.filter(date_due__range=[start_week, end_week])

class EachDay():
#todo: change name of class and all accompanying "things"
    def __init__(self):

        self.current_month = Days.now.strftime("%B")

        #if for a month view, could write method that sets days = X to a variable that is passed depending on day

        self.today = Days.now.strftime("%A")

        self.daytwo = Days.two.strftime("%A")

        self.daythree = Days.three.strftime("%A")

        self.dayfour = Days.four.strftime("%A")

        self.dayfive = Days.five.strftime("%A")

        self.daysix = Days.six.strftime("%A")

        self.dayseven = Days.seven.strftime("%A")

"""class Day():
    def __init__(self, datetime):
        self.datetime = datetime

    def to_string(self):
        return self.datetime.strftime("%A")"""

#another possible way to write the name of week: date.today().strftime("%A")
#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior