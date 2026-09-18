import json
from pathlib import Path

from blog.modelos import Post, crear_post_desde_dict


# Ubica el JSON en la carpeta del proyecto, aunque ejecutes desde otra carpeta.
DATABASE_FILE = Path(__file__).resolve().parent.parent / "posts.json"


def guardar_posts(lista_posts, ruta=DATABASE_FILE):
    """Convierte los objetos Post a diccionarios y los guarda en JSON."""
    try:
        datos = []
        for post in lista_posts:
            if not isinstance(post, Post):
                raise ValueError("Solo se pueden guardar objetos Post.")
            datos_post = post.to_dict()
            crear_post_desde_dict(datos_post)
            datos.append(datos_post)

        # Serializamos antes de abrir para no borrar el JSON si hay un error.
        contenido = json.dumps(datos, indent=4, ensure_ascii=False)
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
    except (OSError, TypeError, ValueError, AttributeError) as error:
        print(f"No se pudieron guardar los posts: {error}")
        return False

    return True


def cargar_posts(ruta=DATABASE_FILE):
    """Lee los diccionarios del JSON y reconstruye los objetos Post y Autor."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        # El archivo debe contener una lista, incluso si solo hay un post.
        if not isinstance(datos, list):
            raise ValueError("El archivo debe contener una lista de posts.")

        posts_recuperados = []
        for datos_post in datos:
            posts_recuperados.append(crear_post_desde_dict(datos_post))

        return posts_recuperados

    except FileNotFoundError:
        # En la primera ejecucion todavia puede no existir el archivo.
        return []
    except (OSError, UnicodeError, ValueError) as error:
        # JSONDecodeError tambien es ValueError: cubre JSON vacio o mal escrito.
        print(f"No se pudieron cargar los posts: {error}")
        return []


# Datos de ejemplo de la preentrega anterior; el menu actual usa el JSON.
perfil_autor = {
    "nombre": "Patrick Jane",
    "bio": "Consultor experto en observar personas y resolver crimenes.",
    "especialidad": "Investigacion y lectura del comportamiento",
    "redes_sociales": ["@patrick_jane", "@consultor_cbi"]
}

estados_post = (
    "borrador",
    "publicado",
    "archivado"
)

etiquetas_blog = {
    "Investigacion",
    "Psicologia",
    "Observacion",
    "Datos"
}
    
posts = [
    {
        "id": 1,
        "titulo": "El misterio de la mansion",
        "contenido": "Analisis de las pistas encontradas en una antigua mansion.",
        "autor": perfil_autor,
        "tags": ["Investigacion", "Observacion"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Las pistas de Red John",
        "contenido": "Una recopilacion de indicios relacionados con Red John.",
        "autor": perfil_autor,
        "tags": ["Investigacion", "Psicologia"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "El arte de observar",
        "contenido": "Como prestar atencion a los detalles del comportamiento.",
        "autor": perfil_autor,
        "tags": ["Observacion", "Psicologia"],
        "estado": "archivado"
    }
]
