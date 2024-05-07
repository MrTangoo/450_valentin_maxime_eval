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



    def test_book_list(self):
            # Arrange : Création de quelques livres pour tester la liste des livres
            Book.objects.create(title='Book 1', author='Author 1')
            Book.objects.create(title='Book 2', author='Author 2')
            Book.objects.create(title='Book 3', author='Author 3')

            # Act : Envoi d'une requête GET pour obtenir la liste des livres
            client = Client()
            response = client.get(reverse('book_list'))

            # Assert
            # Vérifier que la réponse est un succès (status_code 200)
            self.assertEqual(response.status_code, 200)
            # Vérifier que tous les livres sont présents dans la réponse
            self.assertContains(response, 'Book 1')
            self.assertContains(response, 'Book 2')
            self.assertContains(response, 'Book 3')
            # Vérifier que le nombre de livres dans la réponse est correct
            self.assertEqual(len(response.context['book_list']), 3)

