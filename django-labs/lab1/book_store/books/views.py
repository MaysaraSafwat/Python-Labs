from django.shortcuts import render


books_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'The Picture of dorian gray',
        'author': 'Oscar Wild',
        'description': "The Story of a young Man and what vanity did to him",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'The House on the Cerulian Sea',
        'author': "T.J Klune",
        'description': "the story of a man who gets to work t a Magic orphanage for magic creatures/kids",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Normal People',
        'author': 'Sally Rooney',
        'description': "Miscommunication and Selfishness",
    },
]
# Create your views here.
def index(request):
     my_context = {'books_list': books_list}
     return render(request, 'index.html', context=my_context)

def get_book_details(request, *args, **kwrgs):
    book_id = kwrgs.get('book_id')
    book_object = get_book(book_id)
    my_context = {
        'book_id': book_object.get('id'),
        'book_name': book_object.get('name'),
        'book_author': book_object.get('author'),
        'book_description': book_object.get('description')
    }
    return render(request, 'book_details.html' , context=my_context)

def update (request, *args, **kwrgs):
    book_id = kwrgs.get('book_id')
    book_object = get_book(book_id)
    my_context = {
        'book_id': book_object.get('id'),
        'book_name': book_object.get('name'),
        'book_author': book_object.get('author'),
        'book_description': book_object.get('description')
    }
    return render(request, 'book_update.html', context=my_context)

def get_book(id):
    for book in books_list:
        if 'id' in book and book['id'] == id:
            return book
    return None