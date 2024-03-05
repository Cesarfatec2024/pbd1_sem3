import calculadora
print (calculadora.somar(1, 2))
print (calculadora.subtrair(1, 2))
print (calculadora.multiplicar(1, 2))
print (calculadora.dividir(1, 2))
print (calculadora.sair())

def menu():
    a = 1
    b = 2
    soma = calculadora.somar(a, b)
    subtracao = calculadora.subtrair(a, b)
    produto = calculadora.multiplicar(a, b)
    quociente = calculadora.dividir(a, b)
    saida = calculadora.sair()
    print(f'{a} + {b} = {soma}')
    print(f'{a} - {b} = {subtracao}')
    print(f'{a} * {b} = {produto}')
    print(f'{a} / {b} = {quociente}')
    print({saida})

menu()
