from django.shortcuts import render


def top(request):
    context = {
        'name': 'Snova',
    }
    return render(request, 'myprofile/top.html', context)


def resume(request):
    return render(request, 'myprofile/resume.html')

