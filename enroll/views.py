from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegisterationform
from .models import User

# Create your views here.


def add_show(request):
    if request.method == 'POST':
        fm = StudentRegisterationform(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data.get('name')
            em = fm.cleaned_data.get('email')
            ps = fm.cleaned_data.get('password')
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            fm = StudentRegisterationform()
    else:
        fm = StudentRegisterationform()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm,
                                                      'st': stud})


def updatestudent(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegisterationform(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegisterationform(instance=pi)

    return render(request, 'enroll/updatestudent.html', {'form': fm})


def delete(request, id):
    if request.method == 'POST':
        try:
            # Retrieve the User object with the specified ID (pk)
            pi = User.objects.get(pk=id)
        except User.DoesNotExist:
            # Handle the case where the User object does not exist
            # Redirect or display an error message
            return HttpResponseRedirect('/')  # Redirect to the homepage

        # Delete the retrieved User object
        pi.delete()

        # Redirect the user to the homepage after deletion
        return HttpResponseRedirect('/')