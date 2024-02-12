<?php
// Command to execute the Python script
$command = "python3 /var/www/html/TP1-Redis-INFO834/AdminServices/TP1Redis.py";
$nomUtilisateur = 'Arthur'; // Récupérez cela à partir des données de connexion de l'utilisateur
$resultat = shell_exec("python3 TP1Redis.py $nomUtilisateur");

if (trim($resultat) === "L'utilisateur $nomUtilisateur est autorisé à se connecter.") {
    // Connexion autorisée, procédez aux opérations suivantes
} else {
    // Connexion refusée, affichez un message d'erreur
}

?>