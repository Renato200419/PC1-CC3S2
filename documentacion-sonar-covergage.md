# Generar reportes de cobertura y calidad de código.
## 1. Coverage
Coverage (o cobertura de código) es una métrica que mide qué porcentaje del código fuente ha sido ejecutado durante las pruebas. Ayuda a identificar qué partes del código no están probadas y, por lo tanto, podrían tener errores no detectados. Es comúnmente utilizado para asegurar que las pruebas cubren la mayor parte posible del código, aumentando la fiabilidad y calidad del software.

### Integración en CI/CD pipeline
```yml
- name: Run unit tests with coverage
  run: |
    docker-compose exec app coverage run -m pytest tests/    # Correr los tests con coverage
    docker-compose exec app coverage xml -o coverage.xml     # Generar el reporte de coverage
          
- name: List files in container
  run: |
    docker-compose exec app ls -al /  

- name: Copy coverage report to host    
  run: |
    docker cp $(docker-compose ps -q app):/app/coverage.xml .    # Copiar el reporte de coverage al host

- name: Upload coverage report
  uses: actions/upload-artifact@v3
  with:
    name: coverage-report
    path: coverage.xml
```
#### Explicación:
1. **`Run unit tests with coverage`**:
   - Ejecuta las pruebas unitarias con `pytest` y genera el reporte de cobertura (`coverage.xml`) dentro del contenedor `app`.

2. **`List files in container`**:
   - Lista los archivos y directorios en el contenedor para verificar que `coverage.xml` fue generado correctamente.

3. **`Copy coverage report to host`**:
   - Copia el archivo `coverage.xml` desde el contenedor `app` al host del runner de GitHub Actions para poder utilizarlo fuera del contenedor.

4. **`Upload coverage report`**:
   - Sube el archivo `coverage.xml` como un artefacto en GitHub Actions, permitiendo su visualización y descarga desde la interfaz de GitHub.

## 2. SonarCloud
SonarCloud es una herramienta de análisis de calidad de código basada en la nube. Evalúa la calidad, seguridad y mantenibilidad del código fuente mediante la detección de bugs, vulnerabilidades y problemas de estilo. Además, ofrece integraciones con herramientas de CI/CD para automatizar el análisis de calidad en cada commit o pull request, facilitando la detección temprana de problemas y asegurando que el código se mantenga en óptimas condiciones.

### En SonarCloud

[Descripción imagen](Imagenes-sonar/Foto1.png)

[Descripción imagen](Imagenes-sonar/Foto2.png)

[Descripción imagen](Imagenes-sonar/Foto3.png)

#### Integración en CI/CD pipeline
```yml
- name: Set up JDK 17  # Configurar Java 17 para la compatibilidad con SonarQube
  uses: actions/setup-java@v2
  with:
    distribution: 'adopt'
    java-version: '17'    

- name: SonarQube Scan
  # Ejecutar solo si es un Pull Request
  if: github.event_name == 'pull_request'   
  uses: sonarsource/sonarqube-scan-action@v2.1.0
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
  with:
    args: |
       -Dsonar.projectKey=Renato200419_PC1-CC3S2
       -Dsonar.organization=renato200419
       -Dsonar.sources=.
       -Dsonar.host.url=https://sonarcloud.io
       -Dsonar.login=${{ secrets.SONAR_TOKEN }}
       -Dsonar.python.coverage.reportPaths=coverage.xml
       -Dsonar.java.source=17
       -Dsonar.pullrequest.key=${{ github.event.pull_request.number }}
       -Dsonar.pullrequest.base=${{ github.event.pull_request.base.ref }}
       -Dsonar.pullrequest.branch=${{ github.head_ref }}
  
- name: SonarQube Scan - Main Branch
  # Ejecutar solo si es un push a la rama main
  if: github.ref == 'refs/heads/main'  
  uses: sonarsource/sonarqube-scan-action@v2.1.0
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
  with:
    args: |
       -Dsonar.projectKey=Renato200419_PC1-CC3S2
       -Dsonar.organization=renato200419
       -Dsonar.sources=.
       -Dsonar.host.url=https://sonarcloud.io
       -Dsonar.login=${{ secrets.SONAR_TOKEN }}
       -Dsonar.python.coverage.reportPaths=coverage.xml
       -Dsonar.java.source=17
```
#### Explicación

### Explicación Breve de Cada Paso

1. **`Set up JDK 17`**:
   - **Propósito**: Configura Java 17 en el entorno de GitHub Actions para garantizar la compatibilidad con SonarQube.
   - **Descripción**: Utiliza la acción `setup-java@v2` para instalar la versión 17 de Java (`adopt` es el distribuidor). Esto es necesario porque SonarQube requiere Java para ejecutar su análisis.

2. **`SonarQube Scan` (Pull Request)**:
   - **Propósito**: Realiza el análisis de SonarQube solo si la ejecución se activa por un Pull Request (`if: github.event_name == 'pull_request'`).
   - **Descripción**: Usa la acción `sonarsource/sonarqube-scan-action` para ejecutar el análisis en SonarCloud. Se pasan parámetros específicos como `sonar.projectKey`, `sonar.organization`, y las variables del Pull Request (`sonar.pullrequest.key`, `sonar.pullrequest.base`, y `sonar.pullrequest.branch`).

3. **`SonarQube Scan - Main Branch`**:
   - **Propósito**: Ejecuta el análisis de SonarQube en la rama `main` después de un push (`if: github.ref == 'refs/heads/main'`).
   - **Descripción**: Similar al paso anterior, pero sin las variables de Pull Request. Esto asegura que SonarCloud realice un análisis estándar en la rama `main`, midiendo cobertura y verificando calidad.
