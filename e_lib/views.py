from django.shortcuts import render, HttpResponse
from .models import Book, Folder
# from .tasks import get_folder_data
import ast
import sys, os

sys.path.append('/home/damir/drive_app/e_lib/')

save_to_path = '/home/damir/drive_app/e_lib/CicaGoran/results'
to_file = 'data_list.txt'
complete_name = os.path.join(save_to_path, to_file)

# Create your views here.


def home(request):
    folders = Folder.objects.filter(Folder_id="0Bzg8AlBqbBUnaEdrZmhaOVVJSVE")
    context = {'folders': folders}
    return render(request, 'e_lib/M.html', context)



def folders(request, info):
    return render(request, f'e_lib/{info}')


def update(request):
    
    with open(complete_name, 'r') as lines:
        lines = lines.read()
        a = ast.literal_eval(lines)

        for item in a:
            if 'webViewLink' in item.keys():
                Book.objects.create(Name = item['name'], Folder_id = item['folder_id'], Link = item['webViewLink'])
            else:
                Folder.objects.create(Name = item['name'], Folder_id = item['folder_id'])
    return HttpResponse('<h2>Database updated.</h2>')
