from django.views.generic import UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from users.models import Profile


class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # There will only be one profile made as this is for a personal website
        user_profile = Profile.objects.all().first()
        context['user_profile'] = user_profile
        context['user_urls'] = user_profile.url_set.all()
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['name', 'image', 'about']
    login_url = 'login'

