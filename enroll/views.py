from django.shortcuts import render
from . forms import StudentRegistration
from . models import User
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

def home(request):
    form = StudentRegistration()
    students = User.objects.all()
    context = {'form': form, 'students': students}
    return render(request, 'enroll/home.html', context)

# @csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            student_id = request.POST.get('student_id')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            # When Edit button is not clicked
            if (student_id == ''):
                # Create new student object
                user = User(name=name, email=email, password=password)
            # When Edit button is clicked
            else:
                # Update Existing student object
                user = User(id =student_id, name=name, email=email, password=password)
            user.save()

            # Retrieve all students objects
            students = User.objects.values()
            print('students: ', students)
            # Convert Student queryset into list
            student_data = list(students)

            return JsonResponse({'status': 'Save', 
                'student_data': student_data})
        else:
            # return JsonResponse({'status': 'Fail'})
            return JsonResponse({'status':0})


def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('student_id')
        obj = User.objects.get(pk=id)
        obj.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status':0})


# Edit data
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('student_id')
        student = User.objects.get(pk=id)
        student_data = {
            'id': student.id, 
            'name': student.name,
            'email': student.email,
            'password': student.password
        }
        return JsonResponse(student_data)
