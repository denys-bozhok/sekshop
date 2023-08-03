from random import randint

from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

from reviews.models import Review
from .models import Section, Category, Product

# Create your views here.

def home(req):
    sections = Section.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    reviews = Review.objects.all()
    
    random_reviews_list = []
    reviews_length = len(reviews)
    
    i = 0
    while i < 3:
        try:
            random_reviews_list.append(reviews[randint(0, reviews_length - 1)])
        except:
            break
        i += 1
 

    return render(req, "app/app.html", {
        "sections": sections,
        "categories": categories,
        "products": products,
        "random_reviews_list": random_reviews_list
    })
    

def section(req, slug):
    sections = Section.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    categories_of_sextion_arr = []
    need_section = Section.objects.filter(slug=slug)
    
    for el in need_section:
        category_list = Category.objects.filter(section=el).all()
        
    for category in category_list:
        categories_of_sextion_arr.append(category)
    
    return render(req, "app/section.html", {
        "sections": sections,
        "categories": categories,
        "products": products,
        "categories_of_sextion_arr": categories_of_sextion_arr,
        "need_section": need_section
    })


def category(req, slug):
    sections = Section.objects.all()
    categories = Category.objects.all()
    need_category= Category.objects.filter(slug=slug)
    
    for el in need_category:
        products_list = Product.objects.filter(category=el).all()
    
    print(products_list)
    
    return render(req, "./app/category.html", {
        "sections": sections,
        "categories": categories,
        "products_list": products_list
    })


def product(req, slug):
    need_product = Product.objects.filter(slug=slug)
    sections = Section.objects.all()
    categories = Category.objects.all()
    
    return render(req, "./app/product.html", {
        "need_product": need_product,
        "sections": sections,
        "categories": categories
    })