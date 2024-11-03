import pygame

class note:
    coord = None
    hit_time = None
    approach_time = None


    
    def __init__(self, coord, hit_time):
        self.coord = coord
        self.hit_time = hit_time
        self.approach_time = hit_time - 500
        
    def __str__(self):
        return f""
    
    def draw(self, screen, time):
        if self.approach_time <= time <= self.hit_time:
            screen_width, screen_height = screen.get_size()
            x = self.coord[0]
            y = self.coord[1]
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 50)