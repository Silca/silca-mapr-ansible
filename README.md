# Mapr Ansible
## par Crédit Agricole Groupe, Silca

*Ce projet réunit l'ensemble de scripts Ansible utilisé pour le déploiement de
cluster MapR au sein du Silca, une filiale du **Crédit Agricole Groupe**.*

Ces scripts permettre de créer, mettre à jour, étendre un cluster MapR sur différents
type de plateforme.

Les plateformes/technologies supportées sont:
- LXC / LXD (Expérimental)
- KVM
- Openstack (Liberty+)

> La documentation en cours d'écriture pour l'installation de cluster LXC, KVM ou Openstack.


## Structure Ansible

La structure des inventaires est la suivante:

* /inventories/**plateforme** - *Le dossier contenant les données d'une plateforme (ex: **os-prod** pour la production, **os-preprod** pour la préproduction)*
* /inventories/plateforme/**common_vars** - *Le dossier contenant les données d'une plateforme (ex: **os-prod** pour la production, **os-preprod** pour la préproduction)*
* /inventories/plateforme/common_vars/**resources** - *Resources propre à la plateforme (private ssh key, ...)*
* /inventories/plateforme/common_vars/resources/**ssh-keys** - *Dossier contenant les roles et clé ssh à déployer automatiquement sur les machines de la plateforme*
* /inventories/plateforme/common_vars/resources/ssh-keys/**root** - *Clés du roles admin*
* /inventories/plateforme/common_vars/resources/ssh-keys/root/**enabled** - *Clés admin à activer*
* /inventories/plateforme/common_vars/resources/ssh-keys/root/**disabled** - *Clés admin à désactiver*
* /inventories/plateforme/common_vars/**all.yml** - *Variables en clair de la plateforme*
* /inventories/plateforme/common_vars/**all_vault.yml** - *Variables chiffrés de la plateforme*
* /inventories/plateforme/**tenant** - *Dossier d'un tenant (ex: filiale_A, filiale_B, filiale_C)*
* /inventories/plateforme/tenant/**group_vars** - *Dossier des variables du tenant*
* /inventories/plateforme/tenant/**all.yml** - *Variables en clair du tenant (ex: surcharge d'une valeur par défaut)*
* /inventories/plateforme/tenant/**all_vault.yml** - *Variables chiffrées du tenant (ex: mot de passe mapr, mot de passe du compte openstack du tenant)*

## Installation KVM

Pré-requis:
- Workstation avec 32Go ram pour 1 noeud Mapr et 1 Ha node, 64Go ram pour 3 noeuds de type Master
- Fedora 24+ ou Ubuntu 16.04+
- KVM
- Squid proxy (optionnel)

> TODO Documentation


## Installation LXC

Pré-requis:
- Workstation avec 32Go ram pour 1 noeud Mapr et 1 Ha node, 50Go ram pour 3 noeuds de type Master
- Ubuntu 16.04+
- LXD / LXC
- Squid proxy (optionnel)
> TODO Documentation

## Installation Openstack
> La documentation en cours d'écriture pour l'installation de cluster LXC, KVM ou Openstack.

Pré-requis:
- Openstack Liberty +
- Machine Ansible accèdant aux api et à l'ip publique des VM
>>>>>>> First Commit. Initializing the project with a clean history
