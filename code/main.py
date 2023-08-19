import pygame, sys, time
from settings import *
from sprites import Player, Ball, Block
from surfacemaker import SurfaceMaker

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Breakout')

        # background
        self.bg = self.create_bg()

        # sprite group setup
        self.all_sprites = pygame.sprite.Group()
        self.block_sprites = pygame.sprite.Group()

        # setup
        self.surfacemaker = SurfaceMaker()
        self.player = Player(self.all_sprites, self.surfacemaker)
        self.stage_setup()
        self.ball = Ball(self.all_sprites, self.player, self.block_sprites)

        # # hearts
        # self.heart_surf = pygame.image.load('../graphics/other/heart.png').convert_alpha()

        # self.music = pygame.mixer.Sound('../sounds/music.wav')
        self.music = pygame.mixer.Sound('../sounds/Phase4.mp3')
        self.music.set_volume(1.0)
        self.music.play(loops=-1)
        

    def create_bg(self):
        bg_original = pygame.image.load('../graphics/other/bg.png').convert()
        scale_factor = WINDOW_HEIGHT / bg_original.get_height()
        scaled_height = bg_original.get_height() * scale_factor
        scaled_width = bg_original.get_width() * scale_factor
        scaled_bg = pygame.transform.scale(bg_original, (scaled_width, scaled_height))
        return scaled_bg
    
    def stage_setup(self):
        # cycle through all rows and columns of BLOCK MAP
        for row_index, row in enumerate(BLOCK_MAP):
            for col_index, col in enumerate(row):
                if col != ' ':
                    # find the x and y position for each individual block
                    x = col_index * (BLOCK_WIDTH + GAP_SIZE) + GAP_SIZE // 2
                    y = row_index * (BLOCK_HEIGHT + GAP_SIZE) + GAP_SIZE // 2
                    Block(col, (x, y), [self.all_sprites, self.block_sprites], self.surfacemaker)
            
        

    def run(self):
        clock = pygame.time.Clock()
        desired_fps = 50

        last_time = time.time()
        while True:

            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.active = True

            # update the game
            self.all_sprites.update(dt)

            # draw the frame
            self.display_surface.blit(self.bg,(0,0))
            self.all_sprites.draw(self.display_surface)

            # update window
            pygame.display.update()

            # Limit the frame rate to the desired FPS
            clock.tick(desired_fps)

if __name__ == '__main__':
    game = Game()
    game.run()

