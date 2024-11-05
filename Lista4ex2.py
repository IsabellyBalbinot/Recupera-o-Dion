def imprimir_piramide(n, crescente=True):
    for i in range(1, n + 1):
        if crescente:
            linha = list(range(1, i + 1))  
        else:
            linha = list(range(i, 0, -1)) 
        print(" ".join(map(str, linha)).center(n * 2))
imprimir_piramide(5) 
print("\n")
imprimir_piramide(5, crescente=False) 