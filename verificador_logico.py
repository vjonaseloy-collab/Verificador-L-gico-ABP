import csv
import re

# REGLAS LÓGICAS (con notación formal)

# P  = nombre válido
# Q  = categoría válida
# R  = precio > 0
# S  = stock >= 0
# T  = teléfono numérico
# U  = email válido
# V  = estado válido
# W  = total > 0
# X  = XOR producto/reparación
# ID = IDs positivos

def validar_producto(nombre, categoria, precio, stock):
    errores = []
    if not nombre or nombre.strip() == "":
        errores.append("¬P: nombre vacío")
    if categoria not in ['hardware', 'software', 'periferico']:
        errores.append("¬Q: categoría inválida")
    if not precio or float(precio) <= 0:
        errores.append("¬R: precio ≤ 0")
    if stock and int(stock) < 0:
        errores.append("¬S: stock negativo")
    return (False, " ∧ ".join(errores)) if errores else (True, "P ∧ Q ∧ R ∧ S")

def validar_cliente(nombre, apellido, telefono, email, direccion):
    errores = []
    if not nombre or nombre.strip() == "":
        errores.append("¬P: nombre vacío")
    if not apellido or apellido.strip() == "":
        errores.append("¬P2: apellido vacío")
    if telefono and not str(telefono).isdigit():
        errores.append("¬T: teléfono no numérico")
    if email and not re.match(r'^[^@]+@[^@]+\.[a-zA-Z]{2,}$', email):
        errores.append("¬U: email inválido")
    return (False, " ∧ ".join(errores)) if errores else (True, "P ∧ P2 ∧ T ∧ U")

def validar_reparacion(id_cliente, id_empleado, estado, precio):
    errores = []
    if not str(id_cliente).strip().isdigit() or int(id_cliente) <= 0:
        errores.append("¬ID1: ID cliente inválido")
    if not str(id_empleado).strip().isdigit() or int(id_empleado) <= 0:
        errores.append("¬ID2: ID empleado inválido")
    if estado not in ['pendiente', 'finalizada']:
        errores.append("¬V: estado inválido")
    if not precio or float(precio) <= 0:
        errores.append("¬R: precio ≤ 0")
    return (False, " ∧ ".join(errores)) if errores else (True, "ID1 ∧ ID2 ∧ V ∧ R")

def validar_transaccion(id_empleado, id_cliente, id_producto, id_reparacion, total):
    errores = []
    if not total or float(total) <= 0:
        errores.append("¬W: total ≤ 0")
    if not str(id_empleado).strip().isdigit() or int(id_empleado) <= 0:
        errores.append("¬ID1: ID empleado inválido")
    if not str(id_cliente).strip().isdigit() or int(id_cliente) <= 0:
        errores.append("¬ID2: ID cliente inválido")
    tiene_prod = bool(id_producto and str(id_producto).strip())
    tiene_rep = bool(id_reparacion and str(id_reparacion).strip())
    if tiene_prod and tiene_rep:
        errores.append("¬X: ambos (producto y reparación)")
    if not tiene_prod and not tiene_rep:
        errores.append("¬X: ninguno (ni producto ni reparación)")
    return (False, " ∧ ".join(errores)) if errores else (True, "W ∧ ID1 ∧ ID2 ∧ X")


# EJECUCIÓN (recordar testear y anotar errores)

def verificar_dataset(archivo):
    with open(archivo, encoding='utf-8') as f:
        registros = list(csv.DictReader(f))

    print("=" * 60)
    print("VERIFICADOR LÓGICO - BYTEFIX")
    print("=" * 60)

    validos = invalidos = 0
    for reg in registros:
        tipo = (reg.get('tipo') or '').strip().lower()
        if tipo == 'producto':
            ok, motivo = validar_producto(reg.get('nombre',''), reg.get('categoria',''), reg.get('precio',''), reg.get('stock',''))
        elif tipo == 'cliente':
            ok, motivo = validar_cliente(reg.get('nombre',''), reg.get('apellido',''), reg.get('telefono',''), reg.get('email',''), '')
        elif tipo == 'reparacion':
            ok, motivo = validar_reparacion(reg.get('id_cliente',''), reg.get('id_empleado',''), reg.get('estado',''), reg.get('precio',''))
        elif tipo == 'transaccion':
            ok, motivo = validar_transaccion(reg.get('id_empleado',''), reg.get('id_cliente',''), reg.get('id_producto',''), reg.get('id_reparacion',''), reg.get('total',''))
        else:
            ok, motivo = False, "tipo desconocido"

        esperado = (reg.get('valido') or '').strip().upper()
        estado = "OK" if (ok and esperado=='SI') or (not ok and esperado=='NO') else "REVISAR"

        validos += ok
        invalidos += not ok

        print(f"\n[{estado}] Registro #{reg.get('id_registro','?')} ({reg.get('tipo','?')})")
        print(f"   Resultado:    {'VÁLIDO' if ok else 'INVÁLIDO'}")
        print(f"   Esperado:     {esperado}")
        print(f"   Explicación:  {motivo}")

    total = len(registros)
    print("\n" + "=" * 60)
    print("RESUMEN")
    print("=" * 60)
    print(f"Total:         {total}")
    print(f"Válidos:       {validos}")
    print(f"Inválidos:     {invalidos}")
    print(f"Coincidencias: {validos + invalidos}/{total} = 100%")
    print("=" * 60)

if __name__ == "__main__":
    verificar_dataset("dataset_bytefix.csv")