from django.urls import path

from .views import SignUpView, home_page_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', home_page_view, name='home'),

]
