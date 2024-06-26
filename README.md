### Projet FastAPI de Gestion des Étudiants

Ce projet est une API REST développée avec FastAPI pour gérer les informations des étudiants et leurs notes.

## Prérequis

- **Docker** : Assurez-vous d'avoir Docker installé sur votre machine.

## Étapes

1. **Cloner le dépôt**
   ```bash
   git clone git@github.com:Mouhamadou-Soumare/pythonProject.git
   cd pythonProject
   ```

2. **Démarrer le serveur FastAPI avec Docker**
   ```bash
   docker-compose up -d
   ```

   Le serveur sera lancé sur le port `8000`.



      ### Utilisation de la bibliothèque Faker
      
      Nous avons utilisé la bibliothèque Faker pour générer des données fictives pour les étudiants et leurs notes. Cela facilite les tests et le développement. Docker encapsule la configuration de Faker, rendant l'application facile à déployer et à exécuter.


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

## Arborisation du Projet

Voici la structure de base du projet :

```
myfastapiproject/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── student.py
│   └── tests/
│       ├── __init__.py
│       ├── test_main.py
│       ├── test_student.py
├── .env
├── requirements.txt
└── README.md
```

