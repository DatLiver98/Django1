from django.urls import path, include #tao duong dan path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('solutions/', views.solutions, name='solutions'),
    path('partner/', views.partner, name='partner'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('product/', views.product, name='product'),
    path('blog/', include('blog.urls')),

    

    
]