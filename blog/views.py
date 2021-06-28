from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .models import SurvivorStories
from .forms import PostStory
from django.shortcuts import redirect

def home_page(request):
	return render(request, 'blog/home_page.html', {})

def who_we_are(request):
	return render(request, 'blog/who_we_are.html', {})

def our_work(request):
	return render(request, 'blog/our_work.html', {})

def faq(request):
	return render(request, 'blog/faq.html', {})

def work_with_us(request):
	return render(request, 'blog/work_with_us.html', {})

#blogs
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method =="POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)

	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})

def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save( commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render (request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

#stories
def share_your_story(request):
	stories = SurvivorStories.objects.order_by('-published_date')
	return render(request, 'blog/survivor_stories_list.html', {'stories':stories})

def new_story(request):
	if request.method == "POST":
		form = PostStory(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.published_date = timezone.now()
			post.save()
			return redirect('survivor_story')
	else:
		form = PostStory()
	return render (request, 'blog/create_survivor_stories.html', {'form': form})
