from django.urls import path
from users.view import dashboard

"""
separating dashboard controller 
"""

url_lists = []

urlpatterns = [
    path('', dashboard.dashboard, name='dashboard.home'),
    path('book-slot', dashboard.book_slot, name='book_slot')
]
