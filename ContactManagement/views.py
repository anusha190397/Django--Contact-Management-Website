from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Contact
from .forms import ContactForm
from django.utils import timezone

class Home(View):
    def get(self, request):
        columns = {
            'Contact Name': [],
            'Email': [],
            'Created Time': [],
        }
        return render(request, 'ContactManagement/home.html', {'columns': columns})

class NewContactPage(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'ContactManagement/new_contact_page.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list') 
        return render(request, 'ContactManagement/new_contact_page.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.cleaned_data['created_time'] = timezone.now()
            form.save()
            return redirect('contact_list')
        return render(request, 'ContactManagement/new_contact_page.html', {'form': form})

class ContactListView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'ContactManagement/contact_list.html', {'contacts': contacts})

    def post(self, request):
        contact_id = request.POST.get('contact_id')
        action = request.POST.get('action')

        if action == 'view':
            return redirect('contact_detail', pk=contact_id)
        elif action == 'delete':
            contact = get_object_or_404(Contact, pk=contact_id)
            contact.delete()
            return redirect('contact_list')
        else:
            return redirect('contact_list')

class EditContactView(View):
    def get(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(instance=contact)
        return render(request, 'ContactManagement/edit_contact.html', {'form': form, 'contact': contact})

    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
        return render(request, 'ContactManagement/edit_contact.html', {'form': form, 'contact': contact})

class DeleteContactView(View):
    def get(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        return render(request, 'ContactManagement/delete_contact.html', {'contact': contact})

    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        contact.delete()
        return redirect('contact_list')

class ViewContactView(View):
    def get(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        return render(request, 'ContactManagement/view_contact.html', {'contact': contact})
