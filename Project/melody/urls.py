from django.urls import path
from . import views

app_name='melody'
urlpatterns=[
    path('index/', views.MelodyIndexView.as_view(), name="melody_index_view"),
    path('registration/customer/', views.MelodyCustomerRegistrationView.as_view(), name="melody_customerRegistration_view"),
    path('dashboard/product/', views.MelodyProductDashboardView.as_view(), name="melody_productDashboard_view"),
    path('dashboard/customer/', views.MelodyCustomerDashboardView.as_view(), name="melody_customerDashboard_view"),
    path('registration/product/', views.MelodySongRegistrationView.as_view(), name="melody_songRegistration_view"),
]