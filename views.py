from django.shortcuts import render, get_object_or_404
from .models import movie, TechType, Review 
from .forms import MovieForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'movie/index.html')

def movies(request):
  movie_list=movie.objects.all()
  return render(request, 'movie/movie.html', {'movie_list': movie_list})

def movieDetail(request, id):
  movie=get_object_or_404(movie, pk=id)
  return render(request, 'movie/moviedetail.html', {'movie' : movie})

@login_required
def newMovie(request):
  form=MovieForm

  if request.method=='POST':
    Form=MovieForm(request.POST)

  if form_is.valid():     
    post=form.save(commit=True)
    post.save()
    form=MovieForm()

  else:
    form=MovieForm()
  return render(request, 'movie/newmovie.html', {': form'})

def loginmessage(request):
  return render(request, 'movie/loginmessage.html')


def logoutmessage(request):
  return render(request, 'movie/logoutmessage.html')