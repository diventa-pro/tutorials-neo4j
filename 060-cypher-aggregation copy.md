Come raggruppare?

contare le persone presenti

    MATCH (:Person)
    RETURN count(*) AS people

contare gli attori

    MATCH (actor:Person)-[:ACTED_IN]->(:Movie)
    RETURN count( DISTINCT actor )

contare i film in cui ogni attore ha partecipato

    MATCH (actor:Person)-[:ACTED_IN]->(movie:Movie)
    RETURN actor, count( DISTINCT movie )   

ordinare dal più impegnato al meno

    MATCH (actor:Person)-[:ACTED_IN]->(movie:Movie)
    RETURN actor, count( DISTINCT movie ) as movieCount  
    ORDER BY movieCount DESC, actor.name ASC

raccogliere dati

    MATCH (m:Movie)<-[:ACTED_IN]-(a:Person)
    RETURN m.title AS movie, collect(a.name) AS cast, count(*) AS actors
