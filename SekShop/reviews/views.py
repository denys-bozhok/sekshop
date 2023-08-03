from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.db import models

from app.models import Section
from .forms import ReviewForm, Review


# Create your views here.
class ReviewView(FormView):
    
    form_class = ReviewForm
    template_name = 'reviews/reviews.html'
    success_url = '../thank-you'
    
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class ThankYouView(TemplateView):
        template_name = 'reviews/thank_you.html'
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["msg"] = "Alright, pretty good!"
            
            return context
    
    
class ReviewList(ListView):
    template_name = 'reviews/reviews_list.html'
    model = Review
    context_object_name = "reviews"
    
    
class ReviewSingleView(ListView):
    template_name = 'reviews/review.html'
    model = Review
    context_object_name = "review"
