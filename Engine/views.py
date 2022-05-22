from django.shortcuts import render, redirect
from .grad import *
from .models import Answer
import numpy as np
from numpy import ndarray
from sympy import diff


def main(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        f = str(request.POST.get('function'))
        ans = answer(f)
        context = {
            'x_min': ans[0][0],
            'y_min': ans[0][1],
            'f_min': ans[1]
        }
        return render(request, 'index.html', context)