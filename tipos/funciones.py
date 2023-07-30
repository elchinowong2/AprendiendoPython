def hola(nombre, apellido):
    print("hola mundo")
    print(f"ultimo fight {nombre} {apellido} ")


hola("hola", "Wong")


hola(apellido="Wong", nombre="Orlando")


def get_idCliente(**cliente):
    print(cliente)
    print(cliente["ID"])


get_idCliente(nombre="orlando", ID="222222222")
