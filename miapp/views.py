from .models import tareas
from django.shortcuts import render,redirect,get_object_or_404
from .forms import taskform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
 
def index(request):
    
    return render(request,'index.html')


@login_required
def tarea(request):
    tarea=tareas.objects.filter(usuario=request.user,done=False)
    return render(request,'tarea.html',{
        'tareas':tarea
    })
    
@login_required    
def tarea_completed(request):
    tarea=tareas.objects.filter(usuario=request.user,done=True)
    return render(request,'tarea.html',{
        'tareas':tarea
    })
    
     
@login_required
def tareas_nuevas(request):
    if request.method=='GET':
        return render (request,'tarea_nueva.html',{
            'form':taskform
        })
    else:
        try:
            form=taskform(request.POST)
            new_task=form.save(commit=False)
            new_task.usuario=request.user
            new_task.save()
            return redirect('tarea')
        except ValueError:
            return render (request,'tarea_nueva.html',{
            'form':taskform,
            'error':'Please provide valide data'
        })
@login_required    
def tarea_detail(request,tareas_id):
    if request.method=='GET':
        tarea=get_object_or_404(tareas,pk=tareas_id,usuario=request.user)
        form=taskform(instance=tarea)
        return render(request,'tarea_detail.html',{'tareas':tarea,'form':form})
    else:
        try: 
            tarea=get_object_or_404(tareas,pk=tareas_id,usuario=request.user)
            form=taskform(request.POST,instance=tarea)
            form.save()
            return redirect('tarea')
        except ValueError:
            return render(request,'tarea_detail.html',{'tareas':tarea,'form':form,'error':'Error actualizando tarea'})
        
@login_required            
def complete_tarea(request,tareas_id):
    tarea=get_object_or_404(tareas,pk=tareas_id,usuario=request.user)
    if request.method=='POST':
        tarea.done=True
        tarea.save()
        return redirect('tarea')
@login_required    
def delete_tarea(request,tareas_id):
    tarea=get_object_or_404(tareas,pk=tareas_id,usuario=request.user)
    if request.method=='POST':
        tarea.delete()
        return redirect('tarea')
    


def sign_up(request):
    if request.method =='GET':
        return render(request,'signup.html',{
        'formulario': UserCreationForm
    })
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tarea')
            except IntegrityError:
                return render(request,'signup.html',{
                    'formulario':UserCreationForm,
                    "error":'Usuario ya existente'
                })
        return render(request,'signup.html',{
                    'formulario':UserCreationForm,
                    "error":'Las contraseñas no coinciden'
                })

@login_required
def sign_out(request):
    logout(request)
    return redirect('index')

def sign_in(request):
    if request.method=='GET':
        return render(request,'signin.html',{
            'form':AuthenticationForm
        })
    else:
        user=authenticate(
        request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render (request,'singin.html',{
                'form':AuthenticationForm,
                'error':'Usuario o Contraseña incorrectos'  
            })
        else:
            login(request,user)
            return redirect('tarea')
            
            
        
        


        










