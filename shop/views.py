from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.


def shop(request):
    shop = Category.objects.all()
    return render(request, 'shop/shop.html', {'shop': shop})


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category'


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'shop/create.html'

    form_class = CategoryForm


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/shop'
    template_name = 'shop/delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'There was an error creating the category.'

    form = CategoryForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'shop/create.html', data)
