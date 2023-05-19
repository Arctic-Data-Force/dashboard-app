import zipfile

from django.http import HttpResponseRedirect
from django.shortcuts import render

from dashboard.forms import ChampionshipForm
from dashboard.models import Championship


def index(request):
    return render(request, 'dashboard/index.html')


def create_championship(request):
    if request.method == 'POST':
        form = ChampionshipForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            registration_file = request.FILES['registration_file']
            results_file = request.FILES.get('results_file')
            # Сохранение файлов на сервере
            with open('media/registration_files/{}.csv'.format(name), 'wb+') as destination:
                for chunk in registration_file.chunks():
                    destination.write(chunk)
            if results_file:
                with zipfile.ZipFile(results_file, 'r') as results_zip:
                    for filename in results_zip.namelist():
                        with results_zip.open(filename) as csvfile:
                            # Обработка csv-файла
                            pass
            # Создание объекта чемпионата
            championship = Championship.objects.create(name=name)
            # ...
            return HttpResponseRedirect('/championships/')
    else:
        form = ChampionshipForm()
    return render(request, 'dashboard/create_championship.html', {'form': form})
