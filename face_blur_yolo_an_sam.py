import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
from ultralytics import YOLO
from segment_anything import sam_model_registry, SamPredictor

#face detection and blurring with YOLO+SAM vit

# Chargement des modèles

model = YOLO("yolov11n-face.pt")  

sam_checkpoint = "sam_vit_b_01ec64.pth"
model_type = "vit_b"
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device:", device)

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)
predictor = SamPredictor(sam)

# Fonction de traitement d'une image
def process_image(image):
    results = model(image)[0]

    for box in results.boxes.xyxy:
        predictor.set_image(image)
        x1, y1, x2, y2 = map(int, box)
        input_box = np.array([[x1, y1, x2, y2]])
        mask, _, _ = predictor.predict(box=input_box, multimask_output=False)
        mask = mask[0].astype(np.uint8) * 255

        # Zone visage
        face_region = cv2.bitwise_and(image, image, mask=mask)
        blurred_face = cv2.GaussianBlur(face_region, (31, 31), 0)

        # Fusion avec image originale
        face_removed_image = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
        image = cv2.add(face_removed_image, blurred_face)

    return image

def main():
    parser = argparse.ArgumentParser(description="Blur faces in image or video using YOLO + SAM")
    parser.add_argument("--mode", choices=["image", "video"], required=True, help="Mode de traitement")
    parser.add_argument("--input", required=True, help="Chemin du fichier image/vidéo")
    parser.add_argument("--output", help="Chemin de sortie (obligatoire pour vidéo)")
    args = parser.parse_args()

    if args.mode == "image":
        image = cv2.imread(args.input)
        if image is None:
            raise ValueError(f"Impossible de lire l'image : {args.input}")
        processed = process_image(image)
        plt.figure(figsize=(12, 6))
        plt.imshow(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
        plt.axis("off")
        plt.show()

    elif args.mode == "video":
        cap = cv2.VideoCapture(args.input)
        if not cap.isOpened():
            raise ValueError(f"Impossible de lire la vidéo : {args.input}")

        # Préparation de la sortie vidéo
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = None
        if args.output:
            out = cv2.VideoWriter(args.output, fourcc, fps, (width, height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            processed = process_image(frame)

            # Écriture dans le fichier si demandé
            if out:
                out.write(processed)

            # Affichage live
            cv2.imshow("Blurred Faces", processed)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        if out:
            out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
