# API de Videos - Andres Esteban Vasquez Peña - Lenguaje de Programacion 3

Esta es una API RESTful para gestión de videos, desarrollada con Flask, Flask-RESTful y SQLAlchemy.

## Descripción

El proyecto implementa una API simple para gestionar información sobre videos, permitiendo:

- Crear nuevos videos
- Consultar videos existentes
- Actualizar información de videos
- Eliminar videos

Cada video tiene los siguientes atributos:
- ID: Identificador único del video
- Nombre: Título del video
- Vistas: Número de reproducciones
- Likes: Número de "me gusta"

## Estructura del Proyecto

```
lp3-taller1
├── app.py                  # Archivo principal para ejecutar la aplicación
├── config.py               # Configuración de la aplicación
├── models/
│   ├── __init__.py         # Inicializa el módulo models
│   └── video.py            # Modelo de datos para Video
├── resources/
│   ├── __init__.py         # Inicializa el módulo resources
│   └── video.py            # Recursos y rutas para Video
├── database.db             # Base de datos SQLite (generada automáticamente)
├── requirements.txt        # Dependencias del proyecto
└── estudiante.md           # Documentación del estudiante
```

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
   ```
   git clone https://github.com/UR-CC/lp3-taller1.git
   cd lp3-taller1
   ```

2. Crear un entorno virtual:
   ```
   python -m venv venv
   ```

3. Activar el entorno virtual:
     ```
     source venv/bin/activate
     ```

4. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

1. Iniciar el servidor de desarrollo:
   ```
   python app.py
   ```

2. El servidor estará disponible en `http://localhost:5000`

## Uso de la API

La API permite operaciones CRUD en videos. Usa curl para probar en consola.

### Obtener un video (GET)

**En consola:**
```
curl http://127.0.0.1:5000/api/videos/1
```

**En navegador:** Navega a `http://127.0.0.1:5000/api/videos/1` (funciona para GET).

Respuesta de ejemplo:
```json
{
  "id": 1,
  "name": "Tutorial de Python",
  "views": 1500,
  "likes": 120
}
```

### Crear un nuevo video (PUT)

**En consola:**
```
curl -X PUT http://127.0.0.1:5000/api/videos/1 \
-H "Content-Type: application/json" \
-d '{"name":"Tutorial de Flask","views":0,"likes":0}'
```

Respuesta de ejemplo:
```json
{
  "id": 1,
  "name": "Tutorial de Flask",
  "views": 0,
  "likes": 0
}
```

### Actualizar un video (PATCH)

**En consola:**
```
curl -X PATCH http://127.0.0.1:5000/api/videos/1 \
-H "Content-Type: application/json" \
-d '{"views":2500,"likes":200}'
```

Respuesta de ejemplo:
```json
{
  "id": 1,
  "name": "Tutorial de Flask",
  "views": 2500,
  "likes": 200
}
```

### Eliminar un video (DELETE)

**En consola:**
```
curl -X DELETE http://127.0.0.1:5000/api/videos/1
```


Respuesta de ejemplo: 204 No Content (vacío).

## Desarrollo del Taller

1. Ajustar este `README.md` con los datos del Estudiante

2. Realizar un `commit` por cada ajuste realizando, deben buscar los comentarios `# TODO:`

3. Completar el archivo `app.py`

4. Completar el archivo `resources/video.py`

5. Elaborar un documento con las pruebas realizar para cada método del API REST.

6. Implementar una (1) de las sugerencias que se presentan a continuación.

### Sugerencias de Mejora

1. **Autenticación y autorización**:
   - Implementar JWT para autenticar usuarios
   - Definir roles y permisos

2. **Documentación**:
   - Integrar Swagger/OpenAPI para documentar la API
   - Añadir ejemplos de uso

3. **Validación de datos**:
   - Mejorar la validación de entrada con marshmallow o similar
   - Manejar errores de forma más específica

4. **Funcionalidades adicionales**:
   - Añadir búsqueda y filtrado
   - Implementar paginación
   - Añadir endpoints para obtener todos los videos
   - Implementar sistema de categorías/etiquetas

5. **Migración de Base de datos**:
   - Implementar Flask-Migrate para gestionar cambios en el esquema

6. **Pruebas**:
   - Añadir pruebas unitarias
   - Implementar pruebas de integración
   - Configurar CI/CD

7. **Registro y monitoreo**:
   - Implementar logging
   - Añadir métricas y monitoreo

8. **Despliegue**:
   - Dockerizar la aplicación
   - Configurar para entornos de producción

## Implementación de Sugerencia 2: Documentación

Se implementó la integración de Swagger/OpenAPI para documentar la API y añadir ejemplos de uso. Esto permite una interfaz interactiva para probar endpoints.

### Cambios Realizados
- Cambie Flask-RESTful por Flask-RESTX en `app.py` y `resources/video.py`.
- Agregue un namespace en `resources/video.py` para agrupar endpoints.
- Documente cada endpoint con `@api.doc`, incluyendo parámetros, respuestas y modelos de datos.

### Ejemplos de Uso
- Ve a `http://127.0.0.1:5000` para ver Swagger UI.
- En PATCH /api/videos/{id}: Agrega JSON como `{"name": "Nuevo Video", "views": 100, "likes": 50}` y haz "Try it out" para actualizar.