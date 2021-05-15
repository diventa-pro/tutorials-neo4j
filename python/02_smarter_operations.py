from neo4j import GraphDatabase
import traceback

class SmarterOperations:

    def __init__(self, neo4j_uri, neo4j_username, neo4j_password):
        print(f"Collegandosi al database {neo4j_uri}.")
        self.driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))
        print(f"Collegato al database {neo4j_uri}.")

    def close(self):
        if self.driver:
            self.driver.close()
            print(f"Scollegato dal database {self.driver}.")

    def city_create(self, city_name, city_population):
        with self.driver.session() as session:
            result = session.run("create(c:Citta{nome:$name, popolazione:$population}) return id(c)",
                        name=city_name,
                        population=city_population)
            return result.single()[0]

    def create_link(self, origin_city_id, destination_city_id, cost_in_eur, time_in_hours, means_of_transport):
        with self.driver.session() as session:
            session.run("match (origine:Citta) "
                        "match (destinazione:Citta) "
                        "where "
                        "id(origine)=$id_origine and id(destinazione)=$id_destinazione "
                        "with origine,destinazione "
                        "create (origine)-[:COLLEGAMENTO {costo:$costo, tempo:$tempo, mezzo:$mezzo}]->(destinazione)",
                        id_origine=origin_city_id,
                        id_destinazione=destination_city_id,
                        costo=cost_in_eur,
                        tempo=time_in_hours,
                        mezzo=means_of_transport)

    def empty_database(self):
        with self.driver.session() as session:
            return session.run("match (n) detach delete n return count(n)").single()[0]

    def cheapest_path(self):
        # MATCH path=(origin :Citta {nome:"Genova"})-[:COLLEGAMENTO*]->(destination :Citta {nome:"Roma"})
        # return path
        return None


if __name__ == "__main__":

    demo = SmarterOperations("bolt://localhost:7687", "", "")

    print(f"Cancellati {demo.empty_database()} nodi.")
    id_milano = demo.city_create("Milano", 1.7)
    id_torino = demo.city_create("Torino", 0.9)
    id_genova = demo.city_create("Genova", 0.8)
    id_napoli = demo.city_create("Napoli", 2.1)
    id_roma = demo.city_create("Roma", 3.2)
    id_bologna = demo.city_create("Bologna", 0.5)
    id_firenze = demo.city_create("Firenze", 0.7)
    id_ancona = demo.city_create("Ancona", 0.7)
    id_bari = demo.city_create("Bari", 0.6)

    demo.create_link(id_genova, id_torino, 10.0, 1.2, "auto")
    demo.create_link(id_torino, id_milano, 15.0, 0.8, "treno")
    demo.create_link(id_torino, id_milano, 20.0, 1.5, "auto")
    demo.create_link(id_milano, id_bologna, 20.0, 1.5, "treno")
    demo.create_link(id_bologna, id_firenze, 20.0, 1.5, "treno")
    demo.create_link(id_firenze, id_roma, 20.0, 1.5, "treno")
    demo.create_link(id_genova, id_firenze, 20.0, 1.5, "auto")
    demo.create_link(id_milano, id_roma, 200.0, 0.9, "aereo")
    print("DB Creato")


