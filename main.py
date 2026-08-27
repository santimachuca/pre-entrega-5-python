from blog.datos import posts
from blog.menu import mostrar_menu, pedir_termino_busqueda, pedir_tag
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_posts


def ejecutar():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            listar_posts(posts)

        elif opcion == "2":
            termino = pedir_termino_busqueda()
            resultados = buscar_por_titulo(posts, termino)

            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron posts con ese titulo.")

        elif opcion == "3":
            tag = pedir_tag()
            resultados = filtrar_por_tag(posts, tag)

            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron posts con ese tag.")

        elif opcion == "4":
            validar_posts(posts)

        elif opcion == "5":
            print("Gracias por usar el sistema del blog.")
            break

        else:
            print("Opcion invalida. Intenta nuevamente.")


if __name__ == "__main__":
    ejecutar()