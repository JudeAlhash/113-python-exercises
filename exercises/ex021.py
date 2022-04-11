# 021. Run a mp3 file.

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
pygame.event.wait()
pygame.event.wait()
pygame.event.wait()
