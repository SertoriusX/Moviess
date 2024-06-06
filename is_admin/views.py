from django.shortcuts import render,redirect
from core.forms import UserForm
from is_user.forms import UserProfileForm
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout

#Login Page
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')  # Redirect to the home page after login
        else:
            # Handle invalid login
            return render(request, 'is_admin/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'is_admin/login.html')
#Log Out button
def user_logout(request):
    logout(request)
    return redirect('frontpage')  # Redirect to the home page after logout



#Create showcase movies
@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_create_showcase(request):
    if request.method == 'POST':
        form = AdminShowcaseForm(request.POST,request.FILES)
        if form.is_valid():
            showcase = form.save(commit=False)
            showcase.user = request.user
            showcase.save()
            return redirect('frontpage')
    else:
        form = AdminShowcaseForm()
    return render(request, 'is_admin/admin_create_showcase.html', {'form': form})




@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_update_showcase(request,pk):
    showcase = AdminShowcase.objects.get(id=pk)
    if request.method == 'POST':
        form = AdminShowcaseForm(request.POST,request.FILES,instance=showcase)
        if form.is_valid():
            showcase = form.save(commit=False)
            showcase.user = request.user
            showcase.save()
            return redirect('frontpage')
    else:
        form = AdminShowcaseForm(instance=showcase)
    return render(request, 'is_admin/admin_update_showcase.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_delete_showcase(request,pk):
    showcase = AdminShowcase.objects.get(id=pk)
    if request.method == 'POST':
        showcase.delete()
        return redirect('frontpage')
    return render(request, 'is_admin/admin_delete_showcase.html', {'showcase': showcase})
 
@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_views_showcase(request,pk):
    showcase = AdminShowcase.objects.get(id=pk)
 
    return render(request, 'is_admin/admin_views_showcase.html', {'showcase': showcase})
 
#User register form
@login_required
@user_passes_test(lambda u: u.is_admin)
def sing_up_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_user = True
            user.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()
            return redirect('frontpage')
    else:
        user_form = UserForm()
        profile_form     = UserProfileForm()
    return render(request, 'is_admin/sing_up_user.html', {'user_form': user_form, 'profile_form': profile_form})








#Create lastmovies movies
@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_create_lastmovies(request):
    if request.method == 'POST':
        form = AdminsLastMoviesForm(request.POST,request.FILES)
        if form.is_valid():
            lastmovies = form.save(commit=False)
            lastmovies.user = request.user
            lastmovies.save()
            return redirect('frontpage')
    else:
        form = AdminsLastMoviesForm()
    return render(request, 'is_admin/admin_create_lastmovies.html', {'form': form})



#last movies
@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_update_lastmovies(request,pk):
    lastmovies = AdminLastMovies.objects.get(id=pk)
    if request.method == 'POST':
        form = AdminsLastMoviesForm(request.POST,request.FILES,instance=lastmovies)
        if form.is_valid():
            lastmovies = form.save(commit=False)
            lastmovies.user = request.user
            lastmovies.save()
            return redirect('frontpage')
    else:
        form = AdminsLastMoviesForm(instance=lastmovies)
    return render(request, 'is_admin/admin_update_lastmovies.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_delete_lastmovies(request,pk):
    lastmovies = AdminLastMovies.objects.get(id=pk)
    if request.method == 'POST':
        lastmovies.delete()
        return redirect('frontpage')
    return render(request, 'is_admin/admin_delete_lastmovies.html', {'lastmovies': lastmovies})
 
@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_views_lastmovies(request,pk):
    lastmovies = AdminLastMovies.objects.get(id=pk)
 
    return render(request, 'is_admin/admin_views_lastmovies.html', {'lastmovies': lastmovies})
 



#Movies

@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_create_movies(request):
    if request.method == 'POST':
        form = AmdminsMoviesForm(request.POST,request.FILES)
        if form.is_valid():
            movies = form.save(commit=False)
            movies.user = request.user
            movies.save()
            return redirect('frontpage')
    else:
        form = AdminsLastMoviesForm()
    return render(request, 'is_admin/admin_create_movies.html', {'form': form})
@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_update_movies(request,pk):
    movies = AdminMovies.objects.get(id=pk)
    if request.method == 'POST':
        form = AmdminsMoviesForm(request.POST,request.FILES,instance=movies)
        if form.is_valid():
            movies = form.save(commit=False)
            movies.user = request.user
            movies.save()
            return redirect('frontpage')
    else:
        form = AmdminsMoviesForm(instance=movies)
    return render(request, 'is_admin/admin_update_movies.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_delete_movies(request,pk):
    movies = AdminMovies.objects.get(id=pk)
    if request.method == 'POST':
        movies.delete()
        return redirect('frontpage')
    return render(request, 'is_admin/admin_delete_movies.html', {'movies': movies})
 
@login_required
@user_passes_test(lambda u: u.is_admin)
def admin_views_movies(request,pk):
    movies = AdminMovies.objects.get(id=pk)
 
    return render(request, 'is_admin/admin_views_movies.html', {'movies': movies})
 