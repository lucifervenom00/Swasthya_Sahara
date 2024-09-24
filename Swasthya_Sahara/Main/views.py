from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Blog,JournalEntry,Category
from django.views.generic import ListView, DetailView
from .forms import JournalEntryForm
# Create your views here.
def home(request):
    blogs=Blog.objects.all()
    return render(request,"home.html",{'blogs':blogs})

def blog_home(request):
    blogs=Blog.objects.all()
    return render(request,"main/blog_home.html",{'blogs':blogs})
def blog_post(request,pk):
    post = get_object_or_404(Blog, pk=pk)
    categories=Category.objects.all()
    context={
        'category':categories,
        'post':post
    }
    return render(request,"main/blog_post.html",context)
def post(request):
    return render(request,"main/post.html")
@login_required(login_url='/accounts/login/')
def user(request):
    form = JournalEntryForm()
    # print(form.as_p())
    blogs=Blog.objects.all()
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            journal_entry = form.save(commit=False)
            journal_entry.user = request.user  # Associate entry with logged-in user
            journal_entry.save()
            journal_entry.objects.create(content=content)
    else:
        form = JournalEntryForm()
    context={
        'form':form,
        'blogs':blogs
    }
    # return render(request, 'main/base_user.html', {'form': form})
    return render(request,"main/user_dashboard.html",context)
def user_profile(request):
    return render(request,"account/profile.html")
def chat(request):
    return render(request,"main/chat.html")
def handle_login_redirect(request):
    # Redirect to the allauth login page
    return redirect(reverse('account_login'))
# def about_us(request):
#     return render(request,"main/about_us.html")

def update_profile(request):
    return render(request,'account/User_update_view.html')
def blog_list_view(request):
    blogs = Blog.objects.all()  # Fetch all blog entries
    return render(request, 'main/blog_home.html', {'blogs': blogs})


#chat bot
def chat_view(request):
    return render(request, 'main/chat.html')


@login_required
def delete_all_journal_entries(request):
    entry = get_object_or_404(JournalEntry, user=request.user)
    if request.method == 'POST':
        entry.delete();
        return redirect('main/user_dashboard.html') 
    return render(request, 'main/journal_list.html')
@login_required
def journal_list(request):
    entries = JournalEntry.objects.filter(user=request.user).order_by('-date_created')
    return render(request, 'main/journal_list.html',{'entries': entries})
    

