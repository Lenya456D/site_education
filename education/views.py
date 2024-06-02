from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView

from education.models import EducationsLinks, Category
from education.utils import DataMixin

# Create your views here.


class MainPage(DataMixin, ListView):
    model = EducationsLinks
    template_name = "education/index.html"
    title_page = "Главная страница"
    paginate_by = 4
    category = Category.objects.all()

    def get_queryset(self):
        return EducationsLinks.objects.all().order_by('id')


class ShowCategory(DataMixin, ListView):
    model = EducationsLinks
    template_name = 'education/show_category.html'
    paginate_by = 4
    title_page = 'Категории'
    category = Category.objects.all()

    def get_queryset(self):
        return EducationsLinks.objects.filter(cat__slug=self.kwargs['cat_slug'])


class Search(DataMixin, ListView):
    model = EducationsLinks
    template_name = 'education/index.html'
    title_page = 'Поиск'
    category = Category.objects.all()
    paginate_by = 4

    def get_queryset(self):
        return EducationsLinks.objects.filter(title__iregex=self.request.GET.get('search'))
