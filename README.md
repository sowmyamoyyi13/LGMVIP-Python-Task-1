# GIF Generator

This Python script creates a GIF from a folder of images using the MoviePy library.

## Requirements

- Python 3.x
- MoviePy library

## Installation

Install the required dependencies using pip:
---pip install -r requirements.txt

Usage
Place the images you want to include in the GIF in a folder.

Update the following variables in the gif_creator.py script:

image_folder: Path to the folder containing your images.
gif_path: Path to save the output GIF.
Run the script:
---python gif_creator.py
Replace python with python3 if you're using Python 3.x and it's not the default version.

Once the script finishes executing, the GIF will be saved in the specified output path.
You can customize the GIF creation process by adjusting the following parameters in the create_gif function in gif_creator.py:

fps: Frames per second for the GIF.
target_size: Target size for the resized images.
