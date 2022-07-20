import pygame


def background_music(option):
    pygame.init()
    pygame.mixer.music.load('sounds/audio.mp3')
    pygame.mixer.music.set_volume(0.2)
    if option == 'on':
        pygame.mixer.music.play()
    elif option == 'off':
        pygame.mixer.music.stop()


def eating():
    pygame.init()
    pygame.mixer.music.load('sounds/eating.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


def game_over():
    pygame.init()
    pygame.mixer.music.load('sounds/game_over.mp3')
    pygame.mixer.music.play()
