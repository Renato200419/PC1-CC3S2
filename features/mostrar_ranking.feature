Feature: Visualización de ranking de jugadores

  Scenario: Consulta exitosa del ranking
    Given que hay jugadores registrados con partidas jugadas
    When solicito ver el ranking
    Then el sistema muestra una lista ordenada de jugadores por número de victorias

  Scenario: Consulta sin datos disponibles
    Given que no hay jugadores con partidas jugadas
    When solicito ver el ranking
    Then el sistema notifica que no hay jugadores registrados
