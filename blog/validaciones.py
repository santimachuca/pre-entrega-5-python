from .datos import estados_post


def validar_post(post):
    if not isinstance(post, dict):
        return False, "El post no es un diccionario."

    claves_obligatorias = (
        "id",
        "titulo",
        "contenido",
        "autor",
        "tags",
        "estado"
    )

    for clave in claves_obligatorias:
        if clave not in post:
            return False, f'Falta el dato obligatorio: "{clave}".'

    titulo = post.get("titulo")

    if not isinstance(titulo, str) or titulo.strip() == "":
        return False, "El titulo no es valido."

    contenido = post.get("contenido")

    if not isinstance(contenido, str) or contenido.strip() == "":
        return False, "El contenido no es valido."

    autor = post.get("autor")

    if not isinstance(autor, dict):
        return False, "El autor debe ser un diccionario."

    nombre_autor = autor.get("nombre")

    if not isinstance(nombre_autor, str) or nombre_autor.strip() == "":
        return False, "El autor debe tener un nombre."

    if not isinstance(post.get("tags"), list):
        return False, "Los tags deben estar dentro de una lista."

    if post.get("estado") not in estados_post:
        return False, "El estado no esta permitido."

    return True, "El post es valido."


def validar_posts(lista):
    print("\n--- VALIDACION DE POSTS ---")

    for numero, post in enumerate(lista, start=1):
        es_valido, mensaje = validar_post(post)
        titulo = post.get("titulo", "Sin titulo")

        if es_valido:
            print(f'Post {numero} - "{titulo}": VALIDO')
        else:
            print(f'Post {numero} - "{titulo}": INVALIDO')
            print("Motivo:", mensaje)