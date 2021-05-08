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
    CREATE (lara)-[:FIGLIO_DI]->(gianna)
    CREATE (lara)-[:FIGLIO_DI]->(gigi)
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

Visualizziamo

    match(n) return n

Trovare i geniori di una certa persona

    

  
