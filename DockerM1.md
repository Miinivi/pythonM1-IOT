// Docker doc : https://docs.docker.com/
// Docker installation : https://docs.docker.com/get-docker/
// Get started : https://docs.docker.com/get-docker/

# Docker

* Docker = plateforme pour les développeurs et admins système permettant de "build/run/share" des applications avec des conteneurs

// Différence conteneur image : https://waytolearnx.com/2019/03/difference-entre-une-image-docker-et-un-conteneur.html#:~:text=Un%20conteneur%20Docker%20est%20une%20instance%20ex%C3%A9cutable%20d%27une%20image.&text=Si%20une%20image%20est%20une,dire%20un%20objet%20d%27ex%C3%A9cution

#### Image docker

 > "Une image Docker est un fichier immuable, qui constitue une capture instantanée d’un conteneur. Généralement, les images sont créées avec la commande « docker build ». Et puis, ils vont produire un conteneur quand ils sont lancés avec la commande « run ». En revanche, dans un registre Docker, les images sont stockées comme « registry.hub.docker.com ». Comme elles peuvent devenir assez volumineuses, les images sont conçues pour composer des couches de d’autres images, ce qui permet d’envoyer une quantité minimale de données lors du transfert des images sur le réseau."
 
 #### Conteneur docker
 
 > "Un conteneur Docker est une instance exécutable d’une image. En utilisant l’API ou la CLI de Docker, nous pouvons créer, démarrer, arrêter, déplacer ou supprimer un conteneur. De manière avantageuse, nous pouvons connecter un conteneur à un ou plusieurs réseaux, y attacher de la mémoire ou créer une nouvelle image sur la base de son état actuel. De plus, il consiste en une image Docker, un environnement d’exécution et un ensemble d’instructions standard."

> "Si on applique le concept de l’orienté objet. Si une image est une classe, un conteneur est une instance d’une classe, c’est-à-dire un objet d’exécution. Nous pouvons également dire que les conteneurs sont en quelque sorte la raison pour laquelle vous utilisez Docker car ils constituent des encapsulations légères et portables d’un environnement permettant d’exécuter des applications."

C'est avec Docker que leur utilisation est simplifiée.

#### Conteneurisation

* Conteneurisation = utilisation de conteneurs pour déployer des applications 

La conteneurisation est très populaire car : flexible, léger, portable, etc.

#### Conteneurs et machines virtuelles

Un conteneur tourne de manière native sur Linux et partage le même noyau que celui de la machine hôte, avec les autres conteneurs. Il tourne discrètement, car léger, et ne nécessitant que très peu de ressources (en terme de RAM).

A l'inverse, les machines virtuelles sont plus gourmandes en RAM __ET__ en espace sur le disque dur. 

#### Installation 

Voir le lien plus haut 

#### Tester docker

En premier lieu, on vérifiera sa version avec la commande :

* docker --version

