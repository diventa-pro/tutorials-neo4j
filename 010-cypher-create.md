Nodi e archi
======

Creazione di nodi e archi
---------

### Nodo anonimo

Rappresentazione di un nodo anonimo:

    ()

Creazione di un nodo anonimo. 
Il nodo viene creato ma poichè non c'è nessun riferimento ad esso viene anche
rimosso

    CREATE()


### Riferimenti ai nodi e RETURN

Un riferimento ad un nodo.

    (<reference>)

Creare nodi con vari riferimenti

    CREATE(pippo)
    CREATE(pluto)
    CREATE(paperino)

Se si desidera restituire i nodi dopo averli creati...

    CREATE(pippo)
    CREATE(pluto)
    CREATE(paperino)
    RETURN pippo, pluto, paperino


### Nodo con label

Un nodo con label

    (:<label> :<label> :<label>)

Creazione di un nodo con label "città".

    CREATE(:Città)

    CREATE(:Regista :Attore)

Un riferimento chiamato "matrix" 
ad un nodo con label "Movie"

    CREATE(matrix:Movie)    
    RETURN matrix



### Proprietà

Un nodo "Movie" ha anche un titolo: "The Matrix"

    (matrix:Movie {title: "The Matrix"})

Il nodo ha titolo e anno di pubblicazione

    (matrix:Movie {title: "The Matrix", released: 1997})

Tornando alle città, qual'è il nome della città?
Il nome della città è una proprietà

    CREATE(milano:Città {nome: "Milano"})
    RETURN milano

Si possono definire più proprietà.

    CREATE(monza:Città {nome: "Monza", popolazione: 124000})
    RETURN monza


Relazioni
---------

Un arco (o "relazione" in Neo4j) direzionale

    -->
    <--

Una relazione tipizzata

    -[:ACTED_IN]->
    <-[:ACTED_IN]-

Una relazione tipizzata con un riferimento
ad essa (variabile)

    -[role:ACTED_IN]->
    <-[role:ACTED_IN]-

Una relazione tipizzata con
una proprietà di tipo lista

    -[role:ACTED_IN {roles: ["Neo"]}]->    
    <-[role:ACTED_IN {roles: ["Neo"]}]-

Creiamo un cittadino in relazione "residenza"
con una città

    CREATE(carlo:Cittadino {nome: "Carlo Rambaldi"})-[:RESIDENZA]->(biassono:Città {nome: "Biassono", popolazione: 12300})
    RETURN carlo, biassono

Creiamo un cittadino 
con il periodo di residenza

    CREATE(susanna:Cittadino {nome: "Susanna"})-[:RESIDENZA {dal:"2010-03-23" , al:"2020-02-27"}]->(muggiò:Città {nome: "Muggiò", popolazione: 9700})    
    RETURN susanna, muggiò

Creiamo due cittadini con una relazione sentimentale

    CREATE(gng:Cittadino {nome: "Gianna Giancredi"})<-[:COPPIA]-(mrm:Cittadino {nome: "Marco Maramaldi"})    
    RETURN gng, mrm







