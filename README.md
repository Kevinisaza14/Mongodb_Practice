# Proyecto: Práctica Python + MongoDB

Pequeña API REST construida con Python y MongoDB para gestionar una colección de "notas". Proyecto pensado como ejercicio práctico y como pieza para incluir en tu portafolio profesional: código claro, estructura modular y ejemplos de despliegue local.

Por qué incluirlo en tu portafolio  
- Demuestra habilidades backend con Python y Flask.  
- Muestra integración con bases de datos NoSQL (MongoDB) y gestión de variables de entorno.  
- Permite explicar diseño de rutas REST, operaciones CRUD y buenas prácticas (entorno virtual, requirements, scripts de inicialización).  
- Fácil de ejecutar y probar (ideal para demostraciones en entrevistas).

Tecnologías / lenguajes usados
- Python 3.8+ (lenguaje principal).  
- Flask — microframework web para las rutas REST.  
- PyMongo — driver para conectar con MongoDB.  
- python-dotenv — gestión de variables de entorno (.env).  
- MongoDB (local o Atlas) — base de datos NoSQL.  
- JSON — formato para entrada/salida de la API.  
- Herramientas de prueba: curl o Postman.

Estructura del proyecto (explicación por carpeta/archivo)
```
Mongodb_Practice/
├─ app/
│  ├─ __init__.py      # convierte app en paquete; aquí puedes cargar config/globales
│  ├─ main.py          # Flask app + rutas CRUD; punto central de la lógica HTTP
│  ├─ db.py            # conexión a MongoDB (lee MONGO_URI y exporta db o la colección)
│  └─ models.py        # esquemas y validaciones (opcional; p. ej. con pydantic o marshmallow)
├─ scripts/
│  └─ init_db.py       # script para crear datos de ejemplo (útil para demos y pruebas)
├─ requirements.txt    # dependencias: flask, pymongo, python-dotenv
├─ .env                # variables de entorno (MONGO_URI, FLASK_ENV) — no subir a git
├─ run.py              # arranca la aplicación (wrapper que importa app.main)
└─ README.md           # documentación del proyecto
```

Descripciones clave
- app/db.py: establece la conexión con MongoDB. Debe leer MONGO_URI desde .env y exportar la colección o cliente para que main.py la use. Manejar excepciones de conexión para feedback útil.  
- app/main.py: define la app Flask y las rutas REST:
  - GET /notes — listar notas
  - GET /notes/<id> — obtener nota por id
  - POST /notes — crear nota (JSON: { "title": "...", "body": "..." })
  - PUT /notes/<id> — actualizar nota
  - DELETE /notes/<id> — eliminar nota  
  Incluir validación básica del payload y manejo de errores (400/404/500).
- scripts/init_db.py: inserta datos de ejemplo para facilitar demostraciones locales.
- run.py: script simple para arrancar la app, útil como entrypoint en despliegues simples.

Requisitos
- Python 3.8 o superior.  
- MongoDB local o cuenta en Mongo Atlas.  
- Paquetes: flask, pymongo, python-dotenv (ver requirements.txt).

Archivo .env (ejemplo)
```
MONGO_URI=mongodb://localhost:27017/mongo_practice
FLASK_ENV=development
```
Si usas Mongo Atlas, reemplaza MONGO_URI por la cadena proporcionada.

Instalación y ejecución (Windows / Linux / macOS)
1. Crear y activar entorno virtual:
   - Windows:
     - python -m venv venv
     - venv\Scripts\activate
   - Linux/macOS:
     - python -m venv venv
     - source venv/bin/activate
2. Instalar dependencias:
   - pip install -r requirements.txt
3. Configurar `.env` con MONGO_URI.
4. (Opcional) Inicializar datos de ejemplo:
   - python scripts/init_db.py
5. Ejecutar la aplicación:
   - python run.py
   - Por defecto escuchará en http://127.0.0.1:5000

Ejemplos de uso (curl)
- Crear:
  curl -X POST -H "Content-Type: application/json" -d '{"title":"Hola","body":"Clase 1"}' http://127.0.0.1:5000/notes
- Listar:
  curl http://127.0.0.1:5000/notes
- Obtener:
  curl http://127.0.0.1:5000/notes/<id>
- Actualizar:
  curl -X PUT -H "Content-Type: application/json" -d '{"title":"Nuevo","body":"Contenido"}' http://127.0.0.1:5000/notes/<id>
- Borrar:
  curl -X DELETE http://127.0.0.1:5000/notes/<id>

Buenas prácticas recomendadas para el README de tu portafolio
- Incluye una breve introducción del proyecto y objetivos (qué resuelve).  
- Añade instrucciones claras para ejecutar localmente y para pruebas (como las anteriores).  
- Inserta ejemplos de respuesta JSON y errores posibles.  
- Agrega capturas de pantalla o gif demostrativos (si es posible) y un enlace al repositorio.  
- Señala qué partes del proyecto muestran mejor tus habilidades (p. ej. manejo de DB, validaciones, estructura modular).  
- Indica mejoras futuras o retos resueltos (paginación, autenticación, validación avanzada, pruebas unitarias).

Contribuciones y licencia
- Este proyecto está pensado como demo/portafolio. Para colaboración, crea un fork y un pull request con una descripción clara del cambio. Añade tests cuando agregues funcionalidad crítica.

Contacto
¿Te interesa mi trabajo?  
Puedes contactarme a través de [mi perfil de GitHub](https://github.com/Kevinisaza14) o a través de [Mi linkedin](https://www.linkedin.com/in/kevin-isaza-35a202275) para colaboraciones, sugerencias o propuestas laborales.