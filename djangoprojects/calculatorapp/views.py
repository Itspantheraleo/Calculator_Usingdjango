from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def submitquery(request):
    q = request.GET.get('query','')
    try:
        ans=eval(q)
        mydict={
            'q':q,
            'ans':ans,
            'error':False,
        }
    except Exception as e:
        mydict={
            'q':q,
            "error":True, 
            'ans':None,
        }
    return render(request,'index.html',context=mydict)

