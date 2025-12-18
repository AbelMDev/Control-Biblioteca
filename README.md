# 🧮 Control - Biblioteca: Proyecto Final Programación III

El objetivo de este proyecto es desarrollar una aplicación de escritorio simple para la gestión de una pequeña biblioteca utilizando Python y el framework Flet (flet.dev). La interfaz de usuario debe ser intuitiva y reactiva, siguiendo el patrón de la aplicación de ejemplo de To-Do List de Flet, donde las diferentes funcionalidades se manejan como "tareas" o "vistas" dentro de la aplicación principal.

## 👨‍💻 Desarrolladores

- **Abel Murgas**  
- **Indira Perez**  
- **Cristian Pinzón**

## 📘 Requisitos Funcionales

La aplicación debe contar con tres secciones principales:

1. **Gestión de Libros**
Esta sección debe permitir al usuario gestionar el inventario de libros de la biblioteca.

- Registro de Libros:
    - Debe haber un formulario o campo de entrada para agregar nuevos libros.
    - Los campos a registrar obligatoriamente son: Título, Autor y ISBN (como identificador único).
    - Al registrar, el libro debe tener un estado inicial de "Disponible".

- Visualización del Inventario:

    - Mostrar una lista de todos los libros registrados, incluyendo su Título, Autor, e Estado (Disponible o Prestado).

    - La lista debe actualizarse dinámicamente al agregar nuevos libros o al cambiar su estado.

2. Gestión de Clientes
Esta sección se encargará de registrar y listar a los usuarios de la biblioteca.

- Registro de Clientes:

    - Debe haber un formulario para ingresar nuevos clientes.

    - Los campos obligatorios son: Nombre, Apellido y Cédula/ID (como identificador único).

- Visualización de Clientes:

    - Mostrar una lista de todos los clientes registrados, incluyendo su Nombre, Apellido y Cédula.

3. Préstamo de Libros
Esta es la funcionalidad central del sistema.

- Realizar Préstamo:

    - El usuario debe poder seleccionar un libro de la lista de libros disponibles.

    - El usuario debe poder seleccionar un cliente de la lista de clientes existentes (por ejemplo, buscándolo por su Cédula o seleccionándolo de un Dropdown).

    - Al confirmar el préstamo, el estado del libro seleccionado debe cambiar a "Prestado".

    - Se debe registrar qué cliente tiene el libro (asociación entre libro y cliente).

    - Debe haber una validación para asegurar que solo se puedan prestar libros con estado "Disponible".

- Devolución de Libros (Opcional Avanzado):

    - Debe permitir seleccionar un libro prestado y cambiar su estado de vuelta a "Disponible".
---
## 📂 Estructura del Proyecto
```
CONTROL-BIBLIOTECA/

├── assets/ # Recursos gráficos (íconos)
├── db/ # Configuración e inicialización de la base de datos
├── models/ # Modelos de dominio
├── repositories/ # Acceso a datos
├── services/ # Lógica de negocio
├── storage/ # Archivos temporales y persistencia auxiliar
├── ui/ # Tema, componentes y layouts
├── views/ # Vistas de la aplicación
│
├── biblioteca.db # Base de datos SQLite
├── ER diagrama.png # Diagrama entidad–relación
├── main.py # Punto de entrada de la aplicación
├── requirements.txt # Dependencias del proyecto
└── README.md
```


---

## 🚀 Ejecución Local

```bash
git clone https://github.com/AbelMDev/Control-Biblioteca
cd CONTROL-BIBLIOTECA

python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Linux / macOS

pip install -r requirements.txt
flet run main.py
```
## 🧾 Dependencias Principales
- Flet – Framework para interfaces gráficas multiplataforma

- SQLAlchemy – ORM para gestión de base de datos

- SQLite – Base de datos local

- Python 3.10+

## 🧠 Arquitectura
El sistema sigue una arquitectura en capas, lo que garantiza mantenibilidad, escalabilidad y separación de responsabilidades:

- Modelos: representación de entidades

- Repositorios: acceso y persistencia de datos

- Servicios: reglas de negocio

- Vistas: interfaz gráfica

- UI: tema visual y componentes reutilizables

## 📌 Funcionalidades Principales
- Registro y listado de libros

- Registro y listado de clientes

- Préstamo de libros disponibles

- Devolución de libros prestados

- Validaciones de estado y disponibilidad

- Persistencia automática en base de datos

## 🖥️ Plataforma
- Aplicación de escritorio

- bOptimizada para Windows

- Base de datos local integrada

## 📄 Notas
- La base de datos se crea automáticamente al iniciar la aplicación

- El ícono de la aplicación se carga desde la carpeta assets

- El diseño visual se centraliza en el módulo ui
