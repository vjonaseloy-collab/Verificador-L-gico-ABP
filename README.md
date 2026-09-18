# Verificador Lógico - ByteFix

**ABP de Lógica - ISPC 2026**
**Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial**

---

##  Descripción

Este proyecto implementa un **verificador lógico de registros** para el comercio ficticio **ByteFix**, dedicado a la venta de productos de hardware, software y periféricos, y a la reparación de equipos informáticos.

El script aplica **reglas lógicas** a un conjunto de datos (dataset) y clasifica cada registro como **válido** o **inválido**, mostrando una **explicación en notación lógica formal** de cada decisión.

---

##  Objetivo

Validar la consistencia de datos de productos, clientes, reparaciones y transacciones, aplicando reglas lógicas claras y reproducibles, como parte del ABP de Lógica.

---

##  Archivos del proyecto

| Archivo | Descripción |
|---------|-------------|
| `verificador_logico.py` | Script principal que aplica las reglas lógicas |
| `dataset_bytefix.csv` | Dataset con 12 registros de ejemplo |
| `README.md` | Este archivo |

---

##  Reglas lógicas aplicadas

Las reglas se enumeran una sola vez, aunque se apliquen a más de un tipo de registro.

| Regla | Descripción | Aplica a |
|-------|-------------|----------|
| P | El nombre no puede estar vacío | Productos, Clientes |
| P2 | El apellido no puede estar vacío | Clientes |
| Q | La categoría debe ser `hardware`, `software` o `periferico` | Productos |
| R | El precio debe ser mayor a 0 | Productos, Reparaciones |
| S | El stock no puede ser negativo | Productos |
| T | El teléfono debe contener solo números | Clientes |
| U | El email debe tener formato válido | Clientes |
| V | El estado debe ser `pendiente` o `finalizada` | Reparaciones |
| W | El total debe ser mayor a 0 | Transacciones |
| X | Debe tener producto XOR reparación (no ambos, no ninguno) | Transacciones |
| ID | Los IDs deben ser números positivos | Reparaciones, Transacciones |

