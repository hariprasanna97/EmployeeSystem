from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import EmployeeInfo
from django.template import loader
from .forms import AddEmployeeForm,EmailForm
from django.core.mail import send_mail
from django.conf import settings

def email_employee(request):
    form = EmailForm(request.POST or None)
    if form.is_valid():
        subject = "Thank you for signing up"
        message = "Welcome to the website"
        from_email = settings.EMAIL_HOST_USER
        to_email = [form.cleaned_data['to_email']] #data is captured into a list
        print(to_email)
        send_mail(subject=subject, message = message, from_email = from_email , recipient_list = to_email,
                        fail_silently = False)
    return render(request, 'Employee/send_email.html', {'form': form})

def add_employee(request):
    form = AddEmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return render(request, 'Employee/index.html', {'form': form})
    else:
        # return HttpResponseRedirect('not valid data')
        print(form.errors)
    return render(request, 'Employee/employee_add_form.html', {'form': form})


def index(request):
    latest_employee_list = EmployeeInfo.objects.all()
    # output = ', '.join([q.first_name + q.last_name for q in latest_employee_list ])
    # return HttpResponse(output)
    template = loader.get_template('Employee/index.html')
    context = {
        'latest_employee_list': latest_employee_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'Employee/index.html', context)


def detail(request, employee_id):
    single_employee = get_object_or_404(EmployeeInfo, pk=employee_id)

    return render(request, 'Employee/detail.html', {'single_employee': single_employee})
    # return HttpResponse("You're looking at employee %s." % employee_id)
