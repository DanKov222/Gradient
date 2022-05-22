import numpy as np
from numpy import ndarray
from sympy import *
from sympy import diff


def function(func, x):
    func = str(func)
    func = func.replace('x', 'x[0]')
    func = func.replace('y', 'x[1]')
    func = func.replace('^', '**')
    func = eval(func)
    return func


def function_derivative(func):
    func = str(func)
    func = func.replace('^', '**')
    x = Symbol('x')
    y = Symbol('y')
    x_f = eval(func.replace('y', '1'))
    y_f = eval(func.replace('x', '1'))
    x_der = x_f.diff(x)
    y_der = y_f.diff(y)
    return [x_der, y_der]


def gradient(f, alpha=0.001, eps=0.00001):
    x_st = np.array([10, 10])
    x = np.array([5, 5])
    for _ in range(10000000):
        if np.sum(abs(x - x_st)) < eps:
            break
        x_st = x
        a = function_derivative(f)
        first = str(a[0])
        second = str(a[1])
        first = first.replace('x', 'x_st[0]')
        second = second.replace('y', 'x_st[1]')
        first = eval(first)
        second = eval(second)

        try:
            x = x_st - alpha * np.array(first, second)
        except:
            x = x_st - alpha * np.array(first, first/first)
    return np.round(x, 5)


def answer(func):
    x_min = gradient(func)
    f_min = round(function(func, x_min), 5)
    return [x_min, f_min]
