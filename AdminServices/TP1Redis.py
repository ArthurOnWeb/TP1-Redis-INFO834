import redis
import time

# Connexion à Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def peut_appeler(nom_utilisateur):
    cle = f"appels:{nom_utilisateur}"
    now = time.time()
    fin_fenetre = now - 600  # 10 minutes en secondes

    # Utilise un pipeline pour atomiser les commandes suivantes
    with r.pipeline() as pipe:
        # Supprime les anciens appels hors de la fenêtre de 10 minutes
        pipe.zremrangebyscore(cle, 0, fin_fenetre)
        # Compte le nombre d'appels dans la fenêtre actuelle
        pipe.zcard(cle)
        # Ajoute l'appel actuel avec le timestamp comme score
        pipe.zadd(cle, {now: now})
        # Met à jour l'expiration de la clé pour libérer de l'espace automatiquement
        pipe.expire(cle, 600)  # Expire après 10 minutes
        _, compteur, _, _ = pipe.execute()

    # Vérifie si l'utilisateur peut faire un appel
    return compteur <= 10

# Exemple d'utilisation
nom_utilisateur = "Arthur"
if peut_appeler(nom_utilisateur):
    print("Appel autorisé")
    # Ici, effectuez l'appel au service
else:
    print("Limite d'appel atteinte")
