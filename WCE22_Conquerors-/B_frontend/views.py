from contextlib import nullcontext
from django.shortcuts import render,redirect
from B_home.models import broadcast
import requests, json
# Create your views here.
def home(request):
    # bd=broadcast.objects.all()
    response = requests.get('http://127.0.0.1:8000/broadcastviewset')
    # requests.delete('http://127.0.0.1:8000/broadcastviewset/86de0789-a5f2-4f08-abab-d6113765fd13')
    print(response.text)
    return render(request,'index.html',{'bd':json.loads(response.text)})

def filter(request):
    if request.method == 'POST':
        cat=request.POST["filtercategory"]
        frmat=request.POST["filterformat"]
        sDate=request.POST["startDate"]
        eDate=request.POST["endDate"]
        print(sDate)
        print(eDate)
        if cat=="All":
            q=broadcast.objects.filter(format=frmat)
            print(q)
            return render(request,'index.html',{'bd':q})
        if frmat=="All":
            q=broadcast.objects.filter(category=cat)
            print(q)
            return render(request,'index.html',{'bd':q})
        
        q=broadcast.objects.filter(format=frmat)&broadcast.objects.filter(category=cat)
        return render(request,'index.html',{'bd':q})