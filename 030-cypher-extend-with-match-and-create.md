Aggiungiamo vari cittadini a varie città

    MATCH(c:Città {nome:"Milano"})
    CREATE(p1:Cittadino {nome:"Sara"})
    CREATE(p1)-[:RESIDENZA {dal:"1990-02-23"}]->(c)
    CREATE(p2:Cittadino {nome:"Mario"})
    CREATE(p2)-[:RESIDENZA {dal:"1995-12-31"}]->(c)    
    CREATE(p3:Cittadino {nome:"Zeno"})
    CREATE(p3)-[:RESIDENZA {dal:"2017-08-13"}]->(c)        
    RETURN p1, p2, p3

__Attenzione__
quando si combinano
`MATCH` e `CREATE`.

Attenzione!
Cosa succede con questo costrutto?

    MATCH(c:Città)
    MATCH(p:Cittadino {nome:"Sara"})
    CREATE(p)-[:LAVORA_A]->(c)
    RETURN p

`CREATE` viene applicato a tutte le occorrenze trovate da `MATCH`.

__Attenzione__
a quando si usa `CREATE` ripetutamente.

Attenzione!
Cosa succede con questo costrutto?

    MATCH(c:Città {nome:"Milano"})
    MATCH(p:Cittadino {nome:"Sara"})
    CREATE(p)-[:LAVORA_A]->(c)
    CREATE(p)-[:LAVORA_A]->(c)
    CREATE(p)-[:LAVORA_A]->(c)
    CREATE(p)-[:LAVORA_A]->(c)
    CREATE(p)-[:LAVORA_A]->(c)
    RETURN p

Vengono creati più archi di tipo `LAVORA_A`! Non esiste un'identificativo dell'arco!

Cancelliamo tutti gli elementi del grafo. Prima di tutto le relazioni.

    MATCH(n)-[r]->(m)
    DELETE(r)

Poi i nodi

    MATCH(n)
    DELETE(n)