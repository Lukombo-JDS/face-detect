# 📝 TODO

### 🧠 ML & Vecteurs (le cœur du système)

* [ ] **Choisir le modèle**

  * Décider entre **FaceNet (Google)** ou **MobileFaceNet**
  * Objectif : licence gratuite (au moins non-commerciale) pour une démo rapide

* [ ] **Vectorisation des visages**

  * Générer les embeddings pour tous les visages connus
  * Gérer proprement les visages **"inconnus"** dans Milvus

* [ ] **Recherche par similarité**

  * Implémenter le KNN directement sur l’index Milvus
  * Script propre, testable, et optimisé

---

### 🔄 MLOps (amélioration continue)

* [ ] **Boucle d’entraînement**

  * Script de mise à jour du modèle (KNN ou autre)
  * Déclenchement :

    * tous les *n* nouveaux visages
    * ou à chaque batch d’images ajoutées

* [ ] **Exécution en arrière-plan**

  * Lancer les traitements sans bloquer Streamlit
  * (thread, worker, queue… peu importe, mais pas de freeze UI)

---

### 🏗️ Architecture

* [ ] **Refacto en monolithe modulaire**

  * Séparer clairement :

    * vision (ML)
    * stockage (DB / Milvus)
    * logique applicative
  * Objectif : éviter le syndrome spaghetti quand le projet grossit

* [ ] **Réduction de la dette technique**

  * Nettoyage du code
  * Clarification des responsabilités
  * Standardisation minimale (logs, erreurs, etc.)

---

## 💡 V2 — Pistes d’évolution sérieuses

### 🚀 Migration vers Go + FastAPI

Objectif : arrêter de tout faire en Python et préparer un système scalable.

* **Backend en Go**

  * API principale
  * Gestion fichiers / uploads
  * Orchestration
  * Avantages :

    * rapide
    * scalable naturellement
    * concurrence propre (goroutines)

* **Service ML en FastAPI**

  * Garder Python uniquement pour l’IA
  * Exposer des endpoints simples :

    * `/vectorize`
    * `/predict`
  * Le backend Go appelle ces endpoints
