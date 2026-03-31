# ✅ DONE

### 🎨 Frontend & UI (Streamlit)

* ✅ **Upload d’images**

  * Support des fichiers `.jpg`
  * Gestion stable (pas de crash, pas de surprise)

* ✅ **Annotation manuelle**

  * Tag des visages détectés via OpenCV
  * Workflow simple et rapide

* ✅ **Galeries**

  * **Wall of Fame** : visages déjà annotés
  * **Historique** : accès aux images uploadées

* ✅ **Recherche temps réel**

  * Filtrage des noms à la volée
  * UX fluide pendant la saisie

---

### ⚙️ Backend & Infra

* ✅ **Base de données vectorielle**

  * Milvus Standalone opérationnel
  * Déployé via Docker Compose (`/db`)
  * Stable et prêt pour la recherche par similarité

* ✅ **Pipeline ML**

  * Structure en place pour :

    * extraction des visages
    * génération des embeddings
  * Prêt à brancher sur un modèle (FaceNet / autre)

* ✅ **Dockerisation**

  * Image optimisée :

    * utilisation de `uv`
    * `.dockerignore` propre
  * Pas de poids mort inutile

* ✅ **Makefile**

  * Point d’entrée unique pour :

    * build
    * push
    * déploiement
  * Simplifie toute la gestion projet
