# Documentación del Cliente de Consola
## Propósito
Este documento proporciona una guía detallada sobre cómo instalar, ejecutar y utilizar el cliente de consola para el juego de dados competitivo. El cliente permite a los jugadores unirse a partidas, lanzar dados y consultar estadísticas a través de la terminal.
## Instrucciones de Instalación y Ejecución
### Requisitos Previos
- **Python**: Debe estar instalado en tu sistema (versión 3.x recomendada).
- **Dependencias**: Asegúrate de tener las dependencias del proyecto especificadas en `requirements.txt`.
### Instalación
1. **Clonar el Repositorio**: Si aún no lo has hecho, clona el repositorio del proyecto:
   ```bash
   git clone https://github.com/usuario/juego-dados-competitivo.git
   ```
2. **Navegar al Directorio del Proyecto**:
   ```bash
   cd juego-dados-competitivo
   ```
3. **Instalar Dependencias**: Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
### Ejecución
Para iniciar el cliente de consola y comenzar a jugar:
1. **Ejecutar el Cliente**:
   ```bash
   python game_console.py
   ```
## Guía de Uso
### Unirse a una Partida
1. Al iniciar el cliente, se te pedirá ingresar tu nombre y el nombre de la partida a la que deseas unirte.
2. Introduce los datos solicitados y presiona Enter.
### Lanzar Dados
1. Dentro de una partida, puedes lanzar los dados utilizando el comando de lanzamiento cuando se te indique.
2. El cliente mostrará el resultado del lanzamiento y actualizará la puntuación.
### Ver Estadísticas
1. Para consultar las estadísticas de la partida actual, utiliza el comando correspondiente en el cliente.
2. El cliente te proporcionará información sobre la puntuación actual y otras métricas relevantes.
## Ejemplos de Uso
### Unirse a una Partida
```
> python main.py
Ingrese su nombre: Juan
Ingrese el nombre de la partida: Partida1
```
### Lanzar Dados
```
> lanzar dados
Resultado: 4, 5
```
### Ver Estadísticas
```
> ver estadísticas
Puntuación Actual: 9
```
## Solución de Problemas
- **No se puede conectar al servidor**: Verifica que los servicios de la API estén funcionando y que tu red esté correctamente configurada.
- **Errores de dependencia**: Asegúrate de haber instalado todas las dependencias mencionadas en `requirements.txt`.
