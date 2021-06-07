from neo4j import GraphDatabase
import traceback

class BasicUsage:


    def demo_just_connection(self, neo4j_uri, neo4j_username, neo4j_password):
        print(f"Collegandosi al database {neo4j_uri}.")
        driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))

        print(f"Collegato al database {neo4j_uri}.")

        print(f"Scollegandosi dal database {neo4j_uri}.")
        driver.close()
        print(f"Scollegato dal database {neo4j_uri}.")


    def demo_create_nodes(self, neo4j_uri, neo4j_username, neo4j_password):

        print(f"Collegandosi al database {neo4j_uri}.")
        driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))
        print(f"Collegato al database {neo4j_uri}.")

        session = driver.session()
        session.run("create(:Citta{nome:\"Milano\", popolazione:1.2})")
        session.run("create(:Citta{nome:\"Roma\", popolazione:3.0})")
        session.run("create(:Citta{nome:\"Torino\", popolazione:0.9})")
        session.run("create(:Citta{nome:\"Napoli\", popolazione:2.1})")
        session.close()

        print(f"Scollegandosi dal database {neo4j_uri}.")
        driver.close()
        print(f"Scollegato dal database {neo4j_uri}.")


    def demo_read_query_result(self, neo4j_uri, neo4j_username, neo4j_password):

        driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))

        session = driver.session()
        result = session.run("match (c:Citta) return c, c.nome")
        print(result)

        iterable_result = iter(result)
        i = 0
        while True:
            try:
                item = next(iterable_result)
                print(f"\nitem {i} = {item}")

                # si può accedere ai campi del record per posizione...
                print(f"{item[0]}")
                print(f"{item[1]}")

                # ...o per chiave
                print(f"{item['c']}")
                print(f"{item['c.nome']}")
                i = i + 1
            except StopIteration:
                break
            except:
                traceback.print_exc()
                break
        session.close()

        print(f"Scollegandosi dal database {neo4j_uri}.")
        driver.close()
        print(f"Scollegato dal database {neo4j_uri}.")


    def demo_with_arguments(self, neo4j_uri, neo4j_username, neo4j_password, citta_da_cercare):

        driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))

        session = driver.session()
        result = session.run("match (c:Citta {nome:$nome}) return c.nome as nome, c.popolazione as popolazione", nome=citta_da_cercare)
        print(result)

        iterable_result = iter(result)
        i = 0
        while True:
            try:
                item = next(iterable_result)
                print(f"\nitem {i} = {item['nome']} {item['popolazione']}")
                i = i + 1
            except StopIteration:
                break
            except:
                traceback.print_exc()
                break
        if 0 == i:
            print(f"Nessun risultato per {citta_da_cercare}.")
        session.close()

        print(f"Scollegandosi dal database {neo4j_uri}.")
        driver.close()
        print(f"Scollegato dal database {neo4j_uri}.")


if __name__ == "__main__":

    basic = BasicUsage()
    # basic.demo_just_connection("bolt://localhost:7687", "", "")
    # basic.demo_create_nodes("bolt://localhost:7687", "", "")
    basic.demo_read_query_result("bolt://localhost:7687", "", "")
    # basic.demo_with_arguments("bolt://localhost:7687", "", "", "Napoli")
    # basic.demo_with_arguments("bolt://localhost:7687", "", "", "Palermo")
