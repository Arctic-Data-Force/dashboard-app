import zipfile

from django.http import HttpResponseRedirect
from django.shortcuts import render

from dashboard.forms import ChampionshipForm
from dashboard.models import Championship


def index(request):
    context = {
        'championships': Championship.objects.all()
    }
    return render(request, 'dashboard/index.html', context=context)


def show_championship(request, championship_id):
    championship = Championship.objects.get(id=championship_id)
    return render(request, 'dashboard/show_championship.html', {'championship': championship})


def create_championship(request):
    if request.method == 'POST':
        form = ChampionshipForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            registration_file = request.FILES['registration_file']
            results_file = request.FILES.get('results_file')
            # Create a new Championship object
            championship = Championship.objects.create(name=name)
            championship.save()
            # Assign uploaded files to the corresponding fields
            championship.registration_file = registration_file
            if results_file:
                championship.results_file = results_file
            championship.save()

            with open(f'media/uploads/{championship.name}/{registration_file.name}', 'wb+') as destination:
                # Обработка csv-файла регистрации пользователей
                pass
            if results_file:
                with zipfile.ZipFile(results_file, 'r') as results_zip:
                    for filename in results_zip.namelist():
                        with results_zip.open(filename) as csvfile:
                            # Обработка csv-файла каждой компетенции
                            pass
            # ...
            return HttpResponseRedirect(f'/championships/{championship.id}')
    else:
        form = ChampionshipForm()
    return render(request, 'dashboard/create_championship.html', {'form': form})
