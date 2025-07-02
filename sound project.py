import pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("C:\\Users\\GKB\\Desktop\\Coding\\Python\\Padman - Aaj Se Teri.mp3")

# 3. Play the Sound    
pygame.mixer.music.play()
print("Press Ctrl+S to play the music")


# 4. Keep the Program Rucnning
print("Playing music... Press Ctrl+C to stop.")
import time

try:
    while pygame.mixer.music.get_busy(): # Keep running as long as music is playing
        time.sleep(1)
except KeyboardInterrupt:
    print("Music stopped by user.")

# 5. Quit Pygame
pygame.mixer.quit("pygame.mixer")
pygame.quit("pygame")    