from django.shortcuts import render


# Create your views here.
def contact(request):
    return render(request, 'web/contact_us.html')


def about(request):
    return render(request, 'web.about_us.html')
