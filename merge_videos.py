"""combiner 2 vidéos avec la bibliothèque moviepy"""

from moviepy.editor import VideoFileClip, AudioFileClip, clips_array, TextClip, CompositeVideoClip

# Charger les deux vidéos
video1 = VideoFileClip("people.mp4")
video2 = VideoFileClip("ppppp.mp4")

# Redimensionner pour qu'elles aient la même hauteur
h_min = min(video1.h, video2.h)
video1 = video1.resize(height=h_min)
video2 = video2.resize(height=h_min)

# Créer les titres
title1 = TextClip("Original", fontsize=40, color='white', method='caption')
title2 = TextClip("Blurred", fontsize=40, color='white', method='caption')

# Positionner les titres au-dessus des vidéos
title1 = title1.set_position(('center', 'top')).set_duration(video1.duration)
title2 = title2.set_position(('center', 'top')).set_duration(video2.duration)

# Ajouter les titres sur chaque vidéo
video1_with_title = CompositeVideoClip([video1, title1])
video2_with_title = CompositeVideoClip([video2, title2])

# Aligner les vidéos côte à côte
final_clip = clips_array([[video1_with_title, video2_with_title]])

# Définir la durée sur la plus courte des deux
final_clip = final_clip.subclip(0, min(video1.duration, video2.duration))

# 🔊 Ajouter un son de fond
background_audio = AudioFileClip("music_cut.mp3")

# Adapter la durée du son à la vidéo
background_audio = background_audio.subclip(0, final_clip.duration)

# Ajuster le volume (optionnel, 0.0 à 1.0)
background_audio = background_audio.volumex(0.3)

# Combiner le son avec la vidéo finale
final_clip = final_clip.set_audio(background_audio)

# Exporter la vidéo finale
final_clip.write_videofile("output_1.mp4", codec="libx264", audio_codec="aac")
