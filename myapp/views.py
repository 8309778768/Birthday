from django.shortcuts import render
from myapp.models import Post
# Create your views here.
def index(request):
	p=Post.objects.all()
	context={'posts':p}
	return render(request,'index.html',context)