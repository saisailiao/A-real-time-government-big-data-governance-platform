from django.urls import path
from Login import views
urlpatterns = [
    path('',views.login_view),
    path('View/',views.login_view),
    path('Logout/',views.logout_view),
    path('Register/',views.register),

]