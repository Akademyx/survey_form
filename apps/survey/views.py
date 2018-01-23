from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if not 'name' in request.session and not 'loc' in request.session and not 'language' in request.session and not 'comment' in request.session:
        request.session['name'] = ''
        request.session['loc'] = ''
        request.session['language'] = ''
        request.session['comment']=''
    if not 'count' in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1
 
    return render(request, 'index.html')

def process(request):
    request.session['name'] = request.POST['name']
    print "name is ", request.session['name']
    request.session['loc'] = request.POST['loc']
    print "loc is ", request.session['loc']
    request.session['language'] = request.POST['language']
    print "language is ", request.session['language']
    request.session['comment'] = request.POST['comment']
    print "comments are ", request.session['comment']
    return redirect('/result')

def result(request):
    context = {
        'name': request.session['name'],
        'loc': request.session['loc'],
        'language': request.session['language'],
        'comment': request.session['comment'],
        'count': request.session['count']
    }
    return render(request, 'result.html', context)
