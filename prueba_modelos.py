from blog.modelos import Autor, Post, Blog, crear_post_desde_dict


autor = Autor(
    "Patrick Jane",
    "Consultor del CBI."
)

post = Post(
    1,
    "El misterio de la mansion",
    "Patrick encontro una pista importante.",
    autor,
    ["Investigacion", "Observacion"],
    "publicado"
)

blog = Blog([])
blog.agregar_post(post)


# Prueba del listado.
blog.listar_posts()


# Prueba de conversion a diccionario.
print(post.to_dict())


# Pruebas de busqueda y filtrado.
print(
    "Resultados de busqueda:",
    len(blog.buscar_por_titulo("MANSION"))
)

print(
    "Resultados por tag:",
    len(blog.filtrar_por_tag("observacion"))
)


# Prueba de reconstruccion de objetos.
datos_post = post.to_dict()
post_recuperado = crear_post_desde_dict(datos_post)

print("Tipo del post:", type(post_recuperado))
print("Tipo del autor:", type(post_recuperado.autor))
print("Autor recuperado:", post_recuperado.autor.nombre)