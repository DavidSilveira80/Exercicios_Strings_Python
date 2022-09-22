from unittest import TestCase
"""
Faça um programa que receba uma palavra e entre com um caractere 
e substitua todas as vogais
da palavra dada por esse caractere.
"""


def modifica(nome: str, caracter: str) -> str:
    novo_nome = ""
    for letra in nome:
        if letra in 'aeiouAEIOU':
            letra = caracter

        novo_nome += letra

    return novo_nome


class TestModificaVogais(TestCase):
    def test_vogais_minusculas(self):
        self.assertEqual(modifica('David', '@'), 'D@v@d')

    def test_vogais_maiusculas(self):
        self.assertEqual(modifica('DAVID', '+'), 'D+V+D')

    def test_vogais_minusculas_e_maiusculas(self):
        self.assertEqual(modifica('DaeiouAEIOU', '<>'), 'D<><><><><><><><><><>')
