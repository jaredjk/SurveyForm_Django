from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        request.session['name3'] = request.POST['name3']
        request.session['location3'] = request.POST['location3']
        request.session['language3'] = request.POST['language3']
        request.session['comment3'] = request.POST['comment3']
    return redirect('/result')

def result(request): 

    return render(request, 'result.html')