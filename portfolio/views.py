from django.shortcuts import render , get_object_or_404
from .models import Project , Skill  , Account
from .forms  import  MessageForm

def home(request):
    projects = Project.objects.all() 
    skills = Skill.objects.filter(description = '')
    descripted_skills = Skill.objects.all().exclude(description = '')
    form = MessageForm()
    accounts = Account.objects.all()
    context = {
        'projects': projects, 
        'skills': skills ,
        'descripted_skills' : descripted_skills,
        'form' : form , 
        'accounts' : accounts , 
    }
    return render(request , 'portfolio/home.html' , context)



def project_detail(request , slug):
    project = get_object_or_404(Project , slug = slug )

    context = {
        'project' : project , 

    }
    return render(request , 'portfolio/project_page.html' , context)




#htmx views

def create_message(request):
    if request.method == 'POST' : 
        form = MessageForm(request.POST)
        if form.is_valid() : 
            form.save()
            done = True
            message = 'Thank you for contacting us'

        else : 
            done = False
            message = 'Please Enter a Valid Data'

        context = {
            'done' : done , 
            'message' : message , 
            }
        return render(request , 'portfolio/includes/succes_message.html' , context)