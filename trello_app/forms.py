from django import forms
from trello_app.models import Task

class TaskListForm(forms.Form):
  name = forms.CharField(max_length=50)

class TaskForm(forms.ModelForm):
  # additional information / properties
  class Meta:
    # what model
    model = Task

    # what fields
    # fields = '__all__'
    fields = ['name', 'desc', 'due_date', 'list']

    # what additional features / UI
    widgets = {
      # input type
      # 'name': forms.EmailInput(),
      # 'due_date': forms.DateTimeInput(attrs = {'type': 'datetime-local'})
      'due_date': forms.DateTimeInput(attrs = {'type': 'datetime-local'})
    }

