from django.shortcuts import render

def aboutView(request):
    template = 'pages/about.html'

    return render(request, template)
