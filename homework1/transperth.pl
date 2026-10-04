% Assumptions and Conventions
/*
connected(X, Y, L) means there is a one-way edge along train line L from X to Y
-> X and Y cannot be swapped with the same L

the connected(X, Y, L) facts of this knowledge base are formed in a linked list fashion
-> there is not transitivity so you need to traverse edges manually i.e connected(X, Y, L) and connected(Y, Z, L) but not connected(X, Z, L)

there is no edge from X to X on any L i.e no loops
*/


connected(yanchep, eglinton, yanchepLineReverse).
connected(eglinton, alkimos, yanchepLineReverse).
connected(alkimos, butler, yanchepLineReverse).
connected(butler, clarkson, yanchepLineReverse).
connected(clarkson, currambine, yanchepLineReverse).
connected(currambine, joondalup, yanchepLineReverse).
connected(joondalup, edgewater, yanchepLineReverse).
connected(edgewater, whitfords, yanchepLineReverse).

connected(stirling, warwick, yanchepLineForward).
connected(warwick, greenwood, yanchepLineForward).
connected(greenwood, whitfords, yanchepLineForward).
connected(whitfords, edgewater, yanchepLineForward).
connected(edgewater, joondalup, yanchepLineForward).

closed(alkimos).
closed(edgewater).
closed(greenwood).

station_on_line(S,L) :- connected(S, _, L) ; connected(_, S, L).

before_on_line(S, T, L) :- connected(S, T, L).
before_on_line(S, T, L) :- connected(_, T, L), before_on_line(S, _, L).

terminal(S, L) :- \+ connected(_, S, L) ; \+ connected(S, _, L).

route_on_line(S, T, L, [S, T]) :- \+ closed(S), \+ closed(T), connected(S, T, L).
route_on_line(S, T, L, [S, X | Tail]) :- \+ closed(S), connected(S, X, L), \+ X == T, route_on_line(X, T, L, [X | Tail]).