saludo = "SaludoGlobal"


def saludar():
    global saludo
    saludo = "hola mundo"


def saludochanchito():
    saludo = 24
    print("saludo")


print(saludo)
saludar()
print(saludo)
