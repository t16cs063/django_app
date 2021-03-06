from django.shortcuts import render
from .models import Friend
from .forms import HelloForm

def index(request):
    params = {
        'title':'Hello',
        'msg':'すべての友達',
        'form':HelloForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    
    return render(request, 'hello/index.html', params)