<?php
// Vérifiez si le formulaire a été soumis
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Récupérer les données du formulaire
    $nom_utilisateur = $_POST["nom_utilisateur"];
    $mot_de_passe = $_POST["mot_de_passe"];

    // Exécuter le script Python pour vérifier l'authentification
    $command = "python3 /var/www/html/TP1-Redis-INFO834/AdminServices/TP1Redis.py $nom_utilisateur $mot_de_passe";
    $resultat = shell_exec($command);

    // Analyser la réponse du script Python
    if (trim($resultat) === "Connexion réussie") {
        // Rediriger vers la page d'accueil ou une autre page après la connexion réussie
        header("Location: home.php");
        exit;
    } else {
        $message_erreur = "Nom d'utilisateur ou mot de passe incorrect.";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connexion</title>
</head>
<body>
    <h2>Connexion</h2>
    <?php if (isset($message_erreur)) { ?>
        <p><?php echo $message_erreur; ?></p>
    <?php } ?>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="nom_utilisateur">Nom d'utilisateur:</label>
        <input type="text" id="nom_utilisateur" name="nom_utilisateur" required><br><br>
        <label for="mot_de_passe">Mot de passe:</label>
        <input type="password" id="mot_de_passe" name="mot_de_passe" required><br><br>
        <input type="submit" value="Se connecter">
    </form>
</body>
</html>
