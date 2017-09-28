from django.shortcuts import render


def user_list(request):
    return render(request, 'logger/user_list.html')
