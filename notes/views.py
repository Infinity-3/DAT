from django.shortcuts import render,redirect
from .models import Note
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def note(request):
    # msg='Create a Note to Store'
    msg=''
    notecount=0
    noteinfo=None
    if request.user.id is not None:
        noteinfo=Note.objects.filter(user=request.user) 
        # notecount=len(noteinfo)  
        # print(notecount,'count of notes')
    else:
        # msg='1'
        return redirect('login')
    # noteinfo=Note.objects.all()
    # print(request.user,'is user')
   
    return render(request, 'notes.html',{'note': noteinfo,'msg':msg,'count':len(noteinfo) if len(noteinfo)>0 else None})   

@csrf_exempt
def create(request): 
    data=None 
    if request.method == 'POST':
        # note = Note()
        # note.title = request.POST.get('title')
        # note.desc = request.POST.get('content')
        # note.save()
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        data=Note.objects.create(title=title,desc=desc,user=request.user)
        return redirect('notes')
    return render(request, 'createnotes.html',{'data':data,'h1':None}) 


@csrf_exempt
def update(request,id):
    data = Note.objects.get(id=id)
    otitle=data.title
    odesc=data.desc
    if request.method == 'POST':
        title = request.POST.get('title') 
        desc = request.POST.get('desc')   
        data.title = title 
        data.desc = desc
        data.save()
        # data=Note.objects.create(title=title,desc=desc,user=request.user)
        return redirect('notes')
    return render(request, 'createnotes.html',{'data':data,'h1':not None})

def delete(request,id):
    data = Note.objects.get(id=id)
    data.delete()
    return redirect('notes')
