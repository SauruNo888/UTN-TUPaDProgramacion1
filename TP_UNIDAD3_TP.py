print("EJERCICIO 1")
nombre = input("Nombre del cliente: ")

while not nombre.isalpha():
    print("Nombre incorrecto")
    nombre = input("Nombre del cliente: ")

cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) == 0:
    print("Cantidad incorrecta")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)

total = 0
total_descuento = 0

for i in range(cantidad):
    precio = input("Precio del producto: ")

    while not precio.isdigit():
        print("Precio incorrecto")
        precio = input("Precio del producto: ")

    precio = int(precio)
    total = total + precio

    descuento = input("Descuento (S/N): ")

    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Respuesta incorrecta")
        descuento = input("Descuento (S/N): ")

    if descuento.lower() == "s":
        precio = precio * 0.90

    total_descuento = total_descuento + precio

ahorro = total - total_descuento
promedio = total_descuento / cantidad

print("Cliente:", nombre)
print("Total sin descuentos: $", total)
print(f"Total con descuentos: ${total_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")



print("EJERCICIO 2")
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:
    print("Intento", intentos + 1, "/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")

    intentos += 1

if acceso == False:
    print("Cuenta bloqueada")
else:
    opcion = ""

    while opcion != "4":
        print()
        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        while int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: ingrese un número válido.")
                opcion = input("Opción: ")

        if opcion == "1":
            print("Inscripto")

        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")

            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")

            confirmacion = input("Confirmar clave: ")

            while nueva_clave != confirmacion:
                print("Las claves no coinciden.")
                confirmacion = input("Confirmar clave: ")

            clave_correcta = nueva_clave
            print("Clave cambiada correctamente.")

        elif opcion == "3":
            print("¡Sigue adelante, cada esfuerzo te acerca a tu objetivo!")

        elif opcion == "4":
            print("Sesión finalizada.")



print("EJERCICIO 3")
operador = input("Nombre del operador: ")

while not operador.isalpha():
    print("Nombre incorrecto")
    operador = input("Nombre del operador: ")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = ""

while opcion != "5":

    print()
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Ingrese un número válido")
        opcion = input("Opción: ")

    while int(opcion) < 1 or int(opcion) > 5:
        print("Opción fuera de rango")
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Ingrese un número válido")
            opcion = input("Opción: ")

    if opcion == "1":

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Día incorrecto")
            dia = input("Día (1=Lunes, 2=Martes): ")

        nombre = input("Nombre del paciente: ")

        while not nombre.isalpha():
            print("Nombre incorrecto")
            nombre = input("Nombre del paciente: ")

        if dia == "1":

            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("El paciente ya tiene un turno ese día.")

            elif lunes1 == "":
                lunes1 = nombre
                print("Turno reservado.")

            elif lunes2 == "":
                lunes2 = nombre
                print("Turno reservado.")

            elif lunes3 == "":
                lunes3 = nombre
                print("Turno reservado.")

            elif lunes4 == "":
                lunes4 = nombre
                print("Turno reservado.")

            else:
                print("No hay turnos disponibles.")

        else:

            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("El paciente ya tiene un turno ese día.")

            elif martes1 == "":
                martes1 = nombre
                print("Turno reservado.")

            elif martes2 == "":
                martes2 = nombre
                print("Turno reservado.")

            elif martes3 == "":
                martes3 = nombre
                print("Turno reservado.")

            else:
                print("No hay turnos disponibles.")

    elif opcion == "2":

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Día incorrecto")
            dia = input("Día (1=Lunes, 2=Martes): ")

        nombre = input("Nombre del paciente: ")

        while not nombre.isalpha():
            print("Nombre incorrecto")
            nombre = input("Nombre del paciente: ")

        encontrado = False

        if dia == "1":

            if nombre == lunes1:
                lunes1 = ""
                encontrado = True

            elif nombre == lunes2:
                lunes2 = ""
                encontrado = True

            elif nombre == lunes3:
                lunes3 = ""
                encontrado = True

            elif nombre == lunes4:
                lunes4 = ""
                encontrado = True

        else:

            if nombre == martes1:
                martes1 = ""
                encontrado = True

            elif nombre == martes2:
                martes2 = ""
                encontrado = True

            elif nombre == martes3:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado.")
        else:
            print("Paciente no encontrado.")

    elif opcion == "3":

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Día incorrecto")
            dia = input("Día (1=Lunes, 2=Martes): ")

        if dia == "1":

            print("Agenda del Lunes:")
            
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)

        else:

            print("Agenda del Martes:")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)

    elif opcion == "4":

        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        print("Lunes:", ocupados_lunes, "ocupados,", 4 - ocupados_lunes, "disponibles")
        print("Martes:", ocupados_martes, "ocupados,", 3 - ocupados_martes, "disponibles")

        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos es Lunes.")
        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos es Martes.")
        else:
            print("Hay empate entre Lunes y Martes.")

print("Sistema cerrado.")



print("EJERCICIO 4")
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

nombre = input("Nombre del agente: ")

while not nombre.isalpha():
    print("Nombre incorrecto")
    nombre = input("Nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:

    print()
    print("Agente:", nombre)
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Código:", codigo_parcial)

    print()
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Opción incorrecta")
        opcion = input("Opción: ")

    if opcion == "1":

        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        if forzar_seguidas == 3:
            print("La cerradura se trabó.")
            alarma = True

        elif energia < 40:

            numero = input("Riesgo de alarma. Elige un número del 1 al 3: ")

            while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                print("Número incorrecto")
                numero = input("Elige un número del 1 al 3: ")

            if numero == "3":
                alarma = True
                print("¡Alarma activada!")

            else:
                cerraduras_abiertas += 1
                print("Cerradura abierta.")

        else:
            cerraduras_abiertas += 1
            print("Cerradura abierta.")

    elif opcion == "2":

        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        print("Hackeando panel...")

        for i in range(4):
            codigo_parcial += "A"
            print("Paso", i + 1, "- Código:", codigo_parcial)

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡El código abrió una cerradura!")

    elif opcion == "3":

        forzar_seguidas = 0
        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma == True:
            energia -= 10
            print("Descansar con alarma activa cuesta 10 de energía extra.")

        print("Descansaste.")

    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print()
        print("¡La alarma bloqueó la bóveda!")
        break

print()

if cerraduras_abiertas == 3:
    print("¡VICTORIA!")
    print("Abriste las 3 cerraduras.")

elif alarma == True and tiempo <= 3:
    print("¡DERROTA!")
    print("La bóveda quedó bloqueada por la alarma.")

elif energia <= 0 or tiempo <= 0:
    print("¡DERROTA!")
    print("Te quedaste sin energía o sin tiempo.")



print("EJERCICIO 5")
print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
daño_enemigo = 12
turno_jugador = True
juego_activo = True

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    print()
    print(nombre, "(HP:", vida_jugador, ") vs Enemigo (HP:", vida_enemigo, ")")
    print("Pociones:", pociones)

    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    if opcion == "1":

        if vida_enemigo < 20:
            daño = ataque_pesado * 1.5
            print("¡Golpe Crítico!")
        else:
            daño = ataque_pesado

        vida_enemigo -= daño

        print("¡Atacaste al enemigo por", daño, "puntos de daño!")

    elif opcion == "2":

        print(">> ¡Inicias una ráfaga de golpes!")

        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == "3":

        if pociones > 0:
            vida_jugador += 30

            if vida_jugador > 100:
                vida_jugador = 100

            pociones -= 1

            print("¡Te curaste 30 puntos de vida!")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo <= 0:
        break

    vida_jugador -= daño_enemigo

    print("¡El enemigo te atacó por 12 puntos de daño!")

print()

if vida_jugador > 0:
    print("¡VICTORIA!", nombre, "ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
