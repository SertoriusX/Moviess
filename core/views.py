from django.shortcuts import render
from is_admin.models import AdminShowcase,AdminLastMovies,AdminMovies
# Create your views here.
def frontpage(request):
   admin_showcase=AdminShowcase.objects.all()
   admin_last_movies=AdminLastMovies.objects.all()
   admin_movies=AdminMovies.objects.all()
   return render(request,'core/frontpage.html',{'admin_showcase':admin_showcase,'admin_last_movies':admin_last_movies,'admin_movies':admin_movies})


def views_showcase(request,pk):
    showcase = AdminShowcase.objects.get(id=pk)
 
    return render(request, 'core/views_showcase.html', {'showcase': showcase})
 

def views_lastmovies(request,pk):
    lastmovies = AdminLastMovies.objects.get(id=pk)
 
    return render(request, 'core/views_lastmovies.html', {'lastmovies': lastmovies})


def views_movies(request,pk):
    movies = AdminMovies.objects.get(id=pk)
    vtt_subtitle_url = movies.get_vtt_subtitle_url()

    return render(request, 'core/views_movies.html', {'movies': movies,'vtt_subtitle_url':vtt_subtitle_url})
 