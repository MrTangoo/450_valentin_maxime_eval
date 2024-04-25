from django.test import TestCase, Client
from django.urls import reverse
from library.models import Book

class BookIntegrationTest(TestCase):

    def test_create_book(self):
        # Arrange : Données du nouveau livre à créer
        new_book_data = {'title': 'Pico Bogue', 'author': 'Dominique Roques'}

        # Act : Envoi d'une requête POST pour créer un nouveau livre
        client = Client()
        response = client.post(reverse('create_book'), data=new_book_data)

        # Assert
        # Redirection vers la page de détail du livre après sa création
        self.assertRedirects(response, reverse('info', args=[1]), status_code=302, target_status_code=200)
        # Livre créé correctement dans la BD
        book = Book.objects.get(id=1)
        assert book.author == "Dominique Roques"
        assert book.title == "Pico Bogue"
