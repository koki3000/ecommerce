from django.views.generic.edit import CreateView
from .. forms import UserForm
from django.contrib.auth.models import User
from django.shortcuts import render

# User Views

class CreateUser(CreateView):    
    model = User
    form_class = UserForm
    template_name = 'mysite/user_create_form.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        data = form.save(commit=False)
        data.set_password(data.password)
        data.save()
        return super(CreateUser, self).form_valid(form)


def contact_view(request):
    return render(request, 'mysite/contact.html')