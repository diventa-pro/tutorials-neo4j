Partiamo da un db vuoto
    
    MATCH(n)-[dr]->(m)
    DELETE(dr)

    MATCH(dn)
    DELETE(dn)

Ecco il database

    // film
    CREATE (matrix:Movie { title:"The Matrix",released:1997 })
    CREATE (cloudAtlas:Movie { title:"Cloud Atlas",released:2012 })
    CREATE (forrestGump:Movie { title:"Forrest Gump",released:1994 })
    CREATE (granTorino:Movie {title:"Gran Torino",released:2008})

    // persone
    CREATE (keanu:Person { name:"Keanu Reeves", born:1964 })
    CREATE (robert:Person { name:"Robert Zemeckis", born:1951 })
    CREATE (clint:Person { name:"Clint Eastwood", born:1930 })    
    CREATE (tom:Person { name:"Tom Hanks", born:1956 })
    CREATE (carrie:Person { name:"Carrie-Anne Moss", born:1967 })    

    // relazioni
    CREATE (tom)-[:ACTED_IN { roles: ["Forrest"]}]->(forrestGump)
    CREATE (tom)-[:ACTED_IN { roles: ['Zachry']}]->(cloudAtlas)
    CREATE (robert)-[:DIRECTED]->(forrestGump)
    CREATE (clint)-[:DIRECTED]->(granTorino)
    CREATE (clint)-[:ACTED_IN {roles:['Walt']}]->(granTorino)
    CREATE (keanu)-[:ACTED_IN { roles: ['Neo']}]->(matrix)    
    CREATE (carrie)-[:ACTED_IN { roles: ['Trinity']}]->(matrix)    

Questa

    MATCH (m:Movie { title: "The Matrix" })
    RETURN m

equivale a

    MATCH (m:Movie)
    WHERE m.title = "The Matrix"
    RETURN m

ma con la clausola `WHERE` è possibile esprimere molti più vincoli:

    MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
    WHERE p.name =~ "K.+" OR m.released > 2000 OR "Neo" IN r.roles 
    RETURN p,r,m

    MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
    WHERE p.name =~ "K.+" AND m.released <= 2000 AND "Neo" IN r.roles 
    RETURN p,r,m

Tutti gli attori che hanno partecipato a qualche film

    MATCH (p:Person)-[:ACTED_IN]->(m)
    RETURN p,m    

Ma non quelli che si sono diretti

    MATCH (p:Person)-[:ACTED_IN]->(m)
    WHERE NOT (p)-[:DIRECTED]->()
    RETURN p,m    