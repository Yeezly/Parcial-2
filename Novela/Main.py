import json
import sys, pygame
pygame.init()

screenw = 1080 
screenh = 800
black = (0, 0, 0)
white = (251, 252, 253)
screen = pygame.display.set_mode([screenw, screenh])
TextFont = pygame.font.SysFont('arial', 14)

open_json = open("Novela/assetsxd.json")
_ = open_json.read()
data = json.loads(_)
act= "inicio"

v = True
while v:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                selection = 0
            if event.key == pygame.K_b:
                selection = 1
            if event.key == pygame.K_z:
                data = open("Novela/assetsxd.json")
                _ = open_json.read()
            if event.key == pygame.K_SPACE:
                v = False

            act = data[act]["choices"][selection]["node"]
    background = pygame.image.load(data[act]["image"])
    y = 550
    screen.fill(black)
    screen.blit(background, (0, 0))

    for i in data[act]["text"]:
        TextDisplay = TextFont.render((i), True, white)
        screen.blit(TextDisplay, (60, y))
        y += 20
    y = 800
    for i in data[act]["choices"]:
        TextDisplay = TextFont.render((i["text"]), True, white)
        screen.blit(TextDisplay, (60, y))
        y += 20

    pygame.display.flip()