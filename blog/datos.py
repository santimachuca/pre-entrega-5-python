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