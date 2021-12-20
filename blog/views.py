from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse,JsonResponse,HttpResponseNotFound,Http404
from django.urls import reverse,reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
 
###################
#do order by filter,search(js?)
#switch all to classes
#user table
########################

def test_detail_view(request,pk,*args,**kwargs):     #not used
    #assert isinstance(request, HttpRequest) 
    mlist = Movie.objects.get(id=pk)
    try:
        mlist = Movie.objects.get(id=pk)
        
    except test.DoesNotExist:
        Http404
   # return   HttpResponse(f" please{test_list.id}")
    return render(request, 'test_detail_view.html',{"mlist":mlist} )



#************************************* simple navigating
def testd(request,pk,*args,**kwargs):                                       #shows full desc. on main
     movie = Movie.objects.get(id=pk)
     return render(request, 'test_detail.html',{"movie":movie})
     # return HttpResponse("test.html")


def  login_ref(request):
  return render(request, 'login.html')


def add_v(request):                  #not used
    if request.method == 'POST':
        form = AddPostForm(request.POST,request.FILES)
        if form.is_valid():
       
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None," Something's not right")

    else:
        form = AddPostForm()
    return render(request, 'add.html',{'form':form})

def index(request):
  mlist=Movie.objects.all()
  ratings = Rating.objects.all()

  return render(request, 'index.html',{'mlist':mlist,'title':"TheIndex"})
  
def home_v(request):
    records=Movie.objects.all()
    ratings = Rating.objects.all()

    return render(request, 'home.html',{'records': records,'rate_selected':0,'ratings': ratings,'title':"TheHome"})

#**********************************sub navs
def genres(request, genre_id): #not used
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Stored by genre</h1><p>{genre_id}</p>")

def date(request, year):     #not used
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Stored by order</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>my bad(404),best of luck</h1>')


def rate_v(request,rating_id,*args,**kwargs):     #specfic nmovie

    records = Movie.objects.filter(rating_id=rating_id)
    ratings = Rating.objects.all()

    if len(records) == 0:
          records = Movie.objects.all()           #showing all if no matches
    
    paginator = Paginator(records, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'records': records,
        'ratings': ratings,
        'page_obj': page_obj,
        'title': 'By rating',
        'rate_selected': rating_id,
    }

    return render(request, 'home.html', context=context)



#***************************************************************



#*********************error

def error(request,exception):
    return HttpResponse("<h2>4my 0 bad4</h2>")

def register(request):
  return render(request, 'register.html')

#************************************************************** in views classes
class MovieMain(ListView):
    model = Movie
    paginate_by=2
    template_name = 'home.html'
    context_object_name = 'records'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ratings']= Rating.objects.all()
        context['title'] = 'TheMain'

        context['rating_selected'] = 0
        return context

    def get_queryset(self):
        return Movie.objects.filter(is_published=True) #only show published



class add_v(CreateView):
    form_class = AddPostForm
    template_name = 'add.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'YourMovie'
        return context

#///////8888888888888888888888888888888888888888888888888888888888888888888888888888 user (sign up=register | register=log in...)
class SignUp(CreateView):                                 #signup
    form_class = RegisterUserForm
    title="SignUp"
    template_name = 'signup.html'

    success_url = reverse_lazy('login')
    
    def get_user_context(self, **kwargs):                    #datamiixin
        context = kwargs
        ratings = Rating.objects.all()

        if not self.request.user.is_authenticated:
            return redirect('home')

        context['ratings'] = ratings
        if 'rate_selected' not in context:
            context['rate_selected'] = 0
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="SignUp")
        return dict(list(context.items()) + list(c_def.items()))



class LoginUser(LoginView):                  #login
    form_class = LoginUserForm
    template_name = 'login.html'
    
    def get_user_context(self, **kwargs):             #datamiixin
        context = kwargs
        ratings = Rating.objects.all()

        if not self.request.user.is_authenticated:
            return redirect('home')

        context['ratings'] = ratings
        if 'rate_selected' not in context:
            context['rate_selected'] = 0
        return context


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="LogIn")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):                                       #logout
    logout(request)
    return redirect('index')






#*********************************************************************************************************************************************************
class BlogListView(ListView):
    model = Post
    title="TheHome"
    template_name = 'home.html'

class BlogDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'