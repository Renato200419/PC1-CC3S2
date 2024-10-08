from peewee import PostgresqlDatabase

# Configuración de la conexión a la base de datos PostgreSQL
db = PostgresqlDatabase(
    'dadosdb',  # Nombre de la base de datos
    user='admin',  # Usuario de la base de datos
    password='secret',  # Contraseña de la base de datos
    host='db',  # Nombre del host (coincide con el servicio en docker-compose.yml)
    port=5432  # Puerto de la base de datos
)
