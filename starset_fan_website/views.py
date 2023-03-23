from django.shortcuts import render


def index(request):
    return render(request, 'starset_fan_website/index.html')


def band(request):
    return render(request, 'starset_fan_website/band.html')


def society(request):
    return render(request, 'starset_fan_website/society.html')


def feedback(request):
    return render(request, 'starset_fan_website/feedback.html')


def transmissions(request):
    return render(request, 'starset_fan_website/transmissions.html')


def divisions(request):
    return render(request, 'starset_fan_website/divisions.html')


def horizons(request):
    return render(request, 'starset_fan_website/horizons.html')


def vessels(request):
    return render(request, 'starset_fan_website/vessels.html')


def vessels_2(request):
    return render(request, 'starset_fan_website/vessels_2_0.html')


def form_response(request):
    return render(request, 'starset_fan_website/form_response.html')
