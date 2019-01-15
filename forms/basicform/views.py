from django.shortcuts import render

# Create your views here.


def basicform_view(request):
	content = {}
	return render(request,'index.html',{})

def create_data_view(request):
	content = {}
	return render(request,'create.html',{})