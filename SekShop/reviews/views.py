from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models

from app.models import Section
from .forms import ReviewForm, Review


# Create your views here.
def review (req):
    sections = Section.objects.all()
    
    if req.method == "POST":
        form = ReviewForm(req.POST)

        if form.is_valid():
            form.save()
        
        return HttpResponseRedirect('../')
        
    else:

        form = ReviewForm()

    return render(req, 'reviews/reviews.html', {
        "form": form,
        "sections": sections
        })
    
    
def review_list(req):
    sections = Section.objects.all()
    reviews = Review.objects.all()
    best_review = Review.objects.filter(rating=5)

    return render(req, 'reviews/reviews_list.html', {
        "reviews": reviews,
        "best_review": best_review,
        "sections": sections
        })
    