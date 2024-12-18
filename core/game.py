import pygame
from note_types.note import note

def main():
    pygame.init()

    running = True
    fullscreen = False

    info = pygame.display.Info()
    screen_width = info.current_w // 2
    screen_height = info.current_h // 2

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My Game")

    clock = pygame.time.Clock()

    test_note = note([200, 200], 1500)
    test_note2 = note([250, 250], 2000)
    
    while running:
        # Clock to limit the frame rate
        time = pygame.time.get_ticks()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen_width // 2, screen_height // 2))
            

        screen.fill((0, 0, 0))

        # Draw a white line in the middle of the screen
        screen_width, screen_height = screen.get_size()
        pygame.draw.line(screen, (255, 255, 255), ((screen_width // 2) - 3, 0), ((screen_width // 2) - 3, screen_height), 6)

        # Draw the test note
        test_note.draw(screen, time)
        test_note2.draw(screen, time)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()