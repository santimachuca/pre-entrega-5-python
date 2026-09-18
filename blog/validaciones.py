from .modelos import crear_post_desde_dict


def validar_post(post):
    # Usamos las mismas reglas para crear, cargar y validar publicaciones.
    try:
        crear_post_desde_dict(post)
    except ValueError as error:
        return False, str(error)
    return True, "El post es valido."


def validar_posts(lista):
    print("\n--- VALIDACION DE POSTS ---")
    if not lista:
        print("No hay posts para validar.")
    for numero, post in enumerate(lista, start=1):
        es_valido, mensaje = validar_post(post)
        titulo = post.get("titulo", "Sin titulo") if isinstance(post, dict) else "Sin titulo"
        if es_valido:
            print(f'Post {numero} - "{titulo}": VALIDO')
        else:
            print(f'Post {numero} - "{titulo}": INVALIDO')
            print("Motivo:", mensaje)
