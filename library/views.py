from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from django.views import View
from .forms import BookForm

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_visits': num_visits},
    )

def book_info(request, pk):
    """View function for book info."""
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_info.html", {'book':book})

class CreateBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save()
            # Rediriger vers la page de détail du livre nouvellement créé
            return redirect('info', pk=new_book.pk)
        else:
            # Si le formulaire n'est pas valide, réafficher le formulaire avec les erreurs
            return render(request, 'create_book.html', {'form': form})