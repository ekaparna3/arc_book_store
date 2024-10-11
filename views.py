from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from bookstoreapp.models import BookModel
from django.views import View
from django.contrib.auth.models import User
from bookstoreapp.forms import BookForm,RegisterForm,LoginForm,SearchForm
from django.views.generic import CreateView,TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator



# Create your views here
class HomeView(TemplateView):
    template_name='main.html'

class BookView(TemplateView):
    template_name="index.html"

    


    

class RegisterView(CreateView):
    template_name='home.html'
    model=User
    form_class=RegisterForm

    def form_valid(self,form):
        messages.success(self.request,"registration successfull")
        User.objects.create_user(**form.cleaned_data)
        return redirect('log_view')
    
    def form_invalid(self,form):
        messages.error(self.request,"registration incomplete!!!try again")
        return redirect('reg_view')
    
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        user=authenticate(request,username=uname,password=pswd)
        
        if user:
            login(request,user)
            messages.success(request,'Login Successfully')
            return redirect('book_list')
        else:
            messages.error(request,"invalid credentials")
            form=LoginForm()
            return render(request,'login.html',{'form':form})
        
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home_view')
    

def booklist(request):
        # items=BookModel.objects.all()
        booklist = BookModel.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(booklist, 3)
        page_obj = paginator.get_page(page_number)
        print(page_obj)
        return render(request,'index.html',{"page_obj":page_obj})


def searchlist(request):
    form=SearchForm()
    books=BookModel.objects.all()

    if 'searched' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            searched = form.cleaned_data['searched']
            books = BookModel.objects.filter(title__icontains=searched)  

    return render(request, 'search.html', {'form': form, 'books': books})

# def pagination(request):
#     items=BookModel.objects.all()
#     paginator=Paginator(items,5)

#     page_number = request.GET.get("page")
#     pageobj = paginator.get_page(page_number)
#     return render(request,'page.html',{'pageobj':pageobj})
    
# def pagination(request):
#     booklist = BookModel.objects.all()
#     page_number = request.GET.get('page')
#     paginator = Paginator(booklist, 3)
#     page_obj = paginator.get_page(page_number)
#     print(page_obj)
#     return render(request,'page.html',{"page_obj":page_obj})