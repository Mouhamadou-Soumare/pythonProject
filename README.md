### Projet FastAPI de Gestion des Étudiants

Ce projet est une API REST développée avec FastAPI pour gérer les informations des étudiants et leurs notes.

## Prérequis

- **Docker** : Assurez-vous d'avoir Docker installé et en cours d'exécution sur votre machine.

## Étapes

1. **Cloner le dépôt**
   ```bash
   git clone git@github.com:Mouhamadou-Soumare/pythonProject.git
   cd pythonProject
   ```

2. **Démarrer Docker**
   Assurez-vous que Docker est en cours d'exécution sur votre machine. Vous pouvez vérifier cela en lançant l'application Docker Desktop ou en exécutant une commande Docker simple comme `docker --version` pour vérifier que Docker répond.

3. **Démarrer le serveur FastAPI avec Docker Compose**
   ```bash
   docker-compose up -d
   ```

   Le serveur sera lancé sur le port `8000`.

## Utilisation de Faker avec Docker

Nous avons utilisé la bibliothèque Faker pour générer des données fictives pour les étudiants et leurs notes. Cela facilite les tests et le développement. Docker encapsule la configuration de Faker, rendant l'application facile à déployer et à exécuter.

## Exporter les Données en CSV

L'application inclut un endpoint pour exporter les données des étudiants en format CSV. Voici comment cela fonctionne :
- Accédez à http://127.0.0.1:8000/ pour le point de terminaison principal.
- Accédez à [http://127.0.0.1:8000/export](http://127.0.0.1:8000/export) pour exporter les données en CSV (par défaut).
- Accédez à [http://127.0.0.1:8000/export?format=json](http://127.0.0.1:8000/export?format=json) pour exporter les données en JSON.

## Documentation de l'API

FastAPI génère automatiquement une documentation interactive que vous pouvez utiliser pour tester les endpoints.

- **Swagger UI** : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints Disponibles

1. **Créer un étudiant** : `POST /students`
2. **Obtenir un étudiant par ID** : `GET /students/{student_id}`
3. **Supprimer un étudiant** : `DELETE /students/{student_id}`
4. **Obtenir une note spécifique d'un étudiant** : `GET /students/{student_id}/grades/{grade_id}`
5. **Supprimer une note spécifique d'un étudiant** : `DELETE /students/{student_id}/grades/{grade_id}`
6. **Exporter les données** : `GET /export`
7. **Voir la liste de tous les étudiants et leurs notes** : `GET /students`
8. **Voir toutes les notes d'un étudiant** : `GET /students/{student_id}/grades`

## Tests des Endpoints avec Postman

Pour tester les endpoints, il suffit de télécharger le fichier `pythonProject.postman_collection.json` qui se trouve à la racine du projet et de l'importer dans Postman.

## Arborisation du Projet

Voici la structure de base du projet :

```
myfastapiproject/
├── app/
│   ├── __pycache__/
│   │   ├── __init__.cpython-312.pyc
│   │   ├── crud.cpython-312.pyc
│   │   ├── database.cpython-312.pyc
│   │   ├── main.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── routes.cpython-312.pyc
│   │   ├── schemas.cpython-312.pyc
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
├── poetry.lock
├── populate_data.py
├── pyproject.toml
└── requirements.txt
```
## Test Pytest

Pour lancer les tests, exécutez la commande pytest depuis le conteneur Docker :


```
docker exec -it <container_id> pytest
```


## Auteur

- Mouhamadou Soumare- [Email](mailto:mouhamadou.soumare@eemi.com)
- Choeurtis Tchounga- [Email](mailto:choeurtis.tchounga@eemi.com)
- Noham Hirep- [Email](mailto:noham.hirep@eemi.com)
- Loanie Urity- [Email](mailto:loanie.urity@eemi.com)

