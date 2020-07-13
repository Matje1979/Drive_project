from django.shortcuts import render, HttpResponse
from .models import Book, UpdateLinks
# from .tasks import get_folder_data
import ast
import sys, os
from django.http import JsonResponse
from django.forms.models import model_to_dict
from helper.sort import sort_f
from .forms import MessageForm

sys.path.append('/home/damir/drive_app/e_lib/')

save_to_path = '/home/damir/drive_app/e_lib/CicaGoran/results'
to_file = 'data_list.txt'
complete_name = os.path.join(save_to_path, to_file)

# Create your views here.


def home(request):

    """Collects main folders and presents them on the frontpage"""

    print ('Hello')

    main_fs = []
    args = []

    for link in UpdateLinks.objects.all():  
        # print ("This is one link: ", link)         
        print ("*********************************************************************************************************")
        args.append(link.Main_folder_id)       #collecting id's of main folders/books

    # print ("These are link id's: ", args)
    

    for arg in args:
        print ("Id: ", arg)
        q = Book.objects.filter(Folder_id=arg)      #extracting main folders/books from Book instances for frontpage
        print ("Queryset: ", q)
        main_fs.append(q.values())              #turning querysets into lists of dictionaries with q.values() and appending them to a new list
    print ("Main_fs: ", main_fs)
   
    main_folders = []                       
    for queryset in main_fs:                  
        queryset = list(queryset)              #queryet content is a list of dicts but it itself is still a queryset, so it is transformed into list. 
                                               #this is all done because the sorting function sort_f works with lists of dicts, and not querysets.
        main_folders.append(sort_f(queryset, 'Name'))

    
    context = {'main_folders': main_folders}
    return render(request, 'e_lib/M.html', context)

def kontakt(request):
    if request.method == 'POST':
        form = MessageForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'e_lib/message_sent.html')
    else:
        form = MessageForm()

    context = {
        'form': form
    }
    return render(request, 'e_lib/kontakt.html', context)

def o_nama(request):
    return render(request, 'e_lib/o_nama.html')

def statistika(request):
    return render(request, 'e_lib/statistika.html')

def searchResults(request):


    print ('Hello, I am working!')

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        
        result = Book.objects.filter(Name__icontains = q)
        print (result)

        context = {'result': result}
    else:
       notfound = "Nista nije nadjeno."
       context = {'notfound': notfound}

   
    return render(request, 'e_lib/results.html', context)

def update(request):

    """ Updates database with data about google drives stored in a .txt file on the server."""

    with open(complete_name, 'r') as lines:
        lines = lines.read()
        a = ast.literal_eval(lines) 
        # print (a)

        count = 0
        count_item = 0

        for item in a:
            
            if 'webViewLink' in item.keys(): #if item is a folder it does not have the key 'webViewLink' 
                Book.objects.create(Book_id = item['id'], Name = item['name'], Folder_id = item['folder_id'], Link = item['webViewLink'])
            else:
                Book.objects.create(Book_id = item['id'], Name = item['name'], Folder_id = item['folder_id'])

            # a = Book.objects.all()
            # b = len(a)
           

    return HttpResponse('<h2>Database updated.</h2>')

def getBooks(request, parent_id):

    """Responds to an AJAX request. Returns a list of books/folders in a folder."""

    items = Book.objects.filter(Folder_id = parent_id).order_by('Name')
    new_list = []
    for item in items:
        new_list.append(model_to_dict(item))


        
    return JsonResponse({'new_list': new_list}, safe = False)

def message_create_view(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MessageForm()

    context = {
        'form': form
    }

    return render(request, 'e_lib/kontakt.html', context)



