from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<int:my_args>', views.detail, name='detail'),
    path('test/', views.test, name='test')

    # 详情的意思
]







