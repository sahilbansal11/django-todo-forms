## Recap

- Sqlite3 => schema and tables
- Django Models
- Django Shell
- Migrations
- Django Admin

## Django Forms

- Create our own view that displays a nice form
- Add, Edit these different objects

Why we need
- Say we want to display lists associated with tasks
- We cannot expose the entire administrator website to the end user
- Limited set of access to each user
- Custom views and forms
- Let's see how we can do it today.


### Show all the tasks page
1. views.py

```py
from .models import Task

def index(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/index.html', {'tasks': tasks})

```

2. urls for app and project
3. template in settings
4. create template

```html
<body>
  <h1>All Tasks</h1>
  <ul>
    {% for task in tasks %}
    <li>{{ task.name }}</li>
    {% endfor %}
  </ul>
</body>
```

### Create form to create a new task list

1. Create raw HTML form for adding task list
2. `action=''` => Date sent to the same URL, post request

CSRF verification failed
- Do not worry about it.
- Cross Site Request Forgery
- example 1: FB send message
- example 2: scaler submit problem API, you use on your website form action
- Security vulnerability, scaler should try to stop it
- People should not be able to submit problems on other's behalf without logging in
- Certain criteria should be satisfied

3. Add `csrf_token`
4. Show the details in the new task list error page.
5. Save the task

### Contact us Form
- Subject, message, your email
- name in the input tag maps to the one we fetch in the view
- email validation, earlier used type='text' change to 'email'
- Say if we need to add lot of other fields like cc, bcc, etc.
- Lot of manual work involved
- Not good design
- Django Forms provided that alleviates a lot of this pain

### Django Forms: Forms.py
- Form class inherits from `forms.Form`
- Validation should be on both sides, client and server
  - If not on server, user won't get proper feedback
  - If not on client side, someone can bypass and send wrong data
- Fields just like in model
- Create new view and new template
- Pass the form object in the context
- Need not create the HTML tags ourselves
- Use the {{ form }} variable
- No submit button
- View page source, only HTML, no action for form or submit button
- Main task of Django form to give this HTML
- For form to work, provide other HTML tags

## Customization
- Vertical form style of form: `{{ form.as_p }}`, block tag
- How to customize what HTML tag for what field
  - Meta class only for models
  - pass widget option in the field
  - can make it anything
  - but make sure it works well with the data type of the field
- Frontend errors, email validation, native in HTML5

## Submitting the form
- No longer need to get the data
- Can use the form object
- Data option
- Automatically fetches and validates all the fields

## Model Form
- Need not specify the details in model again
- ModelForm has no class specified error
- Django Created all the things for us
- Use model inside the meta class
- To include specific fields, update them as list in the fields attribute of meta
- Remove the created_at field
- Process the form in the view
- if form is valid save the object, automatically created, saved and returned:
```
if form.is_valid():
    new_task = form.save()
```
- Due date not valid, supposed to be a date
- Backend has caught this validation error
- All other fields should remain as it is, error should pop at right place
- Render the same form, it has all the data, and error for due_date
- Add widget for due_date

## Assignment Overview
- Assignment 2 followup
- Describe details for Assignment 3


## References
- Share docs link, available in extra reference material