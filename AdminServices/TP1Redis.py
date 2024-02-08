import redis
import time

# Configuration de la connexion à Redis
redis_host = 'localhost'
redis_port = 6379
r = redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)

def enregistrer_connexion(nom_utilisateur):
    """Enregistre une nouvelle connexion pour l'utilisateur et vérifie le quota."""
    cle_quota = f"quota:{nom_utilisateur}"
    cle_timestamp = f"timestamp:{nom_utilisateur}"
    maintenant = time.time()
    fenetre = 600  # 10 minutes en secondes

    # Vérifie si l'utilisateur a déjà atteint son quota de connexions
    quota = r.get(cle_quota)
    dernier_timestamp = r.get(cle_timestamp)

    if quota and int(quota) >= 10 and dernier_timestamp and (maintenant - float(dernier_timestamp)) < fenetre:
        return False  # Quota atteint, connexion refusée

    # Réinitialise le quota si la fenêtre de 10 minutes est écoulée
    if not dernier_timestamp or (maintenant - float(dernier_timestamp)) >= fenetre:
        r.set(cle_quota, 1)
        r.set(cle_timestamp, maintenant)
    else:
        # Incrémente le quota de connexion
        r.incr(cle_quota)

    return True  # Connexion autorisée

# Exemple d'utilisation
nom_utilisateur = "Arthur"
if enregistrer_connexion(nom_utilisateur):
    print(f"L'utilisateur {nom_utilisateur} est autorisé à se connecter.")
else:
    print(f"L'utilisateur {nom_utilisateur} a dépassé le quota de connexions.")
