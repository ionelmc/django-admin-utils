from django.http import HttpResponse


def root(request):
    return HttpResponse("root")


def level1(request):
    return HttpResponse("level1")


def level2(request):
    return HttpResponse("level2")
