"""
Faça um programa que receba uma palavra e a imprima de trás-para-frente.
"""


def inverte_string(palavra: str) -> str:
    resp = ''
    for i in range(len(palavra)):
        resp += palavra[-(i + 1)]
    return resp


if __name__ == '__main__':
    assert inverte_string('casa') == 'asac'

print(inverte_string('casa'))