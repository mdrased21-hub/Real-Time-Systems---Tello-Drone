import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(keyName):
    feedback = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        feedback = True
    pygame.display.update()

    return feedback

def main():
    if getKey("LEFT"):
        print("Left pressed")
    if getKey("RIGHT"):
        print("Right pressed")
if __name__ == '__main__':
    init()
    while True:
        main()