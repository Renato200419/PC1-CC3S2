Feature: Lanzamiento de dados

  Scenario: Lanzamiento exitoso de dados en una partida
    Given que ingreso un ID de partida válido
    When solicito lanzar los dados
    Then el sistema genera números aleatorios entre 1 y 6 para cada jugador
    And actualiza y muestra los puntajes acumulados de cada jugador

  Scenario: Lanzamiento fallido por partida inexistente
    Given que ingreso un ID de partida inválido
    When solicito lanzar los dados
    Then el sistema notifica que la partida no existe
    And no realiza el lanzamiento

  Scenario: Partida finalizada por alcanzar puntaje máximo
    Given uno o más jugadores han alcanzado el puntaje máximo
    When se realiza un lanzamiento
    Then el sistema declara al ganador y finaliza la partida
