from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from rest_framework import permissions, viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

def user_list(request):
    records=User.objects.all()
    mydict={'records':records}
    return render(request,'app/listingpage.html',context=mydict)

@csrf_exempt
def add_user(request):
    mydict={}
    form=UserForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("/app/")

    mydict['form']=form
    return render(request,'app/add.html',mydict)

def edit_user(request,id=None):
    one_rec=User.objects.get(pk=id)
    form=UserForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/app/')
    mydict= {'form':form}
    return render(request,'app/edit.html',context=mydict)

def delete_user(request,eid=None):
    one_rec = User.objects.get(pk=eid)
    if  request.method !="POST":
         one_rec.delete()
         return redirect('/app/')
    return render(request,'app/delete.html')

def view_user(request,eid=None):
    mydict={}
    one_rec = User.objects.get(pk=eid)
    mydict['user']=one_rec
    return render(request,'''app/view.html''',mydict)