from django.shortcuts import render
from cinema.models import cin
from cinema.forms import cinform
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

# def base(request):
#     c=cin.objects.all()
#     return render(request,'base.html',{'c':c})
# Create your views here.

class Movielistview(ListView):
    model=cin
    template_name="base.html"
    context_object_name="c"




# def viewdetails(request,p):
#     b=cin.objects.get(id=p)
#
#     return render(request, 'viewdetails.html', {'b': b})

class MovieDetailView(DetailView):
    model=cin
    template_name="viewdetails.html"
    context_object_name="b"


# def update(request,p):
#     b=cin.objects.get(id=p)
#     f=cinform(instance=b)
#     if(request.method=="POST"):
#         print(request.POST)
#         f=cinform(request.POST,instance=b)
#         if(f.is_valid()):
#             f.save()
#             return base(request)
#     return render(request,'update.html',{'form':f})


# def delete(request,p):
#     b = cin.objects.get(id=p)
#     b.delete()
#
#     return base(request)



def addmovie(request):
    f=cinform()   #empty form object
    if(request.method=='POST'):
        print(request.POST)
        f=cinform(request.POST,request.FILES)
        if(f.is_valid()):
            f.save()
            return base(request)
    return render(request,'addmovie.html',{'form':f})


# class Movieaddview(CreateView):
#     model=cin
#     template_name = "addmovie.html"
#     fields=['name','desc','year','img']
#     success_url=reverse_lazy('cinema':base.html)

class Movieupdateview(UpdateView):
    model=cin
    template_name="update.html"
    fields=['description','title','img']
    success_url=reverse_lazy('cinema:base')

class Deletemovieview(DeleteView):
    model=cin
    template_name = "delete.html"
    success_url=reverse_lazy('cinema:base')
