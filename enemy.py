

# import pygame
# import random

# class Enemy(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = pygame.image.load("redenemyship.gif")
#         self.rect = self.image.get_rect()

#         # Set initial position
#         self.rect.x = random.randint(0, 1000)  # Adjust to your desired starting position
#         self.rect.y = random.randint(180, 250)  # Adjust to your desired starting position

#         self.speedamt = 5

#     def update(self):
#         self.rect.y += self.speedamt

#         # Reset position if enemy goes off screen
#         if self.rect.top > 600:
#             self.rect.x = random.randint(0, 1000)
#             self.rect.y = random.randint(180, 250)

