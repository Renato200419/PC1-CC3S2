Feature: Creación de partidas

  Scenario: Creación exitosa de una partida
    Given que los jugadores "Ana" y "Luis" están registrados
    When solicito crear una partida con los jugadores "Ana" y "Luis"
    Then el sistema crea la partida asignando un ID único
    And confirma que la partida ha sido creada con éxito

  Scenario: Creación fallida por jugador no registrado
    Given que el jugador "Ana" está registrado
    And que el jugador "María" no está registrado
    When solicito crear una partida con los jugadores "Ana" y "María"
    Then el sistema notifica que el jugador "María" no está registrado

  Scenario: Creación fallida por número insuficiente de jugadores
    Given que el jugador "Ana" está registrado
    When solicito crear una partida con el jugador "Ana"
    Then el sistema notifica que se requieren al menos 2 jugadores
