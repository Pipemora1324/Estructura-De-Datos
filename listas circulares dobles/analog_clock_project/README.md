# ⏰ Superhéroe Analog Clock (Lista Circular Doble)

Este es un reloj analógico interactivo hecho con Python y `tkinter`, que representa las horas usando una lista circular doble. Tiene varias funciones visuales personalizables y fue creado como parte de un proyecto académico de estructuras de datos.

## 📚 Características

✅ Representación de las 12 horas con una **lista circular doble**  
✅ Interfaz gráfica usando **Tkinter**  
✅ Reloj analógico con manecillas de segundos, minutos y horas  
✅ Botón para **mostrar u ocultar la hora digital**  
✅ Botón para **mostrar la fecha actual** (Día, Mes, Año)  
✅ Botón para alternar entre **modo claro y oscuro**

## 🧠 Estructura de Datos

Se usa una lista circular doble para representar las 12 horas del reloj. Cada nodo contiene:

- La hora (1 a 12)
- Referencia al nodo anterior (`prev`)
- Referencia al nodo siguiente (`next`)

## 🖼️ Interfaz

La GUI incluye:
- Canvas para el dibujo del reloj
- Botones para controlar el modo visual
- Hora digital (opcional)
- Fecha actual (opcional)

## 📁 Archivos

- `clock_gui.py` – Interfaz gráfica y lógica del reloj  
- `clock_linked_list.py` – Implementación de la lista circular doble

## ▶️ Cómo ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Clona o descarga este repositorio.
3. Navega a la carpeta del proyecto en tu terminal o CMD:
   ```bash
   cd analog_clock_project

Ejecuta el reloj:
    python clock_gui.py

👨‍💻 Requisitos
Python 3.x

Biblioteca estándar (tkinter, time, math, etc.)

❌ No se requieren librerías externas

✨ Autor
Proyecto desarrollado por Juan Felipe Mora Revelo como parte del curso de Estructura de Datos.