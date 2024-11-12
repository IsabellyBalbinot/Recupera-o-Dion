def gerenciar_clientes(clientes_A, clientes_B):
    interseccao = clientes_A.intersection(clientes_B)
    print("Clientes em ambos os conjuntos:", interseccao)
    apenas_A = clientes_A - clientes_B
    print("Clientes apenas em clientes_A:", apenas_A)
    
    apenas_um = clientes_A.symmetric_difference(clientes_B)
    print("Clientes em apenas um dos conjuntos:", apenas_um)
    
    total_clientes = len(clientes_A.union(clientes_B))
    clientes_unicos = len(apenas_um)
    porcentagem_unicos = (clientes_unicos / total_clientes) * 100
    print(f"Porcentagem de clientes únicos: {porcentagem_unicos:.2f}%")

clientes_A = {"Carlos", "Ana", "Beatriz", "Eduardo", "Lucas"}
clientes_B = {"Lucas", "Fernando", "Ana", "Maria", "Paulo"}

gerenciar_clientes(clientes_A, clientes_B)