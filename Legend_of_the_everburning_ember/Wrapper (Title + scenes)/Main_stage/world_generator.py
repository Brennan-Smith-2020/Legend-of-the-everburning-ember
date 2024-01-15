import pygame
import random

def generate_landscape(screen, grass_images, tree_images, rock_images):
    # Load grass, tree, and rock images
    grass_images = [pygame.image.load(image_path).convert_alpha() for image_path in grass_images]
    tree_images = [pygame.image.load(image_path).convert_alpha() for image_path in tree_images]
    rock_images = [pygame.image.load(image_path).convert_alpha() for image_path in rock_images]

    # Set up constants for grid dimensions
    grid_width, grid_height = 550, 250  # Adjust as needed

    # Calculate dynamic tile size based on screen dimensions
    tile_size = min(4,4)

    # Generate random grass tiles
    num_grass_images = len(grass_images)
    for row in range(grid_height):
        for col in range(grid_width):
            grass_image = random.choice(grass_images)
            screen.blit(grass_image, (col * tile_size, row * tile_size))

    # Generate random trees
    num_trees = random.randint(50, 70)  # Adjust as needed
    for _ in range(min(num_trees, len(tree_images))):  # Cap the loop at the length of tree_images
        tree_image = random.choice(tree_images)
        tree_x = random.randint(0, (grid_width - 1) * tile_size)
        tree_y = random.randint(0, (grid_height - 1) * tile_size)
        screen.blit(tree_image, (tree_x, tree_y))

    # Generate random rocks
    num_rocks = random.randint(10, 20)  # Adjust as needed
    for _ in range(num_rocks):
        rock_image = random.choice(rock_images)
        rock_x = random.randint(0, (grid_width - 1) * tile_size)
        rock_y = random.randint(0, (grid_height - 1) * tile_size)
        screen.blit(rock_image, (rock_x, rock_y))

    # Update display
    pygame.display.flip()
