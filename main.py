import pygame
screen = pygame.display.set_mode((600,700))
player = pygame.image.load("images/player.png")
screen.blit(player, (300,350))
running = True
while running:
  for event in pygame.get.event():
    if event.type == pygame.QUIT():
      running = False #Quit the game
  key_pressed = pygame.key.get_pressed()
  if key_pressed[pygame.key.A]:
    #move the player to the right 
    pass
  if key_pressed[pygame.key.W]:
    #move the player up
    pass
