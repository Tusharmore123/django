
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UpdateRegisterUser,UpdateProfile
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username') # type: ignore
            messages.success(request,f"Created User Successfully {username}")
            return redirect("blog-home")
    else:
        form=UserRegisterForm()

    return render(request,'Users/register.html',{'form':form})

@login_required
def profile(request):
    u_form=UpdateRegisterUser()
    p_form=UpdateProfile()
    context={
        'u_form':u_form,
        'p_form':p_form
    }


    return render(request,'Users/profile.html',context)

# Create your views here.
