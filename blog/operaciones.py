def listar_posts(lista):
    if not lista:
        print("No hay posts disponibles.")
        return

    print("\n--- POSTS DISPONIBLES ---")

    for post in lista:
        titulo = post.get("titulo", "Sin titulo")
        autor = post.get("autor", {})
        nombre_autor = autor.get("nombre", "Autor desconocido")
        estado = post.get("estado", "Estado desconocido")

        print(
            f"- {titulo} | "
            f"Autor: {nombre_autor} | "
            f"Estado: {estado}"
        )


def buscar_por_titulo(lista, termino):
    termino_limpio = termino.strip().lower()
    resultados = []

    if termino_limpio == "":
        return resultados

    for post in lista:
        titulo = post.get("titulo", "")

        if termino_limpio in titulo.lower():
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    tag_limpio = tag.strip().lower()
    resultados = []

    if tag_limpio == "":
        return resultados

    for post in lista:
        tags = post.get("tags", [])

        for tag_post in tags:
            if tag_limpio == tag_post.lower():
                resultados.append(post)
                break

    return resultados