from django.shortcuts import  render, redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Songs,Artists,Rating
from django.db.models import Avg,Count
import json
from django.contrib.auth.decorators import login_required



def register_request(request):
    form = RegistrationForm(request.POST or None)
    print(form.errors)
    if form.is_valid():
        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        new_user = form.save(commit=False)
        new_user.save()
        messages.success(request,'Successfully Registered.')
        return redirect("deltax_frontend:songs")
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
        except:
            user=None
            messages.error(request,f"Are you sure you are registered? We cannot find this user.")
        if user is not None and not user.check_password(password):
            if password is None:
                messages.error(request, f'Field is required')
            messages.error(request,f"Invalid Passsword")
        elif user is None:
            pass
        else:
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Successfully Logged In. Welcome!!')
            #user.emailconfirmed.active_user_email()
            return redirect("deltax_frontend:songs")
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request,'Login.html',context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out. Feel free to login again')
    return redirect('deltax_frontend:login')

@login_required
def Songs_page(request):
    all_songs = Songs.objects.all()
    lst=[]
    sorted_lst = sorted(Rating.objects.all().values_list('song').annotate(Avg('rating')))
    sorted_lst.sort(reverse=True,key=lambda a:a[1])
    for i in sorted_lst:
        lst.append(i[0])
    objects = Songs.objects.filter(id__in=lst)
    all_songs1 = sorted(objects, key=lambda i: lst.index(i.pk))
    for i in all_songs:
        if i in all_songs1:
            continue
        else:
            all_songs1.append(i)
    context = {'all_songs':all_songs1[:10]}
    return render(request,'Songs.html',context=context)

@login_required
def artists_page(request):
    all_songs = Songs.objects.all()
    lst = []
    sorted_lst = sorted(Rating.objects.all().values_list('song').annotate(Avg('rating')))
    sorted_lst.sort(reverse=True, key=lambda a: a[1])
    for i in sorted_lst:
        lst.append(i[0])
    objects = Songs.objects.filter(id__in=lst)
    all_songs1 = sorted(objects, key=lambda i: lst.index(i.pk))
    for i in all_songs:
        if i in all_songs1:
            continue
        else:
            all_songs1.append(i)
    top_ten_artists=[]
    for i in range(len(all_songs1)):
        for j in list(all_songs1[i].artists.values().distinct()):
            if j not in lst:
                top_ten_artists.append(j)
            else:
                continue
    all_artists = Artists.objects.all()
    artist_name = []
    user = get_user_model()
    artist_details = {}
    artist_details_full = []
    if request.method=='POST':
        print(request.method)
    for i in top_ten_artists:
        artist_name.append((i['name'],i['dob']))
    for i in artist_name:
        artist_details['name']=i[0]
        artist_details['details'] = Songs.objects.filter(artists__name=i[0])
        artist_details['dob']=i[1]
        artist_details_full.append(artist_details.copy())
    all_songs = Songs.objects.all()
    context = {'all_artists':all_artists,'artist_details':artist_details_full[:10]}
    return render(request,'artists.html',context=context)

@login_required
def add_artist_ajax(request):
    if request.GET.get('action')=='add_artist':
        name = request.GET.get('name')
        dob = request.GET.get('dob')
        bio = request.GET.get('bio')
        artist_create = Artists.objects.create(name=name,dob=dob,bio=bio)
        artist_create.save()
        return JsonResponse({'ret':True,'result':True})
    return render(request, 'add_artist.html')

@login_required
def add_song(request):
    if request.method =='POST':
        try:
            name = request.POST.get('name')
            date_of_release = request.POST.get('date_of_release')
            rating = request.POST.get('rating')
            artist = request.POST.get('artist')
            artist =  str(request.POST).split("'artist': ")[1][1:str(request.POST).split("'artist': ")[1].find(']')].replace("'","")
            cover_image = request.FILES.get('cover_image')
            artist_create = Songs.objects.create(name=name,cover_image=cover_image,date_of_release=date_of_release)
            for i in artist.split(','):
                artist_object = Artists.objects.get(id=int(i))
                artist_create.artists.add(artist_object)
            artist_create.save()
            context = {'ret':'Song added successfully.','result':True}
            return render(request, 'add_songs.html',context=context)
        except:
            context = {'ret': 'Error adding song.', 'result': True}
            return render(request, 'add_songs.html', context=context)
    return render(request, 'add_songs.html')

@login_required
def get_artist_ajax(request):
    if request.GET.get('action')=='get_artist':
        all_artist = Artists.objects.all()
        return JsonResponse({'ret':list(all_artist.values()),'result':True},safe=False)

@login_required
def get_rating_ajax(request):
    if request.GET.get('action')=='get_rating':
        user = get_user_model()
        all_rating = Rating.objects.filter(author=request.user.id)
        return JsonResponse({'ret': list(all_rating.values()), 'result': True}, safe=False)

@login_required
def put_rating_ajax(request):
    if request.GET.get('action')=='put_rating':
        song_id = request.GET.get('song_id')
        rating = request.GET.get('rating')
        song_object =  Songs.objects.get(id=song_id)
        all_rating = Rating.objects.create(author=request.user,song=song_object,rating=rating)
        all_rating.save()
        return JsonResponse({'ret': True, 'result': True}, safe=False)