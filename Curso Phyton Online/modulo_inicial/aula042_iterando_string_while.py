frase = "O python é uma linguagem de promagração " \
        "multiparadigma. " \
        "Python foi criado por Guido van Rossum. "

i = 0
qtd_apareceu_mais_vezes = 0 
letra_apareceu_mais_vezes = " "

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    qtb_atual = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < qtb_atual:
        qtd_apareceu_mais_vezes = qtb_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print("A letra que apareceu mais vezes foi '", letra_apareceu_mais_vezes, "' que apareceu ", qtd_apareceu_mais_vezes,"x")