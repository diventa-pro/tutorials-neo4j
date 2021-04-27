Cyhper 
======

Nodi
-----

Un nodo anonimo.

    ()

Un riferimento chiamato "matrix" ad un nodo.

    (matrix)

Un nodo con label "Movie"

    (:Movie)

Un riferimento chiamato "matrix" 
ad un nodo con label "Movie"

    (matrix:Movie)

Il nodo ha anche un titolo: "The Matrix"

    (matrix:Movie {title: "The Matrix"})

Il nodo ha titolo e anno di pubblicazione

    (matrix:Movie {title: "The Matrix", released: 1997})

Relazioni
---------

Una relazione non direzionale

    --

Una relazione direzionale

    -->

Una relazione tipizzata

    -[:ACTED_IN]->

Una relazione tipizzata con un riferimento
ad essa (variabile)

    -[role:ACTED_IN]->

Una relazione tipizzata con
una proprietà di tipo lista

    -[role:ACTED_IN {roles: ["Neo"]}]->

Creazione
---------

Creazione di un nodo anonimo.
Poco utile.

    CREATE()

Creazione di un nodo "città".
Ma qual'è il nome della città?

    CREATE(:Città)

Il nome della città è una proprietà

    CREATE(:Città {nome: "Milano"})

Ci possono essere tante proprietà.

    CREATE(:Città {nome: "Monza", popolazione: 124000})

Possiamo assegnare la città creata ad una variabile

    CREATE(desio:Città {nome: "Desio", popolazione: 22000})
    RETURN desio

Creiamo un cittadino in relazione
con una città

    CREATE(:Cittadino {nome: "Carlo"})-[:RESIDENZA]->(:Città {nome: "Biassono", popolazione: 12300})

Creiamo un cittadino 
con il periodo di residenza

    CREATE(:Cittadino {nome: "Susanna"})-[:RESIDENZA {dal:"2010-03-23" , al:"2020-02-27"}]->(:Città {nome: "Muggiò", popolazione: 9700})    