from django.shortcuts import render
from .models import User, ManagerDetail

# Create your views here.
def register_manager(request):
    if request.method == 'POST':  #When we click submit button
        if request.POST['f7'] == request.POST['f8']:
            try:
                user = User.object.create_manager(
                    name=request.POST['f1'],
                    email=request.POST['f2'],
                    phone=request.POST['f3'],
                    profilepic = request.FILES['f4'],
                    address = request.POST['f5'],
                    password = request.POST['f7']
                )
            except Exception as e:
                return render(request,'registermanager.html',{'m':e})
            else:
                try:
                    ManagerDetail.objects.create(user=user,
                                                branch=request.POST['f6']
                                                )
                except Exception as e:
                    user.delete()
                    return render(request,'registermanager.html',{'m':e})
                else:
                    return render(request,'registermanager.html',{'m':'Successfully account created'})
        else:
            return render(request,'registermanager.html',{'m':'Password did not match'})
    else: #When we normally open url
        return render(request,'registermanager.html')

def manager_login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request,'')