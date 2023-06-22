from django.shortcuts import render
from app1.models import place,team

# Create your views here.
def base(request):
    p=place.objects.all()
    t=team.objects.all()
    return render(request,'base.html',{'p':p,'t':t})
