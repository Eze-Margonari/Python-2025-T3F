A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


print("Elementos que se encuentran en A o en B, o en ambos:", A | B)

print("Elementos que se encuentran en A y en B:", A & B)

print("Elementos que se encuentran en A o en B, pero no en ambos:", A ^ B)

print("Es A un subconjunto de B?:", "Sí" if A <= B else "No" )

print("Número de elementos en A:", len(A))