# 🧠 YOLO + SAM : Détection et Floutage Automatique des Visages

Ce projet combine la puissance de **[YOLO](https://github.com/ultralytics/ultralytics)** pour la détection et le tracking des visages et **[Segment Anything (SAM)](https://github.com/facebookresearch/segment-anything)** pour la segmentation précise, afin de flouter automatiquement les visages dans des **images** ou **vidéos**.

---
## 🤝 Contributeurs

👩‍💻 STEVE DONFACK (https://www.linkedin.com/in/steve-don/)

👨‍💻 TAMDJO CHRISTIAN (https://www.linkedin.com/in/christian-dior-tamdjo/)

---

## 🚀 Fonctionnalités

- 🔍 **Détection précise et tracking** des visages via YOLOv11  
- ✂️ **Segmentation fine** avec SAM (Segment Anything)  
- 🧼 **Floutage automatique** des visages détectés  
- 🖼️ Prise en charge des **images** et **vidéos**  
- ⚡ Exécution sur **GPU** (CUDA) ou **CPU**

---

## 🧩 Dépendances

Assurez-vous d’avoir Python ≥ **3.9** installé.  
Installez les dépendances nécessaires avec :

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install ultralytics opencv-python matplotlib numpy segment-anything

## Poids des modèles:

# Téléchargement du modèle YOLOv11n-Face
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov11n-face.pt -O yolov11n-face.pt

# Téléchargement du modèle SAM ViT-B
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth -O sam_vit_b_01ec64.pth

---
🧾 Résultats

Les résultats actuellement disponibles dans le dossier test/ ont été générés uniquement à partir du modèle YOLO,
car les ressources matérielles actuelles (GPU/VRAM) ne permettent pas encore de réaliser des inférences combinant
YOLO et SAM ViT-B simultanément.

🧠 Une version complète combinant les deux modèles sera ajoutée dès que des ressources matérielles plus puissantes seront disponibles.



