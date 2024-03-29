from django.shortcuts import render, redirect
from .models import Task, TaskList
from .forms import TaskListForm, TaskForm
# Create your views here.

def index(request):
  tasks = Task.objects.all()
  lists = TaskList.objects.all()
  return render(request, 'tasks/index.html', {'tasks': tasks, 'lists': lists})

def task_details(request, input_id):
  task_data = Task.objects.get(id=input_id)
  return render(request, 'tasks/task_detail.html', {'data': task_data})


def add_task(request):
  if request.method == 'POST':
    name = request.POST['name']
    desc = request.POST['desc']
    due_date = request.POST['due_date']
    task = Task(name=name, desc=desc, due_date=due_date)
    task.save()
    return redirect('index')
  else:
    return render(request, 'tasks/new_task.html')

def add_task_list(request):
  if request.method == 'POST':
    print(request.POST) # dictionary
    name = request.POST['name']
    task_list = TaskList(name=name)
    task_list.save()
    return redirect('index')
  else:
    return render(request, 'tasks/new_list.html')
  
def add_task_list_form(request):
  if request.method == 'POST':
    form = TaskListForm(data=request.POST)
    if form.is_valid():
      input_name = request.POST['name']

      print('form', form)
      print('name', input_name)

      # keyword argument
      task_list = TaskList(name=input_name)
      task_list.save()
      return redirect('index')
  else:
    form = TaskListForm()
    return render(request, 'tasks/forms/new_list.html', {'form': form})

def add_task_form(request):
  if request.method == 'POST':
    form = TaskForm(data=request.POST)

    print('-----------------------------')
    print('form before validation')
    print(form)
    print('-----------------------------')

    if form.is_valid():
      new_task = form.save()
      return redirect('index')
  else:
    form = TaskForm()
  
  print('-----------------------------')
  print('form after validation')
  print(form)
  print('-----------------------------')
  # if form not valid or if it's a get request we come to this part
  # for get request: print new form
  # for the post request: print the existing filled form
  return render(request, 'tasks/forms/new_task.html', {'form': form})