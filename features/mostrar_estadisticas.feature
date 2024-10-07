Feature: Visualización de estadísticas de partida

  Scenario: Consulta exitosa de estadísticas
    Given que existe una partida con ID guardado
    When solicito ver las estadísticas de la partida guardada
    Then el sistema muestra los puntajes actuales de cada jugador en la partida

  Scenario: Consulta fallida por partida inexistente
    Given que no existe una partida con ID "999999"
    When solicito ver las estadísticas de la partida con ID "999999"
    Then el sistema notifica que la partida no fue encontrada
