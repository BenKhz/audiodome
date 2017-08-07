import time

# Start pygame music and play song in audiodome file.

import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('01_A_Night_Of_Dizzy_Spells.mp3')
pygame.mixer.music.play(0)

pygame.event.wait()



while True:
    print("running application")
    time.sleep(60)
