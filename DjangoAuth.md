## Recap

1. Model, class => table, fields => columns
2. Run the migrations
3. Shell => create and query data
4. Django Admin
5. Django Forms => Model Forms

## Django Forms

- Something that should not be exposed to end users of app
- Our own forms to add data to the tables

1. Display all the lists
2. Form for creating a new list using Django Form
3. Form for creating a new task using Django Model Form

## Code for Class

[https://github.com/sahilbansal11/django_todo_app](https://github.com/sahilbansal11/django_todo_app)

-----------------------------------------------------------------------------

## Django Authentication
- Login pages
- Making sure only logged in users can add task lists and tasks

### Create pages app
- Has home, about and dashboard in the `pages` app
- Rendered from template directly, `TemplateView.as_view`

- Home: Login, Signup, 2 links

## Create accounts app
- Currently, tasklists and tasks exist independently of the user
- we want tasks and lists to be personal to the users in our app
- Create: `accounts` application
- Add to installed_apps

# Login, Register and Logout Functionality

## Auth Apps included in Django
- User model provided in django very robust, works for most of the requirements
- Form for user creation
- `from django.contrib.auth.models import User`
- `from django.contrib.auth.forms import UserCreationForm`

## Views register method

```py
def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
  else:
    form = UserCreationForm()
  return render(request, 'accounts/register.html', {'form': form})
```

- Register template, Form as table
- Inherit from user creation form to customize it, add the email field
- After completion, redirect to login page

## Login method
- Login form frontend
- Login form backend
  - find if such user exists
  - login that user
  - redirect to the dashboard
- Password never stored as it is, convered to hash, salt added
- authenticate and auth_login

```py
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      auth_login(request, user)
      return redirect('dashboard')
    else:
      messages.error(request, 'Username or password is incorrect')
```

## Logout functionality

```py
def logout(request):
  auth_logout(request)
  return redirect('login')

```

## Extra Links
- Login page for register
- Register page for login
- Home page for login and sign up

## User logged in state
- Home page should show logout
- if request.user.is_authenticated => logout page, otherwise => login and signup
- Moving to templates, DRY principle

## Dashboard Page
- username => {{ request.user }}
- Get task lists and tasks
- Similar for all of them right now
- Not associated with any user object as of now
- Task List model
  - `user = models.ForeignKey(User, on_delete=models.CASCADE)`
- Create fresh data, drop db.sqlite3 and remove earlier migrations
- not logged in user should not be able to go to the dashboard
  - `from django.contrib.auth.decorators` import login_required
  - `@login_required(login_url='login')`
  - similar for add_tasks, add_task_lists
- Get lists and tasks for the user
  - `user = request.user`
  - `lists = user.task_list_set.all()`
  - `tasks = Task.objects.filter(list: lists)` ??

## Redirections
- if logged in, on login and register page back to dashboard
- `if request.user.is_authenticated`

## Associate user with task list
- `form.instance.user = request.user`
