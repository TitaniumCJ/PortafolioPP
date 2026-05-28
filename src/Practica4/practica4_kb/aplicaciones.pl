% Torres de Hanoi
hanoi(1, Origen, Destino, _) :-
    write('Mover disco desde '),
    write(Origen),
    write(' hacia '),
    write(Destino),
    nl.
hanoi(N, Origen, Destino, Auxiliar) :-
    N > 1,
    M is N - 1,
    hanoi(M, Origen, Auxiliar, Destino),
    hanoi(1, Origen, Destino, _),
    hanoi(M, Auxiliar, Destino, Origen).

% El mono y el platano
paso(estado(en_suelo, P1, P1, no), empujar(P1, P2), estado(en_suelo, P2, P2, no)).
paso(estado(en_suelo, P1, Box, no), caminar(P1, P2), estado(en_suelo, P2, Box, no)).
paso(estado(en_suelo, P, P, no), subir, estado(en_caja, P, P, no)).
paso(estado(en_caja, centro, centro, no), tomar, estado(en_caja, centro, centro, si)).

solucion(estado(_, _, _, si), []).
solucion(EstadoActual, [Movimiento | Resto]) :-
    paso(EstadoActual, Movimiento, EstadoSiguiente),
    solucion(EstadoSiguiente, Resto).