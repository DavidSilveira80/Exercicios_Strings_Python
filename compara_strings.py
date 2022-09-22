"""
Crie um programa que compara duas 'strings'.
"""


def compara_strings(string1: str, string2: str) -> bool:
    if string1 == string2:
        resp = True
    else:
        resp = False
    return resp


if __name__ == '__main__':
    assert compara_strings('casa', 'prédio') == False
    assert compara_strings('David', 'David') == True
