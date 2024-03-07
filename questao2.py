#calculo de Fibonacci

def fibonacci(n, f_sequencia):
    if n == 0:
        f_sequencia.append(0)
        return 0
    elif n == 1:
        f_sequencia.append(1)
        return 1
    else:
        f = fibonacci(n-1, f_sequencia) + fibonacci(n-2, f_sequencia)
        f_sequencia.append(f)
        return f

def verifica_f(n):
    f_sequencia = []
    fibonacci_resultado = fibonacci(n, f_sequencia)
    r = False
    
    for i in range(len(f_sequencia)):
        if f_sequencia[i] == n:
            r = True
            break

    if r:
        return "O número existe na sequência\n"
    else:
        return "O número NÃO existe na sequência\n"


n = int(input("Digite um número: "))
print(verifica_f(n))