class Autor:
    def __init__(self, nombre, bio):
        self.nombre = nombre
        self.bio = bio

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio
        }


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado
        }


class Blog:
    def __init__(self, posts):
        self.posts = posts

    def agregar_post(self, post):
        self.posts.append(post)

    def crear_post(self, titulo, contenido, nombre, bio, tags, estado):
        # El blog asigna el ID y valida antes de agregar la publicacion.
        nuevo_id = 1
        for post in self.posts:
            if post.id >= nuevo_id:
                nuevo_id = post.id + 1

        datos = {
            "id": nuevo_id, "titulo": titulo, "contenido": contenido,
            "autor": {"nombre": nombre, "bio": bio},
            "tags": tags, "estado": estado
        }
        try:
            nuevo_post = crear_post_desde_dict(datos)
        except ValueError as error:
            return False, str(error)

        self.agregar_post(nuevo_post)
        return True, "Post creado. Elegi la opcion 5 para guardarlo."

    def validar_posts(self):
        # Importacion local para evitar un ciclo entre los modulos.
        from blog.validaciones import validar_posts

        datos = []
        for post in self.posts:
            datos.append(post.to_dict())
        validar_posts(datos)

    def listar_posts(self):
        if not self.posts:
            print("No hay posts disponibles.")
            return

        for post in self.posts:
            print(
                f"- {post.titulo} | "
                f"Autor: {post.autor.nombre} | "
                f"Estado: {post.estado}"
            )

    def buscar_por_titulo(self, termino):
        termino_limpio = termino.strip().lower()

        if termino_limpio == "":
            print("La busqueda no puede estar vacia.")
            return []

        resultados = []

        for post in self.posts:
            if termino_limpio in post.titulo.lower():
                resultados.append(post)

        return resultados

    def filtrar_por_tag(self, tag):
        tag_limpio = tag.strip().lower()

        if tag_limpio == "":
            print("El tag no puede estar vacio.")
            return []

        resultados = []

        for post in self.posts:
            for tag_post in post.tags:
                if tag_limpio == tag_post.lower():
                    resultados.append(post)
                    break

        return resultados


def crear_autor_desde_dict(datos):
    if not isinstance(datos, dict):
        raise ValueError("Los datos del autor deben ser un diccionario.")

    if "nombre" not in datos or "bio" not in datos:
        raise ValueError("Faltan datos obligatorios del autor.")

    if not isinstance(datos["nombre"], str) or datos["nombre"].strip() == "":
        raise ValueError("El nombre del autor debe ser un texto no vacio.")

    if not isinstance(datos["bio"], str) or datos["bio"].strip() == "":
        raise ValueError("La biografia del autor debe ser un texto no vacio.")

    return Autor(
        datos["nombre"],
        datos["bio"]
    )


def crear_post_desde_dict(datos):
    if not isinstance(datos, dict):
        raise ValueError("Los datos del post deben ser un diccionario.")

    claves_obligatorias = (
        "id", "titulo", "contenido", "autor", "tags", "estado"
    )

    for clave in claves_obligatorias:
        if clave not in datos:
            raise ValueError(f"Falta el dato obligatorio: {clave}.")

    # Validamos antes de crear el objeto para evitar errores en el menu.
    # bool es un subtipo de int en Python, pero no sirve como ID.
    if (not isinstance(datos["id"], int)
            or isinstance(datos["id"], bool)
            or datos["id"] <= 0):
        raise ValueError("El ID debe ser un numero entero positivo.")

    for campo in ("titulo", "contenido"):
        if not isinstance(datos[campo], str) or datos[campo].strip() == "":
            raise ValueError(f"El campo {campo} debe ser un texto no vacio.")

    if not isinstance(datos["tags"], list) or not datos["tags"]:
        raise ValueError("Debe haber al menos un tag dentro de una lista.")

    for tag in datos["tags"]:
        if not isinstance(tag, str) or tag.strip() == "":
            raise ValueError("Cada tag debe ser un texto no vacio.")

    if datos["estado"] not in ("borrador", "publicado", "archivado"):
        raise ValueError("El estado no esta permitido.")

    autor = crear_autor_desde_dict(datos["autor"])

    return Post(
        datos["id"],
        datos["titulo"],
        datos["contenido"],
        autor,
        datos["tags"],
        datos["estado"]
    )
