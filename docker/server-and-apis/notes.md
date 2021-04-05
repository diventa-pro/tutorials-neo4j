docker run -it neo4j:4.2.4 /bin/bash

Drop jar in $NEO4J_HOME/plugins

/var/lib/neo4j/

$NEO4J_HOME/conf/neoj4.conf
* dbms.security.procedures.unrestricted
* dbms.security.procedures.allowlist
https://neo4j.com/docs/operations-manual/current/security/securing-extensions/
dbms.security.procedures.unrestricted=my.extensions.example,my.procedures.*

# Example allow listing
dbms.security.procedures.allowlist=apoc.coll.*,apoc.load.*


https://github.com/neo4j-contrib/neo4j-apoc-procedures

4.2.2 (4.2.x) neo4j
4.2.0.2 (apoc)

https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/4.2.0.2/apoc-4.2.0.2-all.jar


docker run \
    -p 7474:7474 -p 7687:7687 \
    -v $PWD/data:/data -v $PWD/plugins:/plugins \
    --name neo4j-apoc \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4JLABS_PLUGINS=\[\"apoc\",""graph-data-science"\] \
    neo4j:4.0