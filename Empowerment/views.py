from django.shortcuts import render
from django.utils import timezone
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect


# Create your views here.
def original_page(request):
    return render(request, 'Empowerment/finalproject.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'Empowerment/product_list.html', {'products':products})

def product_new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            print("yes form was valid")
            product = form.save(commit=False)
            product.save()
            return redirect('product_list')

    else:
        form = ProductForm()
    return render(request, 'Empowerment/product_edit.html', {'form': form})

def product_edit(requet, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            print("HEY YES IT WORKED")
            return redirect('product_detail', pk=product.pk)
        else:
            print("OH NO FORM NOT VALID")

    else:
        form = PostForm(instance=post)
    return render(request, 'Empowerment/product_edit.html', {'form':form})
