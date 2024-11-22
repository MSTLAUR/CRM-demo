"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import home_page_view, single, form_submit, checkout
#from students import views as students_views
from teachers import views as teachers_views
from EcomProducts import views as Ecom_views
from students import views as student_views
from dashboard.main import views as dasboard_views
from django.contrib.auth import views as authentication_views



urlpatterns = [
    path('', home_page_view, name='home'), 
    path('home', home_page_view, name='home'), 
    path('admin/', admin.site.urls),
    #/ecom prod detail single page
    path('EcomProducts/<int:item_id>/', single, name='item'),  # Update view reference to 'views.single'
    path('form',form_submit, name='submit_form'),
    #path('register/',students_views.register, name='register' ),
    #path('register/',students_views.register, name='register' ),
    path('register/', teachers_views.register_Teacher, name='register'),
   # path('teachers/welcome.html/', teachers_views.registerTeacher, name='register'),
    path('login/',teachers_views.login_teachers, name='login' ),
    path('logout/',teachers_views.logout_teachers, name='logout' ),
    path('welcome/',teachers_views.teachersDashboard,name='welcome'),
   # path('dashboard/',dasboard_views.dashboard,name='dashboard'),
    path('ecomproducts/', include('EcomProducts.urls')),
    path('students/', include('students.urls')),
    #path('dashboard/main/', include('dashboard.main.urls')),     # Routes to dashboard/main/urls.py
    #path('dashboard/vristo/', include('dashboard.vristo.urls')), # Routes to dashboard/vristo/urls.py
    path('checkout/',checkout, name='checkout' ),

    


]

#CLAUDE ADDED THIS
# if settings.DEBUG:
  #  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)