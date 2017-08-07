import time

# Start pygame music and play song in audiodome file.

import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("01ANightOfDizzySpells.ogg")
pygame.mixer.music.play(0)

pygame.event.wait()



while True:
    print("running application")
    time.sleep(60)
