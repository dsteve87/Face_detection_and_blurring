import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
from ultralytics import YOLO
import os

"""
    just with yolo
"""
# Chargement YOLO
model = YOLO("faces.pt")


# Fonction traitement image
def process_image(image):
    results = model(image)[0]

    for box in results.boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.rectangle(mask, (x1, y1), (x2, y2), 255, -1)

        face_region = cv2.bitwise_and(image, image, mask=mask)
        blurred_face = cv2.GaussianBlur(face_region, (101, 101), 0)

        face_removed_image = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
        image = cv2.add(face_removed_image, blurred_face)

    return image

def main():
    parser = argparse.ArgumentParser(description="Flouter les visages sur image ou vidéo")
    parser.add_argument("--input", required=True, help="Chemin du fichier image ou vidéo")
    parser.add_argument("--output", help="Chemin du fichier de sortie (utile pour vidéo)")
    args = parser.parse_args()

    # Vérifie si c'est une image ou une vidéo selon l'extension
    ext = os.path.splitext(args.input)[1].lower()
    image_exts = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]

    if ext in image_exts:  # Cas image
        image = cv2.imread(args.input)
        if image is None:
            raise ValueError(f"Impossible de lire l'image : {args.input}")
        processed = process_image(image)

        # Sauvegarde si output fourni, sinon affichage
        if args.output:
            cv2.imwrite(args.output, processed)
            print(f"Image enregistrée : {args.output}")
        else:
            plt.figure(figsize=(12, 6))
            plt.imshow(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
            plt.axis("off")         
            plt.show()

    else:  # Cas vidéo
        cap = cv2.VideoCapture(args.input)
        if not cap.isOpened():
            raise ValueError(f"Impossible de lire la vidéo : {args.input}")

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out = None
        if args.output:
            out = cv2.VideoWriter(args.output, fourcc, fps, (width, height))
            print(f"Enregistrement vidéo : {args.output}")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            processed = process_image(frame)

            if out:
                out.write(processed)

            cv2.imshow("Blurred Faces", processed)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        if out:
            out.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

