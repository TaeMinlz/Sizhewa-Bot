from datetime import datetime

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad

# Ejemplo de uso:
fecha_nacimiento = datetime(1990, 1, 1)
edad = calcular_edad(fecha_nacimiento)
print(f"La edad es: {edad} años")
