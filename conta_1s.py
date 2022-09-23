"""
Faça um programa que conte o número de 1’s que aparecem em um 'string'. Exemplo: ´
0011001 -> 3
"""


def conta_1(binario: str) -> int:

    resp = binario.count('1')
    return resp


assert conta_1('0011001') == 3
assert conta_1('00001') == 1
