# views.py
from django.shortcuts import render, redirect,get_object_or_404
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime

def blog(request):
    if not request.user.is_authenticated:  
        return redirect('login')
    else:
        if request.method == 'POST': 
            title = request.POST.get('title')   
            description = request.POST.get('description') 

            new_blog = Todo(
            title=title,
            description=description,
            author=request.user
            )

            try:
                new_blog.save()
                return redirect('blog')
            except Exception as e:
                return render(request, 'error.html', {'error': str(e)})

        else:
            blogs = Todo.objects.all().order_by('-date_created')  
            return render(request, 'index.html', {'blogs': blogs})
        
def delete_blog(request, id):
    if request.method=='POST':
        blog_to_delete = get_object_or_404(Todo,id=id)  
        try:
            blog_to_delete.delete() 
            return redirect('blog')  
        except Exception as e:
            return f'There was a problem deleting that blog: {str(e)}'
    else:
        blogs = Todo.objects.all().order_by('date_created') 
        return render(request, 'index.html', {'blogs': blogs})   
     
def update_blog(request, id):
    blog = get_object_or_404(Todo, id=id)  

    if request.method == 'POST':  
        blog.content = request.POST['content'] 
        
        try:
            blog.save()  
            return redirect('blog')  
        except Exception as e:
            return f'There was an issue updating your blog: {str(e)}' 
    
    else:  
        return render(request, 'update.html', {'blog': blog})
    
@login_required
def add_blog(request):
    if request.method == 'POST':
        
        title = request.POST['title']
        description = request.POST['description']
        author = request.user.first_name
       
        new_blog = Todo(title=title, description=description, author=author)
        new_blog.save() 

        return redirect('blog/')  
    return render(request, 'add_blog.html')

def blog_detail(request,id):
    blog = get_object_or_404(Todo, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})


