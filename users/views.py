from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import CustomUserCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request,'registration/register.html',context=context)

