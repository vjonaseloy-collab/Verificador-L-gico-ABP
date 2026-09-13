## 📁 Archivos del proyecto

| Archivo | Descripción |
|---------|-------------|
| `verificador_logico.py` | Script principal que aplica las reglas lógicas |
| `dataset_bytefix.csv` | Dataset con 28 registros de ejemplo |
| `README.md` | Este archivo |

---

## 🧠 Reglas lógicas aplicadas

### Productos

| Regla | Descripción |
|-------|-------------|
| — | El nombre no puede estar vacío |
| — | La categoría debe ser `hardware`, `software` o `periferico` |
| — | El precio debe ser mayor a 0 |
| — | El stock no puede ser negativo |

### Clientes

| Regla | Descripción |
|-------|-------------|
| — | El nombre no puede estar vacío |
| — | El apellido no puede estar vacío |
| — | El teléfono debe contener solo números |
| — | El email debe tener formato válido |
| — | La dirección debe tener al menos 5 caracteres |

### Reparaciones

| Regla | Descripción |
|-------|-------------|
| — | El ID del cliente debe ser un número positivo |
| — | El ID del empleado debe ser un número positivo |
| — | El tipo de trabajo no puede estar vacío |
| — | El estado debe ser `pendiente` o `finalizada` |
| — | El precio debe ser mayor a 0 |

### Transacciones

| Regla | Descripción |
|-------|-------------|
| — | El total debe ser mayor a 0 |
| — | El ID del empleado debe ser un número positivo |
| — | El ID del cliente debe ser un número positivo |
| — | Debe tener producto XOR reparación (no ambos, no ninguno) |

## 📊 Estructura del dataset

El archivo `dataset_bytefix.csv` contiene las siguientes columnas:
id_registro, tipo, nombre, apellido, categoria, precio, stock,
email, telefono, estado, total, id_producto, id_reparacion,
id_cliente, id_empleado, valido

- **tipo**: `producto`, `cliente`, `reparacion` o `transaccion`
- **valido**: `SI` o `NO` (resultado esperado)
- Los campos que no aplican a un tipo de registro quedan vacíos (como por ejemplo el campo de apellido queda vacio en el registro de un producto,
o el campo de ID_Producto queda vacio en el registro de Clientes).

