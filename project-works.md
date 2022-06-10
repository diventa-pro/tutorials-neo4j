Percorsi Montani
================
Applicazione che serve a pianificare le gite in montagna.
In particolare:
	- consigliare i percorsi in base alla difficoltà, alla durata, e al numero di persone in un gruppo.
	
L'applicazione deve gestire:
Punti di interesse per le gite in montagna:

* Rifugi, dove dormire di notte.
	- nome
	- capacità_max
* Sentieri
	- indice di difficoltà
	- tempo di percorrenza medio
	- numero
* Punti panoramici
	- altezza s.l.m.
* Punti di partenza / arrivo dei sentieri

1. proporre il percorso entro distanze definite per un certo numero di persone. Es "percorso tra 24h e 48h per 5 persone e 1 rifugio"
2. inserire e cancellare gli elementi: rifugi, percorsi, ecc...
	
	
Gestione Rete di distribuzione energia elettrica
================
Le (C)ittà ricevono energia elettrica da (G)eneratori elettrici.
Ad esempio
* G1 fornisce 100MW a Milano
* G2 fornisce 200 MW a Torino e 50MW a Milano
* G3 fornisce 300MW a Torino

Di tanto in tanto i Generatori devono essere spenti, ad esempio per interventi di manutenzione. Tuttavia le città devono continuare a ricevere la stessa quantità di energia. Per questo motivo, esistono dei Generatori di backup per altri Generatori. Quando un Generatore G1 viene spento, il compito di fornire l'energia alle città che G1 alimentava, passa ai Generatori di backup in funzione.

Ad esempio:
G1 fornisce 100MW a Milano
G2 è il backup di G1 ma è spento per manutenzione.
G3 è il backup di G1 ed è in funzione
G4 è il backup di G1 ed è in funzione

G1 viene spento, quindi chi fornirà i 100MW a Milano?
In questo caso G3 dovrà fornire 50MW e G4 altri 50MW. G2 è spento quindi non può fornire alcuna energia.

Un Generatore può fare da backup a tanti altri generatori.

Sequenza di feature da implementare nel programma Python.
1. inizializzare un database Neo4J con un grafo rappresentate una situazione non banale, non è necessario creare dinamicamente nodi o cose simili, si può anche utilizzare una serie di CREATE hardcoded.
2. spegnere un generatore. In questo caso il programma deve chiedere all'utente il nome / identificativo del generatore da spegnere e aggiornare il database creando i nuovi archi rappresentanti la fornitura di energia (attenzione, si devono anche rimuovere quelli relativi al generatore che si sta spegnendo)
3. aggiungere ad ogni generatore un attributo "potenza massima erogabile" e aggiungere una funzione al programma che elenca tutti i generatori accesi che stanno erogando più energia di quella massima.
4. prevedere la riaccensione di un generatore (da pensare come implementarlo)


Stage Formativo in Azienda
========================

Aiutare gli studenti a trovare lavoro nell'azienda dove vorrebbero lavorare.
L'idea è di trovare il docente cha ha seguito negli anni precedenti uno studente in una certa azienda, in modo da creare il collegamento.

Es.
Studente Gianni vuole lavorare presso ACME.
Scopre che professoressa Luisa, 2 anni fa, ha seguito studente Maria in ACME.
Quindi Gianni scopre che può contattare prof. Luisa per essere presentato in ACME.

Quindi:
- data un'azienda dove vorrei lavorare trovare i prof. che hanno rapporti con quell'azienda.
- tra questi trovare qullo più efficiente (che ha aiutato più studenti a lavorare in quell'azienda)

1. cercare il miglior prof che può fungere da collegamento con l'azienda
2. inserire / cancellare gli elementi del database


Gestione Eredità
================

* Persone 
	* nome, cognome
	* data di nascita, 
	* eventuale morte
	
* Rapporti di parentela 
	* figli
	* matrimonio
	
* Proprietà (casa, auto, conto corrente)
	* descrizione
	* tipo
		* immobile
			* indirizzo
		* conti correnti
			* iban
			
* Una certa persona possiede una certa quota di un bene
	* Persona possiede un oggetto
	* percentuale di possesso
	
* Quella persona muore

* Configurare i nuovi possedimenti degli eredi.



		

	