from django.urls import path
from .views import *

urlpatterns = [
    path('', Homepage, name='home'),
    path('login/', LoginPage, name='login'),
    path('logout/', LogoutPage, name='logout'),
    path('testimonial/', TestimonialPage, name='testimonial'),
    path('testimoniallist/', TestimonialListPage, name='testimoniallist'),
    path('del_testimonial/<str:id>/', TestimonialDeletePage, name='del_testimonial'),
    path('del_contact/<str:id>/', ContactDeletePage, name='del_contact'),
]