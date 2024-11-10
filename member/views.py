from .forms import EventForm  # 確保您的 forms.py 中有這個類
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from events.models import Registration, Event
from django.contrib.auth.decorators import login_required

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('event_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    registrations = Registration.objects.filter(user=user).select_related('event')

    if user.is_superuser:
        # If the user is an admin, show the admin dashboard content
        return admin_dashboard(request)  # Redirect to the admin dashboard
    else:
        # For regular members, show their profile information and registered events
        return render(request, 'member/profile.html', {
            'user': user,
            'registrations': registrations
        })

@login_required  # Ensure only logged-in users can access
def admin_dashboard(request):
    events = Event.objects.all()  # Fetch all events
    registrations = Registration.objects.all()  # You can modify the filter as needed
    return render(request, 'member/admin_dashboard.html', {
        'events': events,
        'registrations': registrations
    })

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redirect to the admin dashboard after creating an event
    else:
        form = EventForm()
    return render(request, 'member/create_event.html', {'form': form})

