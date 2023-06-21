from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from rest_framework import status
import json
from .models import Aluno, Cronograma

User = get_user_model()

class AlunoCRUDIntegrationTests(TestCase):
    def setUp(self):
        self.aluno_data = {
            'first_name': 'Jefferson',
            'last_name': 'Ribeiro',
            'email': 'r.jeff@mail.com',
            'username': 'testuser',
            'password': 'testpassword',
            'notificacao': False,
            'qtd': 0
        }

    def test_create_aluno(self):
        aluno = Aluno.objects.create(**self.aluno_data)
        self.assertEqual(aluno.first_name, self.aluno_data['first_name'])
        self.assertEqual(aluno.last_name, self.aluno_data['last_name'])
        self.assertEqual(aluno.email, self.aluno_data['email'])
        self.assertEqual(aluno.username, self.aluno_data['username'])
        self.assertEqual(aluno.password, self.aluno_data['password'])
        self.assertEqual(aluno.notificacao, self.aluno_data['notificacao'])
        self.assertEqual(aluno.qtd, self.aluno_data['qtd'])

    def test_retrieve_aluno(self):
        aluno = Aluno.objects.create(**self.aluno_data)
        retrieved_aluno = Aluno.objects.get(id=aluno.id)
        self.assertEqual(retrieved_aluno.first_name, self.aluno_data['first_name'])
        self.assertEqual(retrieved_aluno.last_name, self.aluno_data['last_name'])
        self.assertEqual(retrieved_aluno.email, self.aluno_data['email'])
        self.assertEqual(retrieved_aluno.username, self.aluno_data['username'])
        self.assertEqual(retrieved_aluno.password, self.aluno_data['password'])
        self.assertEqual(retrieved_aluno.notificacao, self.aluno_data['notificacao'])
        self.assertEqual(retrieved_aluno.qtd, self.aluno_data['qtd'])

    def test_update_aluno(self):
        aluno = Aluno.objects.create(**self.aluno_data)
        updated_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane@example.com',
            'username': 'janesmith',
            'password': 'newpassword',
            'notificacao': True,
            'qtd': 1
        }
        Aluno.objects.filter(id=aluno.id).update(**updated_data)
        updated_aluno = Aluno.objects.get(id=aluno.id)
        self.assertEqual(updated_aluno.first_name, updated_data['first_name'])
        self.assertEqual(updated_aluno.last_name, updated_data['last_name'])
        self.assertEqual(updated_aluno.email, updated_data['email'])
        self.assertEqual(updated_aluno.username, updated_data['username'])
        self.assertEqual(updated_aluno.password, updated_data['password'])
        self.assertEqual(updated_aluno.notificacao, updated_data['notificacao'])
        self.assertEqual(updated_aluno.qtd, updated_data['qtd'])

    def test_delete_aluno(self):
        aluno = Aluno.objects.create(**self.aluno_data)
        Aluno.objects.filter(id=aluno.id).delete()
        self.assertFalse(Aluno.objects.filter(id=aluno.id).exists())

class AlunoCRUDSystemTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.aluno_data = {
            'first_name': 'Jefferson',
            'last_name': 'Ribeiro',
            'email': 'r.jeff@mail.com',
            'username': self.username,
            'password': self.password,
        }

    def test_create_aluno(self):
        url = reverse('Aluno-list')
        response = self.client.post(url, data=self.aluno_data)

        # Print para debug
        print(response.content)
        # Print para debug
        print(response.data)


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username=self.username).exists())

    def test_retrieve_aluno(self):
        user = User.objects.create_user(**self.aluno_data)
        url = reverse('Aluno-detail', kwargs={'pk': user.id})
        response = self.client.get(url)

        # Print para debug
        print(response.content)
        # Print para debug
        print(response.data)


        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_aluno(self):
        user = User.objects.create_user(username='example_user', password='example_password', email='existing_email@example.com')
        updated_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'username': 'example_user',
            'password': 'example_password',
        }
        url = reverse('Aluno-detail', kwargs={'pk': user.id})
        response = self.client.put(url, data=json.dumps(updated_data), content_type='application/json')
        
        # Print para debug
        print(response.content)
        # Print para debug
        print(response.data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)


    def test_delete_aluno(self):
        user = User.objects.create_user(**self.aluno_data)
        url = reverse('Aluno-detail', kwargs={'pk': user.id})
        response = self.client.delete(url)

        # Print para debug
        print(response.content)
        # Print para debug
        print(response.data)


        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(username=self.username).exists())

class CronogramaIntegrationTests(TestCase):
    def setUp(self):
        self.aluno = {
            'first_name': 'Lucas',
            'last_name': 'Melo',
            'email': 'lucas@mail.com',
            'username': 'testuser',
            'password': 'testpassword',
            'notificacao': False,
            'qtd': 0
        }
        self.cronograma = {
            'privacidade': False,
            'titulo': "Cronograma Teste",
            'aluno': self.aluno
        }

    def test_criar_cronograma(self):
        cronograma = Cronograma.objects.create(**self.cronograma)
        self.assertEqual(cronograma.privacidade, self.cronograma['privacidade'])
        self.assertEqual(cronograma.titulo, self.cronograma['titulo'])
        self.assertEqual(cronograma.aluno, self.cronograma['aluno'])

    def test_atualizar_cronograma(self):
        cronograma = Cronograma.objects.create(**self.cronograma)
        updated_data = {
            'titulo': 'Titulo teste',
            'privacidade': True
        }
        Cronograma.objects.filter(id=cronograma.id).update(**updated_data)
        updated_cronograma = Cronograma.objects.get(id=cronograma.id)
        self.assertEqual(updated_cronograma.privacidade, updated_data['privacidade'])
        self.assertEqual(updated_cronograma.titulo, updated_data['titulo'])

    def test_deletar_cronograma(self):
        cronograma = Cronograma.objects.create(**self.cronograma)
        Cronograma.objects.filter(id=cronograma.id).delete()
        self.assertFalse(Cronograma.objects.filter(id=cronograma.id).exists())
    
    def test_obter_cronograma_por_titulo(self):
        cronograma = Cronograma.objects.create(**self.cronograma)
        cronograma_obtido = Cronograma.objects.get(titulo=cronograma.titulo)
        self.assertEqual(cronograma_obtido.titulo, cronograma['titulo'])
    
    def test_obter_cronogramas_por_aluno(self):
        cronograma1 = Cronograma.objects.create(**self.cronograma)
        cronograma2 = Cronograma.objects.create(
            privacidade=False,
            titulo="Cronograma 2"
        )
        cronogramas_aluno = Cronograma.objects.filter(aluno=self.aluno)
        self.assertEqual(cronogramas_aluno.privacidade, cronograma1['privacidade'])
        self.assertEqual(cronogramas_aluno.titulo, cronograma1['titulo'])
        self.assertEqual(cronogramas_aluno.aluno, cronograma1['aluno'])
        self.assertIn(cronograma1, cronogramas_aluno)
        self.assertNotIn(cronograma2, cronogramas_aluno)