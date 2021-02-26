from django import forms
from trello_app.models import Task

class TaskListForm(forms.Form):
  name = forms.CharField(max_length=50)

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'desc', 'due_date', 'list']
    widgets = {
      'due_date': forms.DateTimeInput(attrs= {'type': 'datetime-local'})
    }