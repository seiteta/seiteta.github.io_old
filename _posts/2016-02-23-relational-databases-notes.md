---
layout: post
permalink: /bdd-notes.html
title: 🏫 MOOC Relational Databases – notes
author: Frédéric Bardolle
---

My notes from the [Relational Databases class](https://www.fun-mooc.fr/courses/inria/41008/session01/), taught by Serge Abiteboul, Benjamin Nguyen and Philippe Rigaux from Inria on FUN.

## Semaine 1 : Transactions et concurrence

### 1. Introduction : les transactions

* Propriétés des transactions ACID :
    * Atomicité
    * Cohérence (garantie par le programmeur, à la différence des autres propriétés qui sont garanties par le système)
    * Isolation
    * Durabilité
* COMMIT : valider une transaction
* ROLLBACK : annuler une transaction
* Une transaction : ensemble séquentiel d’opérations permettant de passer d’un état cohérent de la base à un autre état cohérent.

### 2. Les problèmes

* Problèmes d’incohérence : lorsque plusieurs utilisateurs effectuent des opérations conflictuelles
* Anomalie de lecture non reproductible
    * Lecture et écriture de nuplets identiques
    * Lecture, modif, lecture
* Anomalie de lecture fantôme
    * Agrégation, insertion, Agrégation
* Écriture de nuplets identiques : l’ordre importe

### 3. Sérialisabilité

* La sérialisabilité permet de répondre au problème de l’isolation dans le cas de transaction qui s’enchevêtrent
* Un ordonnancement est suite d’opérations de plusieurs transactions, i.e. opérations de type lecture ou écriture.
* Ordonnancement sérialisable si le graphe de précédence est sans circuit (graphe acyclique dirigée).
* Pour résoudre ça : estampillage (curatif) ou verrouillage (préventif)

### 4. Estampillage

* On attribue une estampille à chaque transaction suivant sa date de début.
* Problème : abandon en cascade, risques de privation pour les transactions longues
* Ew(D)>Er(D)

###  5. Verrouillage à 2 phases

* Deux types de verrous : partagé (S) et exclusif (X)
* Les *read* (R) tentent de créer des S, les *write* (W) tentent de créer des X
* Problème : les *deadlocks*, où deux transactions se bloquent mutuellement
* Pour y remédier :
    * *wait-die* : la transaction la plus vieille est mise en attente, la plus récente est annulée.
    * *wound-wait* : la transaction la plus vieille est annulée, la plus récente est mise en attente.
* La sérialisabilité coûte cher en terme de performance. Solutions :
    * Tolérer un certain nombre d’anomalie : degré d’isolation
    * Verrouiller autrement : verrouillage hiérarchique

### 6. Degrés d'isolation dans les SGBD

L’isolation autorise a transgresser la sérialisabilité pour gagner en performance.
4 niveaux : 

* Sérialisable —> SERIALIZABLE : sérialisabilité complète assurée, données verrouillées.
* Lectures reproductibles —> REPEATABLE READ : lectures reproductibles mais requêtes non-reproductibles. Apparition de fantômes (*phantom read*).
* Lectures valides (propres) —> READ COMMITED : lectures et requêtes non-reproductibles. Apparition de fantômes et changement de valeurs déjà lues.
* Lectures dégradées —> READ UNCOMMITED : lectures et requêtes non-reproductibles. Lectures sales (*dirty read*) i.e. sur des données non commitée.

* RC (par défaut Oracle) : beaucoup de lecture, peu d’écriture, transactions longues, peu de transactions
* S ou RR (par défaut MySQL sur table InnoDB) : peu de lecture, peu d’écriture, transactions courtes, beaucoup de transactions
* RU : débug

### 7. Verrouillage hiérarchique
Autre manière d’améliorer les performances. Le verrouillage est une opération O(n) avec n nombre de nuplets.

L’idée est d’adapter la taille du verrou au nombre de transaction.

Nouveaux types de verrou : row share (RS) et row exclusive (RX). Ces verrous sont posés au niveau de la table, et au niveau de la ligne.

Si la décision est NON au niveau table, c’est rapide. Si c’est OUI, on valide sur la ligne, et c’est pareil qu’avant.

* RS (explicite) : toute les lectures de la table sont autorisées, toutes les modifications sont autorisées sauf la ligne verrouillée. *Exemple : on va lire quelques nuplets sur la table, on bloque les personnes qui souhaiterait modifier l’intégralité des données.*
* RX (implicite) : permet RS et RX, empêche S et X sur les nuplets. *Exemple : on veut modifier des données de la table, on bloque les personnes qui souhaiterait lire l’ensemble de la table.*
* SRX (share row exclusive) : un S et un RX en même temps, permet RS. Moins permissif que S. *Exemple : on va lire certaines données de la table, on ne bloque rien à part des personnes qui souhaiterait modifier la table.*


## Semaine 2 : Indexation

### 1. Introduction

Le but : accès à de gros volumes de données. Pour cela : système de fichiers ou SGBD.


Pour les systèmes de fichiers, on peut accélérer grâce à la compression, à la fragmentation, ou au partage du fichier en blocs.

On peut garder plusieurs blocs en mémoire dans un *buffer*. Exemple de stratégie de remplacement des blocs : LRU (*least recently used*).

*Clustering* (regroupement) : on regroupe dans un même bloc des données souvent utilisées ensemble.

### 2. Hiérarchie de mémoire

Plusieurs critères de stockage : débit, taille et coût.

Mémoire RAM (*random access memory*) :

* Semi-conducteur
* Très rapide (accès micro-secondes)
* Volatile, petite et chère

Disque :

* Lent (accès milli-secondes)
* Persistantes, massive et bon marché

Bande magnétique :

* Encore plus lent, mais encore plus massive

Flash :

* Semi-conducteur
* Plus rapide qu’un disque, moins cher que la RAM
* Persistant

On aimerait une grande base de données rapide et bon marché. Pour cela, on mélange les différents types de mémoire.

### 3. Fichiers indexés

Un fichier indexé est une séquence de nuplets (ou enregistrement).

Un index sur un des attributs des nuplets permet un accès direct.

Accès séquentiel :

* Taille fixe : insertion en fin de fichier, suppression coûteuse (résolu avec un bit qui indique qu’un nuplet est vide)
* Taille variable : problème de fragmentation —> solution hybride (taille fixe + débordement)

Accès direct, trouver un nuplet :

* Parcourir le fichier (lecture de N/2 en moyenne)
* Divide and conquer (lecture de log(N) en moyenne)
* Utiliser un index (on garde cette structure en mémoire)

Fichiers indexés (non dense) :

* Fichier trié selon un attribut
* On construit un index pour cet attribut
* Lecture : un seul bloc
* Insertion : rien à faire
* Suppression rien à faire

Fichier indexé (dense) :

* Fichier non trié selon l’ordre de l’attribut
* Un adresse de nuplet par valeur
* Lecture : au pire un bloc pour chaque nuplet
* Insertion : insérer la clé de l’index
* Suppression : supprimer la clé de l'index

« Ce n'est pas chaque bloc qui est référencé par un index, mais chaque enregistrement. Un bloc sera donc référencé plusieurs fois. »

### 4. Arbre-B

Le principe : le fichier est découpé en bloc ; on a des index et aussi des index d’index.

* nœud de l'arbre (une boite en vert avec 7 compartiments)
* adresse ou pointeur (arc en bleu) : permet de passer d'un nœud à un autre jusqu'à arriver à un bloc de données
* clé : une valeur qui détermine l'enregistrement que l'on cherche. L'animation montre comment récupérer l'enregistrement de clé 55.
* bloc de données (boite bleue) : contient des enregistrements

Pour une recherche de clé : descente en O(log(n))

Avantage : on peut faire des requêtes d’intervalles.

Si arbre déséquilibré : descente en O(n). —> à chaque accès on essaie de rééquilibrer l’arbre.

### 5. Hachage

Table de hachage (aléatoire) T[1..N] : N pointeurs vers N blocs.

Fonction de hachage H : le nuplet de clé K est géré par le bloc T(H(K)).

Exemple : on veut ajouter l’enregistrement lili. Si H(lili)=2, on met lili dans le bloc 2.

On ajoute des enregistrements jusque’à que les blocs soient pleins.

Si le bloc est plein (débordement), on chaine.

Pas trop de problème de débordement (marche bien) avec un taux de remplissage de 60%.

### 6. Hachage dynamique

La table de hachage a une taille variable (1, 2, 4, 8, …).

Quand un bloc est plein, il éclate et on augmente la taille de la table.

Bonne performance. Travail pour double la taille de la table (mais pas sur disque). Pour amortir ce travail : hachage linéaire.


«  Lorsque je dois insérer un n-uplet, je n'ai "rien à faire" tant que la fonction de hashage donne un résultat pointant vers un bloc qui n'est pas plein. Dans le cas contraire : - soit plusieurs résultats de la table de hashage pointent vers le bloc et il n'y a qu’à éclater ; - soit il n'y a qu'un résultat de la table de hashage et je dois doubler la taille de la table de hashage avant d'éclater. Il y a donc pas nécessairement doublement de la taille de hashage à chaque fois qu'il y a éclatement d'un bloc.

Par ailleurs, lorsque j'éclate un bloc, il est possible qu'une partie des n-uplet de ce bloc soit à déplacer dans le nouveau bloc (ceux qui auraient le même résultat de hachage). » 

### 7. Multi-Hachage

Filtre de Bloom : basé sur sur plusieurs fonctions de hachage.

* On construit le filtre de telle sorte que Bloom(h_i(m)) = 1, c’est-à-dire que si on applique le filtre de Bloom à toutes les fonctions de hachage h_i (appliqué à l’élément m), on aura 1.
* Comme ça, si on veux savoir si un autre élément m' est présent, on fait Bloom(h_i(m’))
    * si c’est != 1, alors on est sur qu’il est pas présent (pas de faux-négatif)
    * si c’est = 1, alors on espère qu’il est présent (possible faux-positifs)
* Bonne explication : http://bioinfo-fr.net/filtre-de-bloom



## Semaine 3 : Exécution et optimisation

### 1. Introduction

* Requête déclarative : ne dit pas comment calculer le résultat.
* Plan d’exécution : le programme qui exécute la requête. Arbre constitué d’opérateurs 
* Optimisation de requêtes : à chaque étapes, le système a le choix entre plusieurs décisions (plan d’exécution logique et physique)

### 2. Réécriture algébrique

* Commutativité des jointures R ⋈ S ≡ S ⋈ R
* On crée comme ça des expressions équivalentes pour une même requête
* On ne peut pas explorer tout l’espace des expressions équivalentes —> utilisation d’heuristique
    * Heuristique classique : réduire la taille des données
    * Filtrage des nuplets par sélections
    * Simplification par des projections
    * —> Sélection et projections le plus tôt possible
 
![propriete-algebrique](/downloads/bdd-propriete-algebrique.png "Propriétés algébriques")

### 3. Opérateurs

* Un plan d’exécution est un arbre constitué d’opérateurs échangeants des flux de données
* Les opérateurs :
    * ont une forme générique (itérateur)
    * fournissent une tâche spécialisée
    * peuvent être bloquant ou non
* Mode matérialisation : un opérateur calcule son résultat et le transmet
    * Consomme de la mémoire
    * Temps de latence
* Mode pipelinage : le résultat est produit à la demande
    * Plus de stockage intermédiaire
    * Latence minimum
* On ne peut pas traiter tous les opérateurs en pipelinage s’ils sont bloquants :
    * Exemple : `select min(date) from T`
    * `min` oblige a parcourir toute la table
* Temps de réponse : temps pour obtenir le premier nuplet
* Temps d'exécution : temps pour obtenir tous les nuplets

### 4. Plans d’exécution

* Un opérateur est un itérateur. Trois fonctions :
    * open : initialise les ressources et positionne le curseur
    * next : ramène l’enregistrement courant et se place sur le suivant
    * close : libère les ressources 
* Itérateurs source et produit
* Exemple d’opérateur :
    * *FullScan* (voir ch3) : parcours séquentiel de la table
    * *IndexScan* (Arbre-B) : parcours d’un index
    * *DirectAccess* : accès par adresse à un nuplet
    * *Filter* : test de la condition
    * Utiliser ou pas l’Index ? Des fois c’est moins intéressant, quand les données sont fractionnées sur plusieurs blocs.

### 5. Tri et hachage

* Deux nouveaux opérateurs : tri et hachage.
* Tri : opérateur bloquant (donc coûteuse)
    * Utilisé pour les algos de jointure (*sort/merge*)
    * l’élimination des doublons (*clause distinct*)
    * les opération de regroupement (*group by*)
    * les *order by*
* Tri-fusion (externe) (= mergesort). Le tri se fait en phase de open, càd avant le *next* (fusion).
    * Cas favorable : on charge tout dans la RAM et on fait un *quicksort*
    * Cas non-favorable : on lit un fragment, on trie (en RAM, avec *quicksort*), on stock —> N fragments triés qu’on va fusionner. Pour la fusion, on place un curseur au début de chaque fragment, on compare et on prend la plus petite.

### 6. Algorithmes de jointure

* Un nouvel opérateur : jointure
* Type de requête : `select a ... from T1, T2 ... where T1.x = T2.Y ... order by ...`
* Jointure avec index :
    * Boucle imbriquées indexées
    * Plus courante : naturellement sur les clefs primaires/étrangères
    * Fonctionne en mode pipeline
    * *FullScan* sur la table de gauche, *IndexScan* sur la table de droite
* Jointure sans index :
    * Boucle imbriquées (non indexées) : on teste toutes les solutions possibles. Coût quadratique.
    * Jointure par hachage. Si tient en mémoire —> joinlist. Sinon, on découpe les deux tables en *k* fragments (qui tiennent en mémoire) avec la même fonction de hachage.

### 7. Optimisation

* Les jointures sont commutatives -> il faut mettre la table avec la clef primaire indexée à droite

TP
La sélectivité (nombre de nuplets sélectionnés) diminue puisque il y a plus de films après 1980 qu'après 2015. Du coup Postgres a déterminé qu'un parcours séquentiel devenait préférable. Cela illustre un des aspects vus en cours: **un index n'est valable que quand on sélectionne une faible partie des données**. Vous pouvez varier l'année et regarder celle qui induit un changement de plan d’exécution.

## Semaine 4 : Contrôle d’accès

### 1. Introduction

Sécurité d’accès à l’information.

* Intérêt évident à attaquer les BDD pour dérober des données structurées de grande qualité
* Attaquants : pirate, service de renseignement, hébergeur ou utilisateurs

Mécanisme de défenses :

* Authentification
* Protection des communication
* Contrôle d’accès
* Chiffrement des données
* Audit
* Contrôle d’usage
* Rétention limitée des données
* Anonymisation des données
* Législation

Contrôle d’accès :

* Qui, est autoriser à faire quoi, sur quelles données, dans quelles conditions.

### 2. Modèle de contrôle d'accès discrétionnaire (DAC)

* Par défaut, tout est interdit.
* Le créateur d’un objet est le propriétaire de cet objet
* Il fixe la politique de contrôle d’accès. Certaines permissions sont transférables.
* Modèle décentralisé : souple, mais difficile à administrer
* Les droits sont représentés sous forme de matrice : *Capacity List* ou *Access Control List*
* Commande `GRANT…  (ON…  TO… )` : donne des droits
* Commande `REVOKE…  (ON…  FROM… )` : retire des droits.
    * `CASCADE` : retire les droits en cascade
    * `RESTRICT` : retire les droits pas en cascade
* Les requêtes sont faites sur des vues (pas sur la table).

### 3. Modèle de contrôle d'accès basé sur les rôles (RBAC)

* Les accès des utilisateurs sont gérés en fonction de leur rôle organisationnel
* Gestion des droits facilitée
* Commande `CREATE ROLE` : création d’un nouveau rôle
* Commande `DROP ROLE` : suppression d’un rôle
* Commande `SET ROLE` : activation d’un rôle pendant une session
* `GRANT` : fonctionne toujours
* On peut faire hériter des rôles (hiérarchie organisationnelle ou spécialisation)
* On peut ajouter des contraintes (utilisateur/rôle, session/rôle ou rôle/permission)
* Depuis 2010, ABAC : *Attribute Based Access Control*

### 4. Modèle de contrôle d'accès obligatoire (MAC)

* Limites du DAC et du RBAC : risque de cheval de Troie
* Cloisonnement vertical (niveaux de sécurité hiérarchique) et horizontal (DRH, DAF, …)
* Classe d’accès : combinaison d’un niveau de sécurité et d’une catégorie
    * Niveau de sécurité pour un objet : classification
    * Niveau de sécurité pour un utilisateur : niveau d’accréditation (clearance)
* Deux règles pour la décision d’accès : 
    * *No read up* : exemple, si on peut lire « confidentiel », on peut pas lire « top secret »
    * *No write down* : exemple, si j’ai accès à « top secret », je peux pas envoyer des données dans « confidentiel »
* Oracle Label Security : level, compartment et group
* Pour accéder à une données :
    * user.level >= data.level
    * data.compartement ⊆ user.compartment
    * user.group ⊆ data.group

## Semaine 5 : Reprise sur panne

### 1. Introduction

* Panne légère : affecte la RAM, pas les disques
* Panne lourde : affecte un disque
* Garantie :
    * Durabilité et atomicité : après un commit toutes les modifications de la transaction deviennent permanentes
    * Recouvrabilité et atomicité: tant qu’un `commit` n’a pas eu lieu, on doit pouvoir annuler par un rollback.
* Pour garantir un `commit`, les données modifiés doivent être sur le disque (image après)
* Pour garantir un `rollback`, les données avant modification doivent être sur le disque (image avant)
* État de la base : ensemble des transactions validées —> doit toujours être sur le disque.

### 2. Lectures et écritures, buffer et disque

* En lecture, quand la mémoire est pleine, généralement on fait de la LRU (*Least Recently Used*)
* En écriture, le bloc est modifié dans le *buffer* (image après), pas directement sur le disque (image avant).
* Plusieurs modes de synchronisation entre *buffer* et disque :
    * Mise à jour immédiate : image avant écrasée, écriture aléatoire
    * Mise à jour différée : mise à jour effectuée après le commit —> image avant préservée, risque de surcharger le buffer.
    * Mise à jour opportuniste : mise à jour effectuée au meilleur moment (quand le disque est peu actif par exemple) —> plus courant (meilleures performances), une partie de l’image avant est écrasée.

### 3. Première approche

* Panne légère (RAM perdue)
* MàJ opportuniste : recouvrabilité non garantie
* MàJ immédiate : recouvrabilité non garantie
* MàJ différée : recouvrabilité non garantie (si panne pendant l’écriture juste après le commit)
* Il faut donc avoir sur le disque l’image avant et l’image après —> journal des transactions

### 4. Le journal des transactions

* On écrit séquentiellement dans le journal de transaction (ou *log*)
* Le *log* a son propre buffer
* On n’efface jamais un enregistrement du *log*
* La base et son buffer sont en écriture opportuniste
* Le *log* et son *buffer* sont en écriture immédiate
* Contenu du *log* : toutes les instructions de MàJ (y compris ancienne et nouvelle valeurs)
* Au `commit`, on force l’écriture des modifications du *log*. La transaction est validée quand le `commit` est écrit dans le *log*.
* Pour le rollback, on annule l’écriture de blocs sur le disque, car on a la trace dans le log des modifications non validée (*write-ahead logging*)

### 5. Algorithmes de reprise sur panne

* Panne légère (écriture opportuniste) : des modifications validées pas dans la base, des modifications non validées dans la base
* Refaire (*redo*) les transactions validés et défaire (*undo*) les transactions en cours
* On regarde la liste des transactions validées L_v (commit dans le log) et annulées L_a (pas de commit).
* UNDO : Dans l’ordre inverse d’exécution, on prend chaque transaction de L_a et on remplace la `new_val` par `old_val`.
* REDO : Dans l’ordre d’exécution, on prend chaque transaction de L_v et on remplace la `old_val` par `new_val`.
* Algo de reprise : tous les undo, puis tous les redo.
* Pour ne pas tous se retaper depuis la création de la base à chaque panne, on a des *checkpoints* où on écrit sur disque tous les blocs modifiés. Les transactions ayant eu lieu avant un *checkpoint* sont validées, pas besoin de les considérer pour la reprise.

### 6. Pannes de disque

* Solution : la réplication
* L’état de la base est à la fois dans le *log* et dans le fichier de la base + *buffer*.
* Il faut donc que le log et la base soient sur deux disques différents
* S i panne du disque de la base : on reconstruit avec le log et on utilise des sauvegardes pour pas avoir à tous se retaper et garder un *log* super long.
* Si panne du disque du *log* : on fait un *checkpoint*, on arrête tout et on redémarre (seulement si MàJ différée). Mais s’il y a une panne légère, on est niqué ! Du coup, on peut répliquer le *log*.


## Semaine 6 : Bases de données distribuées

### 1. Introduction

* Les données sont souvent distribuées dans plusieurs SGBD et/ou plusieurs base de données.
* Un système distribué est une application qui coordonne les actions de plusieurs ordinateurs pour réaliser une tâche particulière.
* Une base de données distribués : une grande quantité de données résidant sur plusieurs machines.
* Tout doit être transparent pour l’utilisateur : OSEF de la localisation, du réseau/système, de la fragmentation ou de la réplication
* Avantages : meilleures performances, possibilité d’intégration de plusieurs BDD d’origine différente, réplication des données.
* Inconvénients : complexité, absence de standard, incohérences

### 2. Différentes architectures

* Mono-machine : pas de distribution
* Architecture client-serveur : client (application, GUI) et serveur (gestion des requêtes, transactions, pannes, etc.)
* Architecture 3 niveaux (*3-tier*) : client (navigateur web), intermédiaire (application, communique avec le SGBD), serveur (BDD)
* Typologie : hétérogénéité des SGBD locaux
* Typologie : degré d’autonomie (d’intégration forte à autonomie forte)
* La médiation : fait le lien entre l’application et les adapteurs des différents SGBD

### 3. Fragmentation

* Deux types de fragmentation : horizontale et verticale
* Correspond aux deux types de stockage : par ligne (nuplet) et par colonne
* Stockage en ligne : exemple MySql, lecture/écriture rapide de nuplets, transactionnel
* Stockage en colonne : exemple Google Big Table, lecture/écriture rapide d’attributs, excellente compression, décisionnel
* Obligation : pas de perte d’information
* Préférable : pas de redondance

### 4. Optimisation de requête

* Nouveaux plans d’exécutions dû à l’architecture distribuée
* Centralisation brutale : on envoie tout
* Solution optimisée : on envoie qu’une partie des données
* Les problèmes sont séparés pour simplifier : analyse syntaxique, localisation, optimisation globale (minimisation des communications), optimisation locale (minimisation des I/O et des calculs) 

### 5. Réplication

* La réplication est utilisée principalement pour la fiabilité.
* Une autre raison : les performances
* *Trade-off* : requêtes vs mises-à-jour

### 6. Concurrence

* Sans réplication, la notion de sérialisabilité s’étend, le verrouillage à deux phases aussi. Plus dur de détecté les *deadlocks* —> *timeout*.
* Si réplication, deux méthodes :
    * Réplication asynchrone (incorrecte, pas de cohérence)
    * Technique ROWA (*read-once/write all*) : lecture sur une des copies, écriture sur toutes les copies.

### 7. Conclusion : cinq tendances

* *Cloud* : appli et données dans le cloud
* NoSQL : pour les applications « extrêmes » : applications transactionnelles (millions de transactions pas seconde) ou décisionnelles (analyse de téraoctets de données). Langage plus simple, modèle plus simple, moins universel.
* Pair-à-pair : chaque machine est à la fois un serveur et un client.
* Big data : de plus en plus de données, analyse des données (*machine learning*), calcul massivement parallèle (Hadoop), systèmes NoSQL
* Base de données en mémoire : des serveurs avec tellement de RAM que les BDD tiennent dedans (*blade server 100 cores, 10 Tb de mémoire*).
