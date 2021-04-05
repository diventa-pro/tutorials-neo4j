# Gestire database diversi

Passare al database `system`, normalmente sempre esistente, e creare il database che si desidera.

    :use system; 
    CREATE DATABASE testdb; 

Dare il tempo a `Neo4j` di creare il database desiderato ed iniziare ad usarlo.

    :use testdb;

Creare alcuni nodi e relazioni:

    CREATE (gianni:Persona)-[:AMICO]->(anna:Persona)
    CREATE (anna)-[:AMICO]->(piero:Persona)



https://resources.oreilly.com/examples/0636920233145/raw/master/data/transport-nodes.csv
https://resources.oreilly.com/examples/0636920233145/raw/master/data/transport-relationships.csv