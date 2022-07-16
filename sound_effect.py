import pygame


def background_music(option):
    pygame.init()
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.set_volume(0.2)
    if option == 'on':
        pygame.mixer.music.play()
    elif option == 'off':
        pygame.mixer.music.stop()


def eating():
    pygame.init()
    pygame.mixer.music.load('eating.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


def game_over():
    pygame.init()
    pygame.mixer.music.load('game_over.mp3')
    pygame.mixer.music.play()
