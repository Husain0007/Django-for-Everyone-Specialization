## Set Up

Before you can start submitting the graded assignments you need to set up a student account on [Python Anywhere](https://www.pythonanywhere.com/).

Then follow [these instructions](https://www.dj4e.com/assn/dj4e_install.md) to set up the virtual development enviornment from the in-browser `bash` console on Python-Anywhere.

To view sample programs from the course git clone [this repository](https://github.com/csev/dj4e-samples).

### Enter Django3 Virtual Enviornment

``` 
workon django3 
```

### Create a New Project
```
django-admin startproject project_name
```

### Perform sanity check

The manage.py file picks up syntax errors in files and their linked files. It's a good sanity check when testing an application.

```
python manage.py check
```
