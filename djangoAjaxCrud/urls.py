from django.contrib import admin
from django.urls import path
from enroll.views import home
from enroll.views import save_data, delete_data, edit_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('save/', save_data, name='save'),
    path('delete/', delete_data, name='delete'),
    path('edit/', edit_data, name='edit'),
]
