from django.shortcuts import render, get_object_or_404
from .models import Review


def review_list(request):
    context = {
        'review_list': Review.objects.all(),
    }
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, pk):
    context = {
        'review': get_object_or_404(Review, pk=pk)
    }
    return render(request, 'reviews/review_detail.html', context)
