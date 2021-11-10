from django.shortcuts import render, redirect

"""
separating dashboard views 
"""


def dashboard(request):
    current_component = request.GET.get('c', '')
    studentConfig = {
        'title': 'Student Dashboard',
        'current_component': current_component,
        'dashboard': {
            'title': 'Team Utilization Dashboard',
            'sidebar': [
                {'title': 'Book a Slot', 'url': 'book-slot'},
                {'title': 'Revisit Session', 'url': 'revisit-session'},
                {'title': 'Complete Curriculum', 'url': '#'},
                {'title': 'Select a Mentor', 'url': '#'},
                {'title': 'Shop', 'url': '#'}
            ]
        }
    }

    mentorConfig = {
        'title': 'Mentor Dashboard',
        'current_component': current_component,
        'dashboard': {
            'title': 'Team Utilization Dashboard',
            'sidebar': [
                {'title': 'Add Slot', 'url': '#'},
                {'title': 'My Students', 'url': '#'},
                {'title': 'Complete Curriculum', 'url': '#'},
            ]
        }
    }
    # TODO add condition to check either current user is Mentor/Student
    # and based on that send config to frontend.
    # For now fetching mentor flag from Url query params
    if request.GET.get('mentor', ''):
        config = mentorConfig
    else:
        config = studentConfig
    return render(request, 'dashboard/components/main.html', config)


def book_slot(request):
    config = {
        'dashboard':{
        'current_section':'Book a Slot',
        },
        'slots': [
            1, 2, 3, 4, 5, 6
        ]
    }
    return render(request, 'dashboard/components/book-slot.html', config)
