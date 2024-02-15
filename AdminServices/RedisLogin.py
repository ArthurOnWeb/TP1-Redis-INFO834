import redis
import time

# Configuration de la connexion à Redis
redis_host = 'localhost'
redis_port = 6379
r = redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)

def verifier_connexion_utilisateur(nom_utilisateur):
    """Vérifie si l'utilisateur est autorisé à se connecter."""
    cle_connexion = f"connexion:{nom_utilisateur}"
    return r.get(cle_connexion)

def enregistrer_connexion_utilisateur(nom_utilisateur):
    """Enregistre la connexion de l'utilisateur."""
    cle_connexion = f"connexion:{nom_utilisateur}"
    r.set(cle_connexion, time.time())

def autoriser_acces_service(nom_utilisateur, service):
    """Vérifie si l'utilisateur est autorisé à accéder au service spécifié."""
    cle_acces = f"acces:{nom_utilisateur}:{service}"
    return r.get(cle_acces)

def enregistrer_acces_service(nom_utilisateur, service):
    """Enregistre l'accès de l'utilisateur au service."""
    cle_acces = f"acces:{nom_utilisateur}:{service}"
    r.set(cle_acces, time.time())

# Exemple d'utilisation dans votre serveur web
nom_utilisateur = "Arthur"
service = "Vente"

# Vérifier si l'utilisateur est autorisé à se connecter
if verifier_connexion_utilisateur(nom_utilisateur):
    print(f"L'utilisateur {nom_utilisateur} est autorisé à se connecter.")

    # Vérifier si l'utilisateur est autorisé à accéder au service spécifié
    if autoriser_acces_service(nom_utilisateur, service):
        print(f"L'utilisateur {nom_utilisateur} est autorisé à accéder au service {service}.")
        # Ici, vous pouvez permettre à l'utilisateur d'accéder au service
        # Enregistrer l'accès au service
        enregistrer_acces_service(nom_utilisateur, service)
    else:
        print(f"L'utilisateur {nom_utilisateur} n'est pas autorisé à accéder au service {service}.")
else:
    print(f"L'utilisateur {nom_utilisateur} n'est pas autorisé à se connecter.")

# Enregistrer la connexion de l'utilisateur
enregistrer_connexion_utilisateur(nom_utilisateur)
