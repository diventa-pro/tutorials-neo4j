Esercizi
===============

Parentela
--------------

Creare un grafo di persone, usando questa struttura del nodo:


    Persona {
      nome
      annoDiNascita
    }

Con queste relazioni:

    Persona --FIGLIO_DI--> Persona

Creare questi casi:

    A1 e B1 hanno quattro figli: A2, B2, C2 e D2.
    C1 e D1 hanno due figli: E2, F2.
    A1 e D1 hanno due figli: G2, H2.
    A2 e E2 hanno due figli: A3, B3.
    B2 e F2 hanno due figli: C3, D3.
    e così via...

Trovare questi casi:

    Trovare i genitori di una certa persona.
    Trovare i nonni di una certa persona.
    Trovare i fratelli di una certa persona.
    Trovare gli zii di una certa persona.
    Trovare i cugini di una certa persona.
    Trovare i nipoti di una persona.
    Trovare i figli di una certa coppia.

Database

Cancelliamo tutti i nod

    match (n) detach delete n   

Creiamo il DB

    CREATE (gigi:Persona {nome:"Gigi"})
    CREATE (gianna:Persona {nome:"Gianna"})
    CREATE (ludo:Persona {nome:"Ludovico"})
    CREATE (lara:Persona {nome:"Lara"})
    CREATE (ludo)-[:FIGLIO_DI]->(gianna)
    CREATE (ludo)-[:FIGLIO_DI]->(gigi)
    CREATE (carlo:Persona {nome:"Carlo"})
    CREATE (chiara:Persona {nome:"Chiara"})
    CREATE (andrea:Persona {nome:"Andrea"})
    CREATE (anna:Persona {nome:"Anna"})
    CREATE (andrea)-[:FIGLIO_DI]->(carlo)
    CREATE (andrea)-[:FIGLIO_DI]->(chiara)
    CREATE (anna)-[:FIGLIO_DI]->(carlo)
    CREATE (anna)-[:FIGLIO_DI]->(chiara)
    CREATE (rosa:Persona {nome:"Rosalinda"})
    CREATE (roberta:Persona {nome:"Roberta"})
    CREATE (rosa)-[:FIGLIO_DI]->(anna)
    CREATE (rosa)-[:FIGLIO_DI]->(ludo)
    CREATE (roberta)-[:FIGLIO_DI]->(anna)
    CREATE (roberta)-[:FIGLIO_DI]->(ludo)
    CREATE (lara)-[:FIGLIO_DI]->(anna)
    CREATE (lara)-[:FIGLIO_DI]->(ludo)    

Visualizziamo

    match(n) return n

Trovare i geniori di Rosalinda

    match ({nome:"Rosalinda"})-->(g) return g

Trovare i fratelli di Rosalinda

    match ({nome:"Rosalinda"})-->(g)<--(f) return f

Trovare i nonni di Roberta

    match ({nome:"Roberta"})-[*2]->(n) return n

Trovare quanti fratelli ha ogni singola persona che ha fratelli

    match (p)-->(g1)
    match (p)-->(g2)
    match (f)-->(g1)
    match (f)-->(g2)
    where not(g1=g2) and not(p=f) and (g1.nome<g2.nome)
    return p.nome, count(f.nome)

Trovare quanti fratelli ha ogni singola persona che ha fratelli

    match (p)
    optional match (p)-->(g1)
    optional match (p)-->(g2)
    optional match (f)-->(g1)
    optional match (f)-->(g2)
    with p, g1, g2, f
    where ((g1 is null and g2 is null) or (g1<>g2 and g1.nome > g2.nome)) and (f is null or p<>f)
    return p.nome, count(f)
