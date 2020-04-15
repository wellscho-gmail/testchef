from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

from django.http import HttpResponse

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    # book name include love
    num_lovebook = Book.objects.filter(title__contains='love').count()
    print('lovebook has' + str(num_lovebook))

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_lovebook': num_lovebook,
        'num_visits': num_visits,
    }
    
    print(str(context))

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

class BookListxxView(generic.ListView):
    model = Book
    paginate_by = 2
    #context_object_name = 'book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='love')[:5] # Get 5 books containing the title war
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

    #def get_queryset(self):                                     # overwrite the original get_queryset
        #return Book.objects.filter(title__icontains='love')[:5] # Get 5 books containing the title war
'''
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
'''

class BookDetailView(generic.DetailView):
    model = Book