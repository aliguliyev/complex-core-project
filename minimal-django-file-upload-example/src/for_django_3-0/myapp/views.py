from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
from .custom_parse import parse
from .custom_change_file_name import change_name
import uuid
# from pathlib import stem


def my_view(request):
    # print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = ''
    # Handle file upload
    context = {}
    zipname = ''
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.docfile.name = change_name(newdoc.docfile.name)

            newdoc.save()
            name = newdoc.docfile.name
            fpath = newdoc.docfile.path
            print("Name:", name, "\npath", fpath)
            zipname = parse(fpath)
            context['zipfile'] = zipname + '.zip'
            print("zipname:", zipname)
            print("context:", context)
            
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
   
    # Render list page with the documents and the form
    context['documents'] = documents
    context['form'] = form
    context['message'] = message
    print("context:", context)
    zn = context['zipfile']
    zn = zn.split("/")[-1]
    zn = 'http://127.0.0.1:8000/media/results/' + zn
    context['zipfile'] = zn
    # print("zipname:", zn)
    
    return render(request, 'list.html', context)
