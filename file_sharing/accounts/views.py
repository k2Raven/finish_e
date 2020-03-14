from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from .forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from accounts.models import Profile
from webapp.models import FileBase


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('webapp:index')

    else:
        form = UserCreationForm()
    return render(request, 'create.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if self.request.user == self.object:
                context['file_add'] = FileBase.objects.filter(author=self.request.user)
            else:
                context['file_add'] = FileBase.objects.filter(access='Common', author=self.request.user)
        else:
            context['file_add'] = FileBase.objects.filter(access='Common')
        return context




class UserPersonalInfoChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_info_change.html'
    form_class = UserChangeForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:login')


class UserIndexView(ListView):
    model = User
    template_name = 'accounts_list.html'
    form_class = UserChangeForm
    context_object_name = 'users_obj'