from PIL import Image
import numpy as np

def repeat_key(key, length):
    # Initialize an empty string for the new key
    new_key = ''

    # Loop over the range of the length of the flattened image array
    for i in range(length):
        # Append the corresponding character from the key to the new key
        new_key += key[i % len(key)]

    return new_key


def encrypt_image(image_path, key):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image data to a numpy array
        image_array = np.array(img)

        # Flatten the image array to 1D for easier processing
        flat_image_array = image_array.flatten()

        # Generate the repeated key
        temp_key = repeat_key(key, len(flat_image_array))
        
        # Convert the temp_key to a numpy array
        temp_key_array = np.array([ord(c) for c in temp_key])

        # Perform the encryption by adding the image array to the temp_key_array element by element
        cipher_image_array = [val + temp_key_array[i] for i, val in enumerate(flat_image_array)]

        # Reshape the cipher_image_array back to the original shape
        cipher_image_array = np.array(cipher_image_array).reshape(image_array.shape)

        # Return the cipher image as a PIL Image object
        return Image.fromarray(np.uint8(cipher_image_array))


# Usage:
cipher_image = encrypt_image('image.png', 'caroleensamehsandy')
cipher_image.save('cipher_image2.png')
