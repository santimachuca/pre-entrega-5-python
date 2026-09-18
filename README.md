# Preentrega 6 - Blog por consola con POO y JSON

Sistema de blog desarrollado en Python y organizado mediante modulos y paquetes. Esta version refactoriza la preentrega 5 utilizando programacion orientada a objetos (POO) y persistencia JSON.

El programa permite administrar publicaciones mediante un menu interactivo y recuperarlas en futuras ejecuciones.

## Funcionalidades

1. Ver todos los posts.
2. Buscar posts por titulo.
3. Filtrar posts por tag.
4. Validar la estructura de los posts.
5. Guardar posts en JSON.
6. Salir del programa.
7. Crear un post.

Las busquedas y los filtros ignoran las diferencias entre mayusculas y minusculas.

## Estructura del proyecto

```text
Pre-entrega-6-repo/
├── main.py
├── prueba_modelos.py
├── README.md
├── posts.json              # Se crea al guardar desde el menu
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

- `main.py`: carga los posts, crea el objeto Blog y controla el menu y la creacion de publicaciones.
- `blog/__init__.py`: permite que la carpeta `blog` funcione como un paquete de Python.
- `blog/datos.py`: carga y guarda publicaciones en posts.json; tambien conserva datos y constantes de la version anterior.
- `blog/menu.py`: muestra el menu y recibe los datos ingresados por el usuario.
- `blog/modelos.py`: define Autor, Post y Blog, convierte objetos a diccionarios y reconstruye objetos validando los datos recibidos.
- `blog/operaciones.py`: conserva las funciones de la preentrega 5; el menu actual utiliza los metodos de Blog para listar, buscar y filtrar.
- `blog/validaciones.py`: comprueba que cada post tenga las claves y los tipos de datos requeridos.
- `prueba_modelos.py`: prueba los modelos, las busquedas, los filtros y la conversion entre objetos y diccionarios. No guarda publicaciones en posts.json.
- `posts.json`: almacena las publicaciones guardadas para recuperarlas en otra ejecucion.

## Requisitos

- Python 3.
- No requiere librerias externas.

## Ejecucion

Abrir una terminal en la carpeta raiz del proyecto y ejecutar:

```powershell
python main.py
```

El archivo que debe ejecutarse es `main.py`. Para probar los modelos por separado:

```powershell
python prueba_modelos.py
```

## Datos utilizados

En memoria, cada publicacion es un objeto Post que contiene:

- ID.
- Titulo.
- Contenido.
- Autor.
- Tags.
- Estado.

Autor contiene nombre y biografia. Post contiene un objeto Autor, una lista de tags y los demas atributos indicados. Blog administra una lista de objetos Post.

Para guardar, `to_dict()` convierte los objetos a diccionarios, incluyendo el autor. Al cargar el JSON, los diccionarios se convierten nuevamente en objetos Post y Autor.

Los tags se ingresan separados por comas. Los estados permitidos son `borrador`, `publicado` y `archivado`.

## Guardado y recuperacion

Al iniciar, el programa intenta cargar posts.json desde la carpeta raiz del proyecto. Si no existe, comienza con una lista vacia: no es necesario crearlo manualmente.

Para comprobar la persistencia:

1. Elegir la opcion 7 y completar una publicacion.
2. Elegir la opcion 1 para verla.
3. Elegir la opcion 5 para guardarla en posts.json.
4. Salir con la opcion 6.
5. Ejecutar nuevamente el programa y elegir la opcion 1.

El guardado es manual: hay que elegir la opcion 5 antes de salir para conservar los cambios. Guardar reemplaza el contenido del JSON por la lista actual del blog.

Si el archivo esta vacio, mal escrito o contiene datos invalidos, el programa muestra un mensaje y carga una lista vacia. En ese caso, conviene revisar o respaldar el archivo antes de guardar, porque se reemplazaria su contenido.

## Validaciones

Blog asigna el ID y centraliza la creacion y validacion. Se comprueban titulo, contenido, nombre y biografia del autor, al menos un tag y un estado permitido. Al reconstruir publicaciones desde JSON se aplican las mismas reglas, incluyendo el ID entero positivo y los tipos de los campos. Una opcion de menu invalida muestra un mensaje y permite continuar. La conversion a JSON se comprueba antes de abrir el archivo para evitar reemplazarlo con datos invalidos.

## Autor del proyecto

Santiago Machuca
