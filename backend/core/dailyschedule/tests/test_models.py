from django.test import TestCase
from models import Aluno, Cronograma, Tipo, Tarefa

class AlunoTestCase(TestCase):
    
    def setUp(self):
        self.aluno1 = Aluno(first_name='João', last_name='Silva', email='joao@example.com', username='joao123', password='senha123')
        self.aluno2 = Aluno(first_name='João', last_name='Silva', email='joao@example.com', username='joao123', password='senha123')
        self.aluno3 = Aluno(first_name='Maria', last_name='Santos', email='maria@example.com', username='maria456', password='senha456')

    def test_aluno_eq_same_objects(self):
        self.assertEqual(self.aluno1, self.aluno1)

    def test_aluno_eq_equal_objects(self):
        self.assertEqual(self.aluno1, self.aluno2)

    def test_aluno_eq_different_objects(self):
        self.assertNotEqual(self.aluno1, self.aluno3)

    def test_aluno_ordering(self):
        self.assertLess(self.aluno2, self.aluno1)
        self.assertLessEqual(self.aluno1, self.aluno3)
        self.assertGreater(self.aluno1, self.aluno2)
        self.assertGreaterEqual(self.aluno1, self.aluno1)

class CronogramaTestCase(TestCase):
    
    def setUp(self):
        self.aluno = Aluno.objects.create(nome="João")
        self.cronograma1 = Cronograma.objects.create(privacidade=False, titulo="Cronograma 1", aluno=self.aluno)
        self.cronograma2 = Cronograma.objects.create(privacidade=True, titulo="Cronograma 2", aluno=self.aluno)
    
    def test_equals_same_instance(self):
        self.assertEqual(self.cronograma1, self.cronograma1)
    
    def test_equals_different_instances_same_values(self):
        cronograma = Cronograma(privacidade=False, titulo="Cronograma 1", aluno=self.aluno)
        self.assertEqual(self.cronograma1, self.cronograma)
    
    def test_equals_different_instances_different_values(self):
        cronograma = Cronograma(privacidade=True, titulo="Cronograma 3", aluno=self.aluno)
        self.assertNotEqual(self.cronograma1, self.cronograma)
    
    def test_compareTo_different_instances(self):
        cronograma = Cronograma(privacidade=False, titulo="Cronograma 2", aluno=self.aluno)
        self.assertLess(self.cronograma2, self.cronograma1)
        self.assertLessEqual(self.cronograma1, cronograma)
        self.assertGreater(self.cronograma1, self.cronograma2)
        self.assertGreaterEqual(self.cronograma1, self.cronograma1)

class TipoTestCase(TestCase):
    def setUp(self):
        self.tarefa = Tarefa.objects.create(nome="Tarefa 1")
        self.tipo1 = Tipo.objects.create(tipo="Tipo 1", assunto=False, tarefa=self.tarefa)
        self.tipo2 = Tipo.objects.create(tipo="Tipo 2", assunto=True, tarefa=self.tarefa)
    
    def test_tipo_default_value(self):
        tipo = Tipo()
        self.assertEqual(tipo.tipo, "")
    
    def test_equals_same_instance(self):
        self.assertTrue(self.cronograma1.equals(self.cronograma1))
    
    def test_compareTo_different_instances(self):
        tipo = Tipo(tipo="Tipo 2", assunto=False, tarefa=self.tarefa)
        self.assertLess(self.tipo2, self.tipo1)
        self.assertLessEqual(self.tipo1, tipo)
        self.assertGreater(self.tipo1, self.tipo2)
        self.assertGreaterEqual(self.tipo1, self.tipo1)
