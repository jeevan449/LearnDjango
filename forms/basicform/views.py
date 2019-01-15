from django.shortcuts import render

# Create your views here.
from .forms import RawForm
from .models import Sample_Data

def get_time():
	return 'this is time'
def basicform_view(request):
	data = Sample_Data.objects.all()
	
	content = {'data':data,'time':get_time()}

	return render(request,'index.html',content)

def create_data_view(request):
	fr = RawForm()
	if request.method == 'POST':
		fr = RawForm(request.POST)
		if fr.is_valid():
			print(fr.cleaned_data)
			Sample_Data.objects.create(**fr.cleaned_data)

		else:
			print('erros')
	content = {'form':fr}
	return render(request,'create.html',content)