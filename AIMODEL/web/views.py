from django.shortcuts import render,redirect
import pickle
import numpy as np


def index(request):
    model = pickle.load(open("d://logic", "rb"))
    if request.method == 'POST':

        k = request.POST.get('input1')
        k2= request.POST.get('input2')
        k3 = request.POST.get('input3')
        k4 = request.POST.get('input4')
        k = np.array([[k, k2, k3, k4]])
        h = model.predict(k)
        return render(request, 'index.html',{'pred':h})
    return render(request,'index.html')


