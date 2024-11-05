class Produto:
    preco = 0.0
    nome = ""
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_info(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco: .2f}")


produto1 = Produto("Caneta", 1.50)
produto2 = Produto("Caderno", 5.00)

produto1.exibir_info()
produto2.exibir_info()
