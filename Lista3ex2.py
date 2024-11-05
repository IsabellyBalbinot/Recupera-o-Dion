
def e_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos(n):
    primos = []
    for num in range(1, n + 1):
        if e_primo(num):
            primos.append(num)
    return primos

try:
    n = int(input("Digite um número inteiro: "))
    print(f"Números primos entre 1 e {n}: {numeros_primos(n)}")
except ValueError:
    print("insira um número inteiro válido!")
