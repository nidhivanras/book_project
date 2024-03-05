from django.http import JsonResponse
from django.shortcuts import render
from .models import Book, BookIndex


# Create your views here.
def book_list(request):
    book_folder = Book.objects.all()
    context = {
        'book_folder': book_folder,
    }
    return render(request, 'book_list.html', context)


def book_folder_files(request, folder_id):
    folder_files = BookIndex.objects.filter(book_id=folder_id)
    context = {
        'folder_files': folder_files,
    }
    # return render(request, 'book_files.html', context)
    # return render(request, 'book_details.html', context)
    # return render(request, 'test2.html', context)
    # return render(request, 'home.html', context)
    return render(request, 'new_h.html', context)


def get_index_pdf(request, index_id):
    pdf_files = BookIndex.objects.get(id=index_id)
    context = {
        'pdf': pdf_files.file.url,
    }

    return JsonResponse(context)
