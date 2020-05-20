from django.shortcuts import render
from .models import Diary


def top(request):
    context = {
        'diary_list': Diary.objects.all(),
    }
    return render(request, 'diary/diary_list.html', context)
