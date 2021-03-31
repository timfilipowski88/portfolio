from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import datetime
from .models import *
from ..log_reg.models import User

from django.http import JsonResponse

from django.views.generic import View
from django.views.generic import ListView

# Create your views here.
def index(View):
    def get(self, request):
        if 'logged_user' not in request.session:
            return redirect('/')
        else:
            context = {
                'logged_user': User.objects.get(id=request.session['logged_user']),
                'collections': Collection.objects.all().order_by("due_date"),
                'assignments': Assignment.objects.all().order_by("due_date"),

                # 'all_trips': Trip.objects.all(),
                # 'excluded_trips': Trip.objects.exclude(trips_joined=request.session['logged_user']),
            }
            test = Assignment.objects.all()
            print(test)
        return render(request, "base.html", context)

class add_assignment(View):
    def  get(self, request):
        user = User.objects.get(id=request.session['logged_user'])
        collection = Collection.objects.get(id=request.GET['collection_id'])
        this_assignment = Assignment.objects.create(
            creator=user,
            collection=collection,
            name=request.GET['assignment_name'],
            description=request.GET['description'],
            due_date=request.GET['due_date'],
            min_hours=request.GET['min_hours'],
            max_hours=request.GET['max_hours'],
            priority=request.GET['priority'],
            completed=request.GET.get('completed', False),
        )
        this_assignment.save()
        new_assignment = {
            'creator': this_assignment.creator.id,
            'collection': this_assignment.collection.name,
            'name': this_assignment.name,
            'description': this_assignment.description,
            'due_date': this_assignment.due_date,
            'min_hours': this_assignment.min_hours,
            'max_hours': this_assignment.max_hours,
            'priority': this_assignment.priority,
            'completed': this_assignment.completed,
        }
        data = {
            'new_assignment': new_assignment,
        }
        return JsonResponse(data)




# def get_collection_form(request):
#     context = {
#         'collections': Collection.objects.all().order_by("due_date"),
#     }
#     return render(request, 'collection_form.html', context)




# def get_assignment_form(request):
#     context = {
#         'assignments': Assignment.objects.all().order_by("due_date"),
#     }
#     return render(request, 'assignment_form.html', context)




# def add_collection(request):
#     errors = Collection.objects.collection_validator(request.POST)

#     if errors:
#         for k, v in errors.items():
#             messages.error(request, v)
#         return redirect('/main/index/')
#     else:
#         user = User.objects.get(id=request.session['logged_user'])
#         this_collection = Collection.objects.create(
#             name=request.POST['collection_name'],
#             description=request.POST['description'],
#             due_date=request.POST['due_date'],
#             priority=request.POST['priority'],
#             completed=request.POST.get('completed', False),
#             creator=user,
#         )
#         this_collection.save()
#         context = {
#             'collection': this_collection,
#         }
#         return render(request, "add_collection_form.html", context)




# def add_assignment(request):
#     errors = Assignment.objects.assignment_validator(request.POST)

#     if errors:
#         for k, v in errors.items():
#             messages.error(request, v)
#         return redirect('/main/index/')
#     else:
#         # possible Checkbox Bug Fix
#         # if request.POST['completed'] = "on":
#         #     completed=True
#         user = User.objects.get(id=request.session['logged_user'])
#         collection = Collection.objects.get(id=request.POST['collection_id'])
#         this_assignment = Assignment.objects.create(
#             creator=user,
#             collection=collection,
#             name=request.POST['assignment_name'],
#             description=request.POST['description'],
#             due_date=request.POST['due_date'],
#             min_hours=request.POST['min_hours'],
#             max_hours=request.POST['max_hours'],
#             priority=request.POST['priority'],
#             completed=request.POST.get('completed', False),
#         )
#         this_assignment.save()
#         context ={
#             'assignment': this_assignment
#         }
#         return render(request, 'add_assignment_form.html', context)




# def update_assignment(request, assignment_id):
#     errors = Assignment.objects.assignment_validator(request.POST)

#     if errors:
#         for k, v in errors.items():
#             messages.error(request, v)
#         return redirect('/main/index/')
#     else:
#         assignment_form = Assignment.objects.get(id=request.POST['assignment_id'])
#         new_collection_id = Collection.objects.get(id=request.POST['collection'])
#         assignment_form.collection=new_collection_id,
#         assignment_form.name=request.POST['assignment_name'],
#         assignment_form.description=request.POST['description'],
#         assignment_form.due_date=request.POST['due_date'],
#         assignment_form.min_hours=request.POST['min_hours'],
#         assignment_form.max_hours=request.POST['max_hours'],
#         assignment_form.priority=request.POST['priority'],
#         assignment_form.completed=request.POST.get('completed', False)
#         assignment_form.save()
#         success = True
#         console.log(success)
#         context = {
#             'assignments': Assignment.objects.all().order_by("due_date"),
#         }
#         return render(request, 'assignment_form.html', context)





# def update_collection(request):
#     pass

    