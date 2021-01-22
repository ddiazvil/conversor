def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 💰

1- Pesos Colombianos
2- Pesos Argentinos
3- Bolívares Soberanos
4- Peso Méxicano

Elige una opción: """  

opcion = int(input(menu))

if opcion == 1:
    conversor("pesos colombianos", 3476)
elif opcion == 2:
    conversor("pesos argentinos", 151)
elif opcion == 3:
    conversor("bolívares soberanos", 1782704)
elif opcion == 4:
    conversor("pesos méxicanos", 19.64)    
else:
    print('Ingresa una opción correcta')

