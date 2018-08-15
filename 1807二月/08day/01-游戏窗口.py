import pygame

pygame.init()

clock = pygame.time.Clock()
i = 0

pygame.rect = pygame.Rect(150,500,102,126)

pygame.display.set_mode((480,700))
hero_rect = pygame.Rect((100,500,120,126))

bg = pygame.image.load("./images/background.png")
screen = pygame.display.set_mode((480,700))
screen.blit(bg,(0,0))
hero = pygame.image.load("./images/hero.gif")
screen.blit(hero,(200,500))
pygame.display.update()

while True:
	clock.tick(100)
	print(i)
	i += 1
	hero_rect.y -= 1
	if hero_rect.bottom <= 0:
		hero_rect.top = 700
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	pygame.display.update()
pygame.quit()
