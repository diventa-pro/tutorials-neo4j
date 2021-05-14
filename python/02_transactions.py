class CompanyExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def empty_database(self):
        print(f"Svuotando database.")
        with self.driver.session() as session:
            count_removed = session.write_transaction(self._empty_database)
            print(f"Svuotato database, {count_removed} nodi rimossi.")
            return count_removed

    def insert_company(self, company_name):
        print(f"Creando azienda {company_name}.")
        with self.driver.session() as session:
            id = session.write_transaction(self._create_company, company_name)
            print(f"Azienda {company_name} creata con id {id}")
            return id

    @staticmethod
    def _create_company(tx, company_name):
        result = tx.run("CREATE (c:Company) SET c.name = $name RETURN id(c)", name=company_name)
        return result.single()[0]

    @staticmethod
    def _empty_database(tx):
        result = tx.run("MATCH (n) DETACH DELETE n return count(n)")
        return result.single()[0]
