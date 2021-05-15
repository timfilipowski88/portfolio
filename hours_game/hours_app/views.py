from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import datetime
from django.views.generic import ListView
from .models import Collection, Assignment, User
from django.http import JsonResponse
from django.views.generic import View
import bcrypt



def log_reg(request):
    return render(request, 'log_reg.html')

def register(request):
    errors = User.objects.registration_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email_address = request.POST['email_address'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['logged_user'] = user.id
        return redirect('/context/')


def login(request):
    errors = User.objects.login_validator(request.POST)

    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        user = User.objects.get(email_address=request.POST['email_address'])
        request.session['logged_user'] = user.id
        return redirect('/context/')


def context(request):
    logged_user = User.objects.get(id=request.session['logged_user'])
    due_date = str(logged_user.due_date)
    if due_date:
        days_available = logged_user.days_available
        incomplete_assignments = Assignment.objects.filter(completed=False)
        max_hours = 0
        min_hours = 0
        for assignment in incomplete_assignments:
            if str(assignment.due_date) <= due_date:
                max_hours += assignment.max_hours
                min_hours += assignment.min_hours

        # date_difference = due_date.days - date_now.days
        # if date_difference.days == 0:
        #     date_difference.days += 1

        min_avg = min_hours / int(days_available)
        max_avg = max_hours / int(days_available)
        mid_avg = (max_avg + min_avg) / 2
        mid_avg = round(mid_avg, 1)
        min_avg = round(min_avg)
        max_avg = round(max_avg)
        completed_max = 0
        completed_min = 0
        completed_assignments = Assignment.objects.filter(completed=True).order_by("-due_date")
        incomplete_assignments = Assignment.objects.filter(completed=False).order_by("due_date")
        collections = Collection.objects.all()
        for assignment in completed_assignments:
            completed_max += assignment.max_hours
            completed_min += assignment.min_hours
        context = {
            'completed_assignments': completed_assignments,
            'incomplete_assignments': incomplete_assignments,
            'collections': collections,
            'min_total': min_hours,
            'max_total': max_hours,
            'min_avg': min_avg,
            'max_avg': max_avg,
            'mid_avg': mid_avg,
            'completed_min': completed_min,
            'completed_max': completed_max,
            'due_date': str(due_date),
            'days_available': days_available,
            'logged_user': User.objects.get(id=request.session['logged_user'])
        }
        return render(request, 'assignment.html', context)
    else:
        completed_assignments = Assignment.objects.filter(completed=True).order_by("due_date")
        incomplete_assignments = Assignment.objects.filter(completed=False).order_by("due_date")
        collections = Collection.objects.all()
        context = {
            'completed_assignments': completed_assignments,
            'incomplete_assignments': incomplete_assignments,
            'collections': collections,
        }
        return render(request, 'assignment.html', context)




def add_collection(request):
    errors = Collection.objects.collection_validator(request.POST)

    if errors:
        for k, v in errors.items():
            messages.error(request, v)
            # messages.info('Check form for error messages')

        return redirect('/context/')
    else:
        user = User.objects.get(id=request.session['logged_user'])
        this_collection = Collection.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            # due_date=request.POST['due_date'],
            priority=request.POST['priority'],
            # completed=request.POST.get('completed', False),
            creator=user,
        )
        this_collection.save()
        context = {
            'collection': this_collection,
        }
        return redirect('/context/')


def add_assignment(request):
    errors = Assignment.objects.assignment_validator(request.POST)

    if errors:
        for k, v in errors.items():
            messages.error(request, v)
            # messages.info('Check form for error messages')

        return redirect('/context/')
    else:
        # possible Checkbox Bug Fix
        # if request.POST['completed'] = "on":
        #     completed=True
        user = User.objects.get(id=request.session['logged_user'])
        collection = Collection.objects.get(id=request.POST['collection_id'])
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
        this_assignment.save()
        context ={
            'assignment': this_assignment
        }
        return redirect('/context/')

def update_assignment(request, id):
    collection = Collection.objects.get(id=request.POST['collection_id'])
    assignment = Assignment.objects.get(id=id)
    assignment.collection = collection
    assignment.name=request.POST['assignment_name']
    assignment.description=request.POST['description']
    assignment.due_date=request.POST['due_date']
    assignment.min_hours=request.POST['min_hours']
    assignment.max_hours=request.POST['max_hours']
    assignment.priority=request.POST['priority']    
    # assignment.completed=request.POST.get('completed', False)
    assignment.save()
    return redirect('/context/')


def update_collection(request, id):
    collection = Collection.objects.get(id=id)
    collection.name=request.POST['collection_name']
    collection.description=request.POST['description']
    collection.priority=request.POST['priority']    
    # collection.completed=request.POST.get('completed', False)
    collection.save()
    return redirect('/context/')


def delete_assignment(request, id):
    assignment = Assignment.objects.get(id=id)
    assignment.delete()
    return redirect('/context/')

def delete_collection(request, id):
    collection = Collection.objects.get(id=id)
    collection.delete()
    return redirect('/context/')

def change_complete(request, id):
    assignment = Assignment.objects.get(id=id)
    if assignment.completed == True:
        assignment.completed = False
    else:
        assignment.completed = True
    assignment.save()
    return redirect('/context/')



def calculate_hours(request):
    logged_user = User.objects.get(id=request.session['logged_user'])
    logged_user.due_date = request.POST['due_date']
    logged_user.days_available = request.POST['days_available']
    logged_user.save()
    return redirect('/context/')

    # date_now = datetime.now()
    # incomplete_assignments = Assignment.objects.filter(completed=False)
    # for assignment in incomplete_assignments:
    #     if assignment.due_date < due_date:
    #         max_hours += assignment.max_hours
    #         min_hours += assignment.min_hours
    # date_difference = due_date - date_now
    # min_avg = min_hours / date_difference.days
    # max_avg = max_hours / date_difference.days
    # request.session['min_total'] = min_hours
    # request.session['max_total'] = max_hours
    # request.session['min_avg'] = min_avg
    # request.session['max_avg'] = max_avg
    # request.session['due_date'] = due_date


# class AssignmentView(ListView):
#     model = Assignment
#     template_name = 'assignment.html'
#     context_object_name = 'assignments'

#     def get_context_data(self, **kwargs):
#         all_collections = Collection.objects.all()
#         # Call the base implementation first to get the context
#         context = super(AssignmentView, self).get_context_data(**kwargs)
#         # Create any data and add it to the context
#         context['collections'] = all_collections
#         return context

# class UpdateAssignment(View):
#     def  get(self, request):
#         user = User.objects.get(id=request.session['logged_user'])
#         collection = Collection.objects.get(id=request.GET['collection_id'])
#         this_assignment = Assignment.objects.create(
#             creator=user,
#             collection=collection,
#             name=request.GET['assignment_name'],
#             description=request.GET['description'],
#             due_date=request.GET['due_date'],
#             min_hours=request.GET['min_hours'],
#             max_hours=request.GET['max_hours'],
#             priority=request.GET['priority'],
#             completed=request.GET.get('completed', False),
#         )
#         this_assignment.save()
#         new_assignment = {
#             'creator': this_assignment.creator.id,
#             'collection': this_assignment.collection.name,
#             'name': this_assignment.name,
#             'description': this_assignment.description,
#             'due_date': this_assignment.due_date,
#             'min_hours': this_assignment.min_hours,
#             'max_hours': this_assignment.max_hours,
#             'priority': this_assignment.priority,
#             'completed': this_assignment.completed,
#         }
#         data = {
#             'new_assignment': new_assignment,
#         }
#         return JsonResponse(data)


# class AssignmentDelete(View):
#     def  get(self, request):
#         id1 = request.GET.get('id', None)
#         Assignment.objects.get(id=id1).delete()
#         data = {
#             'deleted': True
#         }
#         return JsonResponse(data)




# class AddAssignment(View):
#     def  get(self, request):
#         user = User.objects.get(id=request.session['logged_user'])
#         collection = Collection.objects.get(id=request.GET['collection_id'])
#         this_assignment = Assignment.objects.create(
#             creator=user,
#             collection=collection,
#             name=request.GET['assignment_name'],
#             description=request.GET['description'],
#             due_date=request.GET['due_date'],
#             min_hours=request.GET['min_hours'],
#             max_hours=request.GET['max_hours'],
#             priority=request.GET['priority'],
#             completed=request.GET.get('completed', False),
#         )
#         this_assignment.save()
#         new_assignment = {
#             'creator': this_assignment.creator.id,
#             'collection': this_assignment.collection.name,
#             'name': this_assignment.name,
#             'description': this_assignment.description,
#             'due_date': this_assignment.due_date,
#             'min_hours': this_assignment.min_hours,
#             'max_hours': this_assignment.max_hours,
#             'priority': this_assignment.priority,
#             'completed': this_assignment.completed,
#         }
#         data = {
#             'new_assignment': new_assignment,
#         }
#         return JsonResponse(data)
