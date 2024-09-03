def verificar_letra_a(texto):
    quantidade = 0

    for char in texto:
        if char == 'a' or char == 'A':
            quantidade += 1

    if quantidade > 0:
        print(f"A letra 'a' aparece {quantidade} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

texto_usuario = input("Digite uma string: ")
verificar_letra_a(texto_usuario)
