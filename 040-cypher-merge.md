Partiamo da un nuovo grafo.   
   
    // film
    CREATE (matrix:Movie { title:"The Matrix",released:1997 })
    CREATE (cloudAtlas:Movie { title:"Cloud Atlas",released:2012 })
    CREATE (forrestGump:Movie { title:"Forrest Gump",released:1994 })

    // persone
    CREATE (keanu:Person { name:"Keanu Reeves", born:1964 })
    CREATE (robert:Person { name:"Robert Zemeckis", born:1951 })

    // relazioni
    CREATE (tom:Person { name:"Tom Hanks", born:1956 })
    CREATE (tom)-[:ACTED_IN { roles: ["Forrest"]}]->(forrestGump)
    CREATE (tom)-[:ACTED_IN { roles: ['Zachry']}]->(cloudAtlas)
    CREATE (robert)-[:DIRECTED]->(forrestGump)

Ipotizziamo di volerci assicurare che un film esista, senza crearlo due volte.    

    MERGE (m:Movie { title:"Cloud Atlas" })
    ON CREATE SET m.released = 2012
    RETURN m    

Se anche eseguiamo questa 
operazione n volte non ci sono duplicati.

Oppure di creare una relazione.

    MATCH (m:Movie { title:"The Matrix" })
    MATCH (p:Person { name:"Keanu Reeves" })
    MERGE (p)-[r:ACTED_IN]->(m)
    ON CREATE SET r.roles =['Neo']
    RETURN p,r,m
