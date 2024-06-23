from datetime import datetime

def calculadora(operacao, n1, n2): 
    if operacao == "soma":
        return n1 + n2
    elif operacao == "subtracao":
        return n1 - n2
    elif operacao == "multiplicacao":
        return n1 * n2
    else:
        return n1 / n2

print(calculadora("soma", 1, 2))
print(calculadora("subtracao", 1, 2))
print(calculadora("divisao", 1, 2))
print(calculadora("multiplicacao", 1, 2))
