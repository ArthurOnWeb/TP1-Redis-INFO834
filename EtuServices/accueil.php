<?php
// Chemin vers le script Python
$command = "python3 /var/www/html/TP1-Redis-INFO834/AdminServices/TP1Redis.py";

// Nom de l'utilisateur (remplacez-le par la valeur réelle)
$nomUtilisateur = 'Arthur';

// Exécution du script Python et récupération du résultat
$resultat = shell_exec("$command $nomUtilisateur");

// Vérification du résultat
if (trim($resultat) === "L'utilisateur $nomUtilisateur est autorisé à se connecter.") {
    // Connexion autorisée, redirigez l'utilisateur vers une page de service
    header("Location: services_autorises.php");
    exit();
} else {
    // Connexion refusée, affichez un message d'erreur
    echo "Connexion refusée : $resultat";
}
?>
