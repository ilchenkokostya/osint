from django.shortcuts import render


def home(reguest):
    name = 'Kosta'
    return render(reguest,'home.html', {'name': name})