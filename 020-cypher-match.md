    // Troviamo le città
    MATCH(c:Città)
    RETURN c

    // Troviamo la città di
    // Milano
    MATCH(m:Città {nome: "Milano"})
    RETURN m

    // Troviamo la popolazione della città
    // in cui vive Carlo
    MATCH(p:Cittadino {nome: "Carlo"})-[:RESIDENZA]->(c:Città)
    RETURN p.nome, c.popolazione