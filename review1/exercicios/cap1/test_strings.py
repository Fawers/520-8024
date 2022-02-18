import unittest


from cap1 import strings


class TestOperacoesStrings(unittest.TestCase):
    def test_replace(self):
        for (entrada, esperado) in [
            (('', '', ''), ''),
            (("O|Brasil|faz|parte|do|Mercosul", '|', ' '), "O Brasil faz parte do Mercosul"),
        ]:
            with self.subTest(entrada=entrada):
                self.assertEqual(strings.replace(*entrada), esperado)

    def test_lower(self):
        for (entrada, esperado) in [
            ('PyTHon', 'python'),
            ('Curso de PythonFundamentals', 'curso de pythonfundamentals'),
            ('4520', '4520'),
        ]:
            with self.subTest(entrada=entrada):
                self.assertEqual(strings.lower(entrada), esperado)

    def test_upper(self):
        for (entrada, esperado) in [
            ('PyTHon', 'PYTHON'),
            ('Curso de PythonFundamentals', 'CURSO DE PYTHONFUNDAMENTALS'),
            ('4520', '4520'),
        ]:
            with self.subTest(entrada=entrada):
                self.assertEqual(strings.upper(entrada), esperado)

    def test_format(self):
        for (entrada, esperado) in [
            (("", (), {}), ""),
            (("Curso {} de {} da {}", (4520, 'Python Fundamentals', '4Linux'), {}),
             "Curso 4520 de Python Fundamentals da 4Linux"),
            (("Curso {2} de {0} da {1}", ('Python Fundamentals', '4Linux', 4520), {}),
             "Curso 4520 de Python Fundamentals da 4Linux"),
            (("Curso {id} de {nome} da {empresa}", (), {'id': 520, 'nome': 'Python', 'empresa': '4L'}),
             "Curso 520 de Python da 4L"),
        ]:
            with self.subTest(entrada=entrada):
                self.assertEqual(strings.format(entrada[0], *entrada[1], **entrada[2]),
                                 esperado)
