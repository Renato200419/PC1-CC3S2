Feature: Registro de jugadores

  Scenario: Registro exitoso de un nuevo jugador
    Given que no existe un jugador con nombre "Juan"
    When solicito registrar el jugador "Juan"
    Then el sistema confirma que el jugador ha sido registrado con éxito

  Scenario: Registro fallido por jugador ya registrado
    Given que existe un jugador con nombre "Pedro"
    When solicito registrar el jugador "Pedro"
    Then el sistema notifica que el jugador ya está registrado
