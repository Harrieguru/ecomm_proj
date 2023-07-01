from django.shortcuts import render, redirect
from .models import Category, Profile
from .forms import ProductForm, ProfileForm

# Create your views here.

def home(request):

    return render(request,'base.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories_list.html',{'categories':categories})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html',{'form':form})

def profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    
    context = {
        'admin_name': request.user.username,
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile.html',context)
            

