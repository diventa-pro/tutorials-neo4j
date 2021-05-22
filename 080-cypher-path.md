Path
====

Crea un db con 02_smarter_operations.py

Restituire un percorso tra Genova e Roma

    MATCH path=(origin :Citta {nome:"Genova"})-[:COLLEGAMENTO*]-(destination :Citta {nome:"Roma"})
    return path

Il tempo di esecuzione è amplissimo. 
Limitiamo il risultato.

    match path=(origin :Citta {nome:"Genova"})-[:COLLEGAMENTO*]-(destination :Citta {nome:"Roma"})
    return path
    limit 10

Non ci sono info sul costo del percorso, aggiungiamole.

    MATCH percorso=(origin :Citta {nome:"Genova"})-[:COLLEGAMENTO*]-(destination :Citta {nome:"Roma"}) 
    return 
    percorso,
    reduce(costo=0, tratta in relationships(percorso) | costo + tratta.costo) as costototale
    limit 10

Ordiniamo in modo da avere i più economici in cima

    MATCH percorso=(origin :Citta {nome:"Genova"})-[:COLLEGAMENTO*]-(destination :Citta {nome:"Roma"}) 
    return 
    percorso,
    reduce(costo=0, tratta in relationships(percorso) | costo + tratta.costo) as costototale
    order by costototale
    limit 10

Aggiungiamo altri campi che descrivano il percorso:

    MATCH percorso=(origin :Citta {nome:"Genova"})-[:COLLEGAMENTO*]-(destination :Citta {nome:"Roma"}) 
    return 
    reduce(costo=0, tratta in relationships(percorso) | costo + tratta.costo) as costototale,
    reduce(descrizione="", tratta in relationships(percorso) | descrizione + "/" + tratta.nome + " " + tratta.mezzo ) as indicazioni,
    reduce(descrizione="", citta in nodes(percorso) | descrizione + "/" + citta.nome ) as citta
    order by costototale
    limit 10

Aggiungiamo anche il tempo di percorrenza:

    MATCH percorso=(origin :Citta {nome:"Genova"})-[:COLLEGAMENTO*]-(destination :Citta {nome:"Roma"}) 
    return 
    reduce(costo=0, tratta in relationships(percorso) | costo + tratta.costo) as costototale,
    reduce(tempo=0, tratta in relationships(percorso) | tempo + tratta.tempo) as tempototale,
    reduce(descrizione="", tratta in relationships(percorso) | descrizione + "/" + tratta.nome + " " + tratta.mezzo ) as indicazioni,
    reduce(descrizione="", citta in nodes(percorso) | descrizione + "/" + citta.nome ) as citta
    order by tempototale
    limit 10

