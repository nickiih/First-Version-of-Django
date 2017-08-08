from django.conf.urls import url
from . import views
from .forms import ProductForm
def product_new(request):
    form = ProductForm()
    return render(request, 'blog/product_edit.html', {'form': form})

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^product/new/$', views.product_new, name='product_new'),
    url(r'^product/(?P<pk>\d+)/edit/$', views.product_edit, name='product_edit'),
    url(r'^Women-Empowerment$', views.original_page, name='original_page'),
]
