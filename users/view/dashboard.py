from django.shortcuts import render, redirect

"""
separating dashboard views 
"""

def dashboard(request):
    studentConfig = {
        'title': 'Student Dashboard',
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
    return render(request, 'dashboard/components/book-slot.html')
