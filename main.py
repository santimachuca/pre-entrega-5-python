from blog.datos import cargar_posts, guardar_posts
from blog.modelos import Blog
from blog.menu import mostrar_menu, pedir_termino_busqueda, pedir_tag

def ejecutar():
    posts_recuperados = cargar_posts()

    blog = Blog(posts_recuperados)

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            blog.listar_posts()

        elif opcion == "2":
            termino = pedir_termino_busqueda()
            resultados = blog.buscar_por_titulo(termino)

            if resultados:
                Blog(resultados).listar_posts()
            else:
                print("No se encontraron posts con ese titulo.")

        elif opcion == "3":
            tag = pedir_tag()
            resultados = blog.filtrar_por_tag(tag)

            if resultados:
                Blog(resultados).listar_posts()
            else:
                print("No se encontraron posts con ese tag.")

        elif opcion == "4":
            blog.validar_posts()

        elif opcion == "5":
            if guardar_posts(blog.posts):
                print("Posts guardados en posts.json.")

        elif opcion == "7":
            # Pedimos los datos de la nueva publicacion.
            titulo = input("Titulo: ").strip()
            contenido = input("Contenido: ").strip()
            nombre = input("Nombre del autor: ").strip()
            bio = input("Biografia del autor: ").strip()
            estado = input(
                "Estado (borrador, publicado o archivado): "
            ).strip().lower()

            # Convertimos los tags separados por comas en una lista.
            texto_tags = input("Tags separados por comas: ")
            tags = []

            for tag in texto_tags.split(","):
                tag_limpio = tag.strip()

                if tag_limpio:
                    tags.append(tag_limpio)

            # El menu pide datos; Blog crea, valida y agrega el objeto.
            es_valido, mensaje = blog.crear_post(
                titulo, contenido, nombre, bio, tags, estado
            )
            if es_valido:
                print(mensaje)
            else:
                print("No se pudo crear el post:", mensaje)

        elif opcion == "6":
            print("Gracias por usar el sistema del blog.")
            break

        else:
            print("Opcion invalida. Intenta nuevamente.")


if __name__ == "__main__":
    ejecutar()
