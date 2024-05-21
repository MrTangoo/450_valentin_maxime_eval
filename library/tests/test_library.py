from django.test import TestCase, Client
from django.urls import reverse
from library.models import Book
from unittest.mock import patch

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
        


class BookListUnitTestFixture(TestCase):

    
    @classmethod
    def setUpTestData(cls):
        # Création d'objets livres pour tester
        cls.book1 = Book.objects.create(title='Livre 1', author='Auteur 1')
        cls.book2 = Book.objects.create(title='Livre 2', author='Auteur 2')

    def test_book_list(self):
        # Arrange : Créer un client pour effectuer les requêtes HTTP
        client = Client()
        
        # Act : Envoyer une requête GET pour obtenir la liste des livres
        response = client.get(reverse('book_list'))
        
        # Assert : Vérifier la réponse HTTP, le modèle utilisé et la présence des livres dans la réponse
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertEqual(len(response.context['book_list']), 2)
        self.assertIn(self.book1, response.context['book_list'])
        self.assertIn(self.book2, response.context['book_list'])


class BookListIntegrationTestFixture(TestCase):
    
    @classmethod
    def setUpTestData(self):
        # Création d'objets livres pour tester
        self.book1 = Book.objects.create(title='Book 1', author='Author 1')
        self.book2 = Book.objects.create(title='Book 2', author='Author 2')

    def test_book_list_view(self):
        # Arrange : Créer un client pour effectuer les requêtes HTTP
        client = Client()

         # Act : Envoyer une requête GET pour obtenir la liste des livres
        response = client.get(reverse('book_list'))
        
        # Assert : Vérifier la réponse HTTP, la présence des livres dans la réponse et le modèle utilisé
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Book 1')
        self.assertContains(response, 'Book 2')
        self.assertTemplateUsed(response, 'book_list.html')


class BookListUnitTestMocks(TestCase):

    @patch('library.views.Book.objects.all')
    def test_book_list_with_mock(self, mock_all):
        # Arrange : Mock de la méthode 'objects.all()' de la classe Book
        mock_all.return_value = [
            Book(title='Mock Book 1', author='Mock Author 1'),
            Book(title='Mock Book 2', author='Mock Author 2')
        ]
        
        client = Client()
        
        # Act : Envoyer une requête GET pour obtenir la liste des livres
        response = client.get(reverse('book_list'))
        
        # Assert : Vérifier la réponse HTTP, le modèle utilisé, la présence des livres dans la réponse et l'appel à la méthode mockée
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertEqual(len(response.context['book_list']), 2)
        self.assertEqual(response.context['book_list'][0].title, 'Mock Book 1')
        self.assertEqual(response.context['book_list'][1].title, 'Mock Book 2')
        mock_all.assert_called_once()
