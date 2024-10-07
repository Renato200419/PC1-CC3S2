---
name: Análisis de Seguridad Automatizado
about: Implementación de un análisis de seguridad automatizado para detectar vulnerabilidades
  en el código.
title: ''
labels: ''
assignees: ''

---

**Como**: desarrollador  
**Quiero**: detectar vulnerabilidades en el código automáticamente  
**Para**: mantener la seguridad e integridad de la aplicación  

**Criterios de Aceptación**:
- Debe integrarse una herramienta de análisis de seguridad (por ejemplo, `pip-audit` o `OWASP Dependency-Check`) en el pipeline de CI/CD.
- El análisis debe ejecutarse automáticamente cada vez que se realice un nuevo commit.
- Se deben generar reportes detallados de las vulnerabilidades detectadas, indicando las acciones recomendadas.
