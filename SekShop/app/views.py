from django.shortcuts import render
from django.http import HttpResponse

from .models import Section, Category, Product

# Create your views here.
def home(req):
    sections = Section.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(req, "app/app.html", {
        "sections": sections,
        "categories": categories,
        "products": products
    })
    

def section(req, slug):
    sections = Section.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
         
    need_section = Section.objects.filter(slug=slug)
    
    for el in need_section:
        category_list = Category.objects.filter(section=el).all()
        categories_of_sextion_arr = []
        
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

    return render(req, "./app/category.html")


def product(req, slug):
    
    return render(req, "./app/product.html")