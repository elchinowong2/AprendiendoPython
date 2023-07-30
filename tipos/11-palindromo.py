def no_space(texto):
    nuevo_texto = ""
    for letra in texto:
        if letra != " ":
            nuevo_texto += letra
    return nuevo_texto


def reverso(texto):
    texto_al_reves = ""
    for i in texto:
        texto_al_reves = i + texto_al_reves
    return texto_al_reves


palabra = "orlando wong"
print(no_space(palabra))
print(reverso(palabra))
