# Face_detection_and_blurring

# 🧠 YOLO + SAM : Détection et Floutage Automatique des Visages

Ce projet combine la puissance de **[YOLO](https://github.com/ultralytics/ultralytics)** pour la détection des visages et **[Segment Anything (SAM)](https://github.com/facebookresearch/segment-anything)** pour la segmentation précise, afin de flouter automatiquement les visages dans des **images** ou **vidéos**.

---

## 🚀 Fonctionnalités

- 🔍 **Détection précise** des visages via YOLOv11  
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
