from django.shortcuts import render


def home_view(request):
    user = {
        'is_authenticated': True,
        'username': {
            'first_name': 'Barrack',
            'last_name': 'Amuyunzu'
        }
    }

    return render(request, 'home.html', {'user': user})
