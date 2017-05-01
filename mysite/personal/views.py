from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me at:','rfgranzow@gmail.com']})

def CV(request):
	return render(request, 'personal/cv.html')

def VBA(request):
	return render(request, 'personal/VBA.html')

def LaTeX(request):
	return render(request, 'personal/LaTeX.html')

def Pytuts(request):
	return render(request, 'personal/Pytuts.html')

def django(request):
	return render(request, 'personal/django.html')

def extra(request):
	return render(request, 'personal/extra.html')

def safety(request):
	return render(request, 'personal/safety.html')

def forecast(request):
	return render(request, 'personal/forecast.html')

