from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .models import Event, Ticket

# Create your views here.

def user_home(request):
    events = Event.objects.all().order_by('booking_start_date')
    tickets = Ticket.objects.filter(user=request.user)
    for event in events:
        event.is_booked_by_user = event.ticket_set.filter(user=request.user).exists()
    return render(request, 'user_home.html', {'events': events, 'tickets': tickets})


@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':

        ticket = Ticket.objects.create(event=event, user=request.user)
        return render(request, 'view_ticket.html', {'ticket': ticket})

    return render(request, 'book_event.html', {'event': event})


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    return render(request, 'view_ticket.html', {'ticket': ticket})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('user_home')
        else:
            messages.error(request, 'Invalid login credentials') 

    return render(request, 'login.html')


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after successful signup
            login(request, user)
            return redirect('user_home')  # Redirect to user home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
@staff_member_required
def admin_home(request):
    events = Event.objects.all().order_by('booking_start_date')
    return render(request, 'admin_home.html', {'events': events})


@csrf_exempt
@staff_member_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        event_type = request.POST.get('event_type')
        max_seats = request.POST.get('max_seats')
        booking_open = request.POST.get('booking_open')
        booking_start_date = request.POST.get('booking_start_date')
        booking_end_date = request.POST.get('booking_end_date')

        event = Event.objects.create(
            title=title,
            description=description,
            event_type=event_type,
            max_seats=max_seats,
            booking_open=booking_open,
            booking_start_date=booking_start_date,
            booking_end_date=booking_end_date,
        )

        return redirect('admin_home')
    else:
        return render(request, 'create_event.html')


# @login_required
# def list_events(request):
#     events = Event.objects.all().order_by('booking_start_date')
#     data = [{'id': event.id, 'title': event.title} for event in events]
#     return JsonResponse(data, safe=False)


@login_required
@staff_member_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        event.title = request.POST.get('title', event.title)
        event.description = request.POST.get('description', event.description)
        event.event_type = request.POST.get('event_type', event.event_type)
        event.max_seats = request.POST.get('max_seats', event.max_seats)
        event.booking_open = request.POST.get('booking_open', event.booking_open)
        event.booking_start_date = request.POST.get('booking_start_date', event.booking_start_date)
        event.booking_end_date = request.POST.get('booking_end_date', event.booking_end_date)
        event.save()

        return redirect('admin_home')
    else:
        return render(request, 'update_event.html', {'event': event})


@login_required
def view_summary(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event not found.'}, status=404)

    summary = {
        'title': event.title,
        'description': event.description,
        'total_seats': event.max_seats,
        'available_seats': event.max_seats - event.ticket_set.count(),
    }

    return JsonResponse(summary)

