from django.urls import path, include

from . import views

app_name = "checklist"

urlpatterns = [ 
       # path('accounts/', include('django.contrib.auth.urls')),
        path('', views.index, name='index'),
#        path('date_select/', views.render_file, name='render_file'),
]
