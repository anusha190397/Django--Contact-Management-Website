from django.urls import path
from .views import Home, NewContactPage, ContactListView, EditContactView, DeleteContactView, ViewContactView


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('new-contact/', NewContactPage.as_view(), name='new_contact_page'),
    path('contact-list/', ContactListView.as_view(), name='contact_list'),
    path('edit-contact/<int:pk>/', EditContactView.as_view(), name='edit_contact'),
    path('delete-contact/<int:pk>/', DeleteContactView.as_view(), name='delete_contact'),
    path('view-contact/<int:pk>/', ViewContactView.as_view(), name='view_contact'),
]

