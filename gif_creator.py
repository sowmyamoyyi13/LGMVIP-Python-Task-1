def resize_image(image_path, target_size=(800, 600)):
    """
    Resize an image to a target size.

    Parameters:
        image_path (str): Path to the image file.
        target_size (tuple, optional): Target size for the resized image. Default is (800, 600).

    Returns:
        PIL.Image.Image: Resized image object.
    """
    image = Image.open(image_path)
    resized_image = image.resize(target_size, Image.LANCZOS)
    return resized_image


def image_to_np_array(image):
    """
    Convert a PIL Image object to a NumPy array.

    Parameters:
        image (PIL.Image.Image): The PIL Image object to be converted.

    Returns:
        np.ndarray: NumPy array representation of the image.
    """
    return np.array(image)


def create_gif(image_folder, gif_path, fps=10, target_size=(800, 600)):
    """
    Create a GIF from a folder of images.

    Parameters:
        image_folder (str): Path to the folder containing images.
        gif_path (str): Path to save the output GIF.
        fps (int, optional): Frames per second for the GIF. Default is 10.
        target_size (tuple, optional): Target size for the resized images. Default is (800, 600).
    """
    image_files = sorted([os.path.join(image_folder, file) for file in os.listdir(image_folder) if
                          file.endswith(('.png', '.jpg', '.jpeg'))])

    if not image_files:
        print("No images found in the specified folder.")
        return

    resized_images = [resize_image(image_path, target_size) for image_path in image_files]
    resized_images_np = [image_to_np_array(image) for image in resized_images]

    clip = ImageSequenceClip(resized_images_np, fps=fps)
    clip.write_gif(gif_path, fps=fps)


# Example usage:
image_folder = r'C:\Users\SURYA\Desktop\unsplash'
gif_path = r'C:\Users\SURYA\Desktop\unsplash\output.gif'
create_gif(image_folder, gif_path, fps=10)
