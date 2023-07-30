gas = True
encendido = True
edad = 18

if gas and encendido:
    print("encendido")

if gas or encendido:
    print("encendido")

if not gas or encendido and edad > 10:
    print("encendido")
