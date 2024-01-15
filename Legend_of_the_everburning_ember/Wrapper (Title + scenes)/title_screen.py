import pygame
import sys
from Main_stage.world_generator import generate_landscape

inTitleScreen = True

# Initialize Pygame
pygame.init()

# Set up display in resizable mode
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Legend of the everburning ember")

# Define the paths to grass, tree, and rock images
grass_images = [
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Grass0 - 0.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Grass0 - 1.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Grass0 - 2.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Grass0 - 3.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Grass0 - 4.png",
]

rock_images = [
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Rock - 0.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Rock - 1.png",
]

tree_images = [
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Tree - 0.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Tree - 1.png",
]

# Load images for different layers
layer_images = [
    pygame.image.load("Wrapper (Title + scenes)/ParallaxBackground/ParallaxBackground/Sky.png").convert_alpha(),
    pygame.image.load("Wrapper (Title + scenes)/ParallaxBackground/ParallaxBackground/DownLayer.png").convert_alpha(),
    pygame.image.load("Wrapper (Title + scenes)/ParallaxBackground/ParallaxBackground/MiddleLayer.png").convert_alpha(),
    pygame.image.load("Wrapper (Title + scenes)/ParallaxBackground/ParallaxBackground/Light.png").convert_alpha(),
    pygame.image.load("Wrapper (Title + scenes)/ParallaxBackground/ParallaxBackground/TopLayer.png").convert_alpha(),
]

# Get the color of the sky from the top-left pixel of the sky image
sky_color = layer_images[0].get_at((0, 0))

# Scale images to screen size
layer_images = [pygame.transform.scale(img, (screen_width, screen_height)) for img in layer_images]

# Set up font
font_path = "Assets/fonts/antiquity-print.ttf"
font_size = 40
font = pygame.font.Font(font_path, font_size)

# Set up text
title_text = "Legend of the Everburning Ember"
play_text = "Play"
new_game_text = "New game"
load_game_text = "Load game"
text_color = (255, 255, 255)
text_render_title = font.render(title_text, True, text_color)
text_render_play = font.render(play_text, True, text_color)
text_render_new = font.render(new_game_text, True, text_color)
text_render_load = font.render(load_game_text, True, text_color)

# Set up text position
text_x = (screen_width - text_render_title.get_width()) // 2
text_y = screen_height - 100

# Set up layer scroll speeds
layer_speeds = [0.1, 0.2, 0.3, 0.4, 0.5]  # Adjust as needed

# Main game loop
running = True
clock = pygame.time.Clock()
frame_count = 0

# Define button functions
def play():
    print("NOT DONE, pressed play")

def load():
    print("NOT DONE, pressed load")

def new_game():
    print("NOT DONE, pressed new game")

# Button properties
button_width, button_height = 100, 50
button_start_y = screen_height // 2
button_spacing = 20

# Button 1 (Play)
button1_rect = pygame.Rect(130, button_start_y, button_width, button_height)

# Button 2 (Extra 1)
button2_rect = pygame.Rect(130, button_start_y + button_height + button_spacing, button_width, button_height)

# Button 3 (Extra 2)
button3_rect = pygame.Rect(130, button_start_y + 2 * (button_height + button_spacing), button_width, button_height)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size
            if inTitleScreen == True:
                screen.fill(sky_color)  # Fill with sky color on resize
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            # Recreate scaled images on resize
            layer_images = [pygame.transform.scale(img, (screen_width, screen_height)) for img in layer_images]
            # Update text position
            text_x = (screen_width - text_render_title.get_width()) // 2
            text_y = screen_height - 100
            # Update button positions
            button1_rect = pygame.Rect(130, button_start_y, button_width, button_height)
            button2_rect = pygame.Rect(130, button_start_y + button_height + button_spacing, button_width, button_height)
            button3_rect = pygame.Rect(130, button_start_y + 2 * (button_height + button_spacing), button_width, button_height)

            # Fit to screen
            generate_landscape(screen, grass_images, tree_images, rock_images)

    # Fill the screen with the color of the sky
    if inTitleScreen == True:
        screen.fill(sky_color)

    # Scroll and loop all layers based on their speeds
    if inTitleScreen == True:
        for i, layer_speed in enumerate(layer_speeds):
            layer_width = layer_images[i].get_width()

            # Calculate the position of the layer
            layer_x = (frame_count * layer_speed) % layer_width

            # Draw the layer twice for looping effect
            screen.blit(layer_images[i], (layer_x, 0))
            screen.blit(layer_images[i], (layer_x - layer_width, 0))

            # Draw the text
            screen.blit(text_render_title, (text_x, text_y))

            # Draw the "Play" button text at the same position as button1_rect
            screen.blit(text_render_play, (130, button_start_y))

            # Draw other buttons
            screen.blit(text_render_new, (130, button_start_y + button_height + button_spacing))
            screen.blit(text_render_load, (130, button_start_y + 2 * (button_height + button_spacing)))

    # Update display
    pygame.display.flip()

    # Check for button clicks
    if inTitleScreen == True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1_rect.collidepoint(mouse_x, mouse_y):
                # play()
                screen.fill((0, 0, 0))
                inTitleScreen = False
                generate_landscape(screen, grass_images, tree_images, rock_images)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button2_rect.collidepoint(mouse_x, mouse_y):
                load()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button3_rect.collidepoint(mouse_x, mouse_y):
                new_game()

    # Control the frame rate
    clock.tick(60)
    frame_count += 1

# Quit Pygame
pygame.quit()
sys.exit()
