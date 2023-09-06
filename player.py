

# import pygame

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = pygame.image.load("blue32ship.gif")
#         self.rect = self.image.get_rect()

#         # Set initial position
#         self.rect.centerx = 500  # Adjust to your desired starting position
#         self.rect.bottom = 600  # Adjust to your desired starting position

#         # Player movement
#         self.playerspeed = 5

#     def update(self, keys):
#         if keys[pygame.K_LEFT]:
#             self.rect.x -= self.playerspeed
#             if self.rect.left < 0:
#                 self.rect.left = 0
#         if keys[pygame.K_RIGHT]:
#             self.rect.x += self.playerspeed
#             if self.rect.right > 1000:
#                 self.rect.right = 1000
