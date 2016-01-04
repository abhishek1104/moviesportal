from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from .models import movies
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from datetime import datetime

# Create your views here.


class IndexView(generic.ListView): #generic.ListView => Display list of objects!
    template_name='movies/index.html'
    context_object_name = 'thisweek_movies_released'

    def get_queryset(self):
        return movies.objects.filter(release_date__range = (timezone.now() - datetime.timedelta(days=7),timezone.now()).order_by('-release_date')[:5]


class MovieDetailView(generic.DetailView):

    model = movies
    template_name = 'movies/details.html'

    def get_queryset(self):
        return movies.objects.filter


def SelectMovieView(request,movies_id):
    p= get_object_or_404(movies,pk=movies_id)

