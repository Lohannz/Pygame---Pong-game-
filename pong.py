import pygame
from sys import exit

WIDTH = 800
HEIGHT = 500
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

def screen_winner(winner):
    if winner == 1:
        winner_text = 'Esquerdo'
        color = pygame.Color('green')
    else:
        winner_text = 'Direito'
        color = pygame.Color('blue')

    basic_font = pygame.font.Font('./DigitalDisco.ttf', 50)
    text_surf = basic_font.render(f"Ganhador {winner_text}!", True, color)
    text_rect = text_surf.get_rect(midbottom=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text_surf, text_rect)

def ball_moves(ball_rect):
    global vel_ball_x, vel_ball_y

    ball_rect.x += vel_ball_x
    ball_rect.y += vel_ball_y

    # Vencedor esquerdo
    if ball_rect.right >= WIDTH:
        return 1

    # Vencedor direito
    if ball_rect.left <= 0:
        return 2

    # Impede a bola de sair da tela verticalmente
    if ball_rect.bottom >= HEIGHT or ball_rect.top <= 0:
        vel_ball_y *= -1

    if ball_rect.colliderect(opponent_rect) or ball_rect.colliderect(player_rect):
        vel_ball_x *= -1

    return 0

def players_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= 5
    if keys[pygame.K_s]:
        player_rect.y += 5
    if keys[pygame.K_UP]:
        opponent_rect.y -= 5
    if keys[pygame.K_DOWN]:
        opponent_rect.y += 5

    # Impede os jogadores de saírem da tela
    player_rect.y = max(0, min(player_rect.y, HEIGHT - player_rect.height))
    opponent_rect.y = max(0, min(opponent_rect.y, HEIGHT - opponent_rect.height))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('black'))

player_rect = pygame.Rect(0, 400, 10, 70)
opponent_rect = pygame.Rect(790, 400, 10, 70)
vel_ball_x = BALL_SPEED_X
vel_ball_y = BALL_SPEED_Y
ball_rect = pygame.Rect(WIDTH / 2 - 15, HEIGHT / 2 - 15, 30, 30)
game_active = True
resultado = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        screen.blit(background, (0, 0))
        resultado = ball_moves(ball_rect)

        if resultado == 1:
            screen_winner(1)
            game_active = False
        elif resultado == 2:
            screen_winner(2)
            game_active = False

        players_input()
        pygame.draw.rect(screen, pygame.Color('green'), player_rect)
        pygame.draw.rect(screen, pygame.Color('blue'), opponent_rect)
        pygame.draw.ellipse(screen, pygame.Color('yellow'), ball_rect)
        pygame.draw.aaline(screen, pygame.Color('white'), (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 3)

    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            ball_rect.x, ball_rect.y = (WIDTH / 2 - 15, HEIGHT / 2 - 15)
            vel_ball_x = BALL_SPEED_X
            vel_ball_y = BALL_SPEED_Y
            game_active = True

    pygame.display.update()
    clock.tick(60)
