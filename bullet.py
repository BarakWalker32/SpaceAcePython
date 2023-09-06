

# import pygame

# class Bullet(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = pygame.image.load("missile.gif")
#         self.rect = self.image.get_rect()

#         # Set initial position
#         self.rect.centerx = 500  # Adjust to your desired starting position
#         self.rect.bottom = 600  # Adjust to your desired starting position

#         self.speedamt = 20
#         self.state = "Ready"

#     def update(self):
#         if self.state == "Fire":
#             self.rect.y -= self.speedamt

#         # Reset position if bullet goes off screen
#         if self.rect.bottom < 0:
#             self.state = "Ready"

