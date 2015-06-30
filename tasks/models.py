from django.db import models
import datetime
from .days import Days

class CurrentTask(models.Model):

    task_type = models.CharField(max_length=255)
    frequency = models.CharField(max_length=50)
    person_in_charge = models.CharField(max_length=600)
    date_due = models.DateField('date due')

    def __unicode__(self):
        return self.task_type

    def is_due_today(self):
        return self.date_due == datetime.datetime.now().date()

    def is_due_two(self):
        return self.date_due == Days.two.date()

    def is_due_three(self):
        return self.date_due == Days.three.date()

    def is_due_four(self):
        return self.date_due == Days.four.date()

    def is_due_five(self):
        return self.date_due == Days.five.date()

    def is_due_six(self):
        return self.date_due == Days.six.date()

    def is_due_seven(self):
        return self.date_due == Days.seven.date()


