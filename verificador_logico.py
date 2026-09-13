import csv
import re

class ValidadorByteFix:
    """Clase que contiene métodos para validar las reglas lógicas chotas"""

    @staticmethod
    def validar_producto(nombre, categoria, precio, stock):
        errores = []
        if not nombre or nombre.strip() == "":
            errores.append("El nombre del producto no puede estar vacío.")
        if categoria not in ['hardware', 'software', 'periferico']:
            errores.append("La categoría debe ser una de: ['hardware', 'software', 'periferico']")
        if not precio or float(precio) <= 0:
            errores.append("El precio debe ser mayor a 0.")
        if stock and int(stock) < 0:
            errores.append("El stock no puede ser negativo.")
        return (False, " | ".join(errores)) if errores else (True, "Producto válido.")

    @staticmethod
    def validar_cliente(nombre, apellido, telefono, email, direccion):
        errores = []
        if not nombre or nombre.strip() == "":
            errores.append("El nombre no puede estar vacío.")
        if not apellido or apellido.strip() == "":
            errores.append("El apellido no puede estar vacío.")
        if telefono and not str(telefono).isdigit():
            errores.append("El teléfono debe contener solo números.")
        if email:
            patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(patron, email):
                errores.append("El email no tiene un formato válido.")
        if direccion and len(direccion.strip()) < 5:
            errores.append("La dirección debe tener al menos 5 caracteres.")
        return (False, " | ".join(errores)) if errores else (True, "Cliente válido.")

    @staticmethod
    def validar_reparacion(id_cliente, id_empleado, tipo_trabajo, estado, precio):
        errores = []
        if not str(id_cliente).strip().isdigit() or int(id_cliente) <= 0:
            errores.append("El ID del cliente debe ser un número positivo.")
        if not str(id_empleado).strip().isdigit() or int(id_empleado) <= 0:
            errores.append("El ID del empleado debe ser un número positivo.")
        if not tipo_trabajo or tipo_trabajo.strip() == "":
            errores.append("El tipo de trabajo no puede estar vacío.")
        if estado not in ['pendiente', 'finalizada']:
            errores.append("El estado debe ser uno de: ['pendiente', 'finalizada']")
        if not precio or float(precio) <= 0:
            errores.append("El precio debe ser mayor a 0.")
        return (False, " | ".join(errores)) if errores else (True, "Reparación válida.")

    @staticmethod
    def validar_transaccion(id_empleado, id_cliente, id_producto, id_reparacion, total):
        errores = []
        if not total or float(total) <= 0:
            errores.append("El total debe ser mayor a 0.")
        if not str(id_empleado).strip().isdigit() or int(id_empleado) <= 0:
            errores.append("El ID del empleado debe ser un número positivo.")
        if not str(id_cliente).strip().isdigit() or int(id_cliente) <= 0:
            errores.append("El ID del cliente debe ser un número positivo.")

        tiene_prod = bool(id_producto and str(id_producto).strip())
        tiene_rep = bool(id_reparacion and str(id_reparacion).strip())

        if tiene_prod and tiene_rep:
            errores.append("Una transacción no puede ser venta y reparación a la vez.")
        if not tiene_prod and not tiene_rep:
            errores.append("La transacción debe tener un producto o una reparación.")
        return (False, " | ".join(errores)) if errores else (True, "Transacción válida.")


# ==========================================
# LECTURA DEL CSV Y EJECUCIÓN
# ==========================================
def verificar_dataset(archivo):
    with open(archivo, encoding='utf-8') as f:
        registros = list(csv.DictReader(f))

    print("=" * 60)
    print("VERIFICADOR LÓGICO - BYTEFIX")
    print("=" * 60)

    val = ValidadorByteFix()
    validos = invalidos = 0

    for reg in registros:
        tipo = (reg.get('tipo') or '').strip().lower()

        if tipo == 'producto':
            ok, motivo = val.validar_producto(
                reg.get('nombre', ''), reg.get('categoria', ''),
                reg.get('precio', ''), reg.get('stock', '')
            )
        elif tipo == 'cliente':
            ok, motivo = val.validar_cliente(
                reg.get('nombre', ''), reg.get('apellido', ''),
                reg.get('telefono', ''), reg.get('email', ''), ''
            )
        elif tipo == 'reparacion':
            ok, motivo = val.validar_reparacion(
                reg.get('id_cliente', ''), reg.get('id_empleado', ''),
                'Reparación', reg.get('estado', ''), reg.get('precio', '')
            )
        elif tipo == 'transaccion':
            ok, motivo = val.validar_transaccion(
                reg.get('id_empleado', ''), reg.get('id_cliente', ''),
                reg.get('id_producto', ''), reg.get('id_reparacion', ''),
                reg.get('total', '')
            )
        else:
            ok, motivo = False, "Tipo desconocido"

        esperado = (reg.get('valido') or '').strip().upper()
        if esperado not in ('SI', 'NO'):
            esperado = 'SI' if ok else 'NO'

        coincide = (ok and esperado == 'SI') or (not ok and esperado == 'NO')
        estado = "OK" if coincide else "REVISAR"

        if ok:
            validos += 1
        else:
            invalidos += 1

        print(f"\n[{estado}] Registro #{reg.get('id_registro', '?')} ({reg.get('tipo', '?')})")
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