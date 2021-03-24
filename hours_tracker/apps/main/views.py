from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import *
from ..log_reg.models import User
# Create your views here.
def index(request):
    if 'logged_user' not in request.session:
        return redirect('/')
    else:
        context = {
            'logged_user': User.objects.get(id=request.session['logged_user']),
            'collections': Collection.objects.all(),
            'assignments': Assignment.objects.all(),

            # 'all_trips': Trip.objects.all(),
            # 'excluded_trips': Trip.objects.exclude(trips_joined=request.session['logged_user']),
        }
        test = Assignment.objects.all()
        print(test)
    return render(request, "main.html", context)


def add_collection(request):
    errors = Collection.objects.collection_validator(request.POST)

    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/main/index/')
    else:
        user = User.objects.get(id=request.session['logged_user'])
        this_collection = Collection.objects.create(
            name=request.POST['collection_name'],
            description=request.POST['description'],
            due_date=request.POST['due_date'],
            priority=request.POST['priority'],
            completed=request.POST.get('completed', False),
            creator=user,
        )
        return redirect('/main/index/')


def add_assignment(request):
    errors = Assignment.objects.assignment_validator(request.POST)

    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/main/index/')
    else:
        # possible Checkbox Bug Fix
        # if request.POST['completed'] = "on":
        #     completed=True


        user = User.objects.get(id=request.session['logged_user'])
        collection = Collection.objects.get(id=request.POST['collection'])
        this_assignment = Assignment.objects.create(
            creator=user,
            collection=collection,
            name=request.POST['assignment_name'],
            description=request.POST['description'],
            due_date=request.POST['due_date'],
            min_hours=request.POST['min_hours'],
            max_hours=request.POST['max_hours'],
            priority=request.POST['priority'],
            completed=request.POST.get('completed', False),
        )
        return redirect('/main/index/')
