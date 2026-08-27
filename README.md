# Preentrega 5 - Blog por consola

Sistema de blog desarrollado en Python y organizado mediante modulos y paquetes.

El programa utiliza un menu interactivo que permite listar publicaciones, buscar posts por titulo, filtrar por tag y validar la estructura de los datos.

## Funcionalidades

1. Ver todos los posts.
2. Buscar posts por titulo.
3. Filtrar posts por tag.
4. Validar la estructura de los posts.
5. Salir del programa.

Las busquedas y los filtros ignoran las diferencias entre mayusculas y minusculas.

## Estructura del proyecto

```text
Pre-entrega-5/
├── main.py
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

- `main.py`: inicia el programa, controla el menu y conecta los diferentes modulos.
- `blog/__init__.py`: permite que la carpeta `blog` funcione como un paquete de Python.
- `blog/datos.py`: contiene el perfil del autor, los estados permitidos, las etiquetas y la lista de posts.
- `blog/menu.py`: muestra el menu y recibe los datos ingresados por el usuario.
- `blog/operaciones.py`: contiene las funciones para listar, buscar y filtrar posts.
- `blog/validaciones.py`: comprueba que cada post tenga las claves y los tipos de datos requeridos.

## Requisitos

- Python 3.
- No requiere librerias externas.

## Ejecucion

Abrir una terminal en la carpeta raiz del proyecto y ejecutar:

```powershell
python main.py
```

El archivo que debe ejecutarse es `main.py`.

## Datos utilizados

Cada post se representa mediante un diccionario que contiene:

- ID.
- Titulo.
- Contenido.
- Autor.
- Tags.
- Estado.

El autor se guarda como un diccionario anidado dentro de cada post.

## Autor del proyecto

Santiago Machuca