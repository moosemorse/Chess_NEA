import pygame

class Timer:
    def __init__(self, total_time):
        self.total_time = total_time
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        # Calculate the time passed since the timer was started
        ticks_passed = (pygame.time.get_ticks() - self.start_ticks) // 1000
        time_left = self.total_time - ticks_passed
        return max(time_left, 0)

    def draw(self, screen, font, x, y):
        # Update the time left 
        time_left = self.update()
        # Find minutes and seconds 
        minutes = time_left // 60
        seconds = time_left % 60
        # Timer text '00:00' 
        timer_text = f'{minutes}:{seconds:02d}'
        timer_surface = font.render(timer_text, True, pygame.Color('black')) 

        # Calculate the size of the text for the background rectangle
        text_width, text_height = font.size(timer_text)
        background_rect = pygame.Rect(x, y, text_width, text_height)
        # Draw the background rectangle
        pygame.draw.rect(screen, '#808080', background_rect)
        # Draw the new timer text
        screen.blit(timer_surface, (x, y))

    def is_time_up(self):
        return self.update() <= 0