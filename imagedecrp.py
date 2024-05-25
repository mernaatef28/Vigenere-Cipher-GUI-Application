from PIL import Image
import numpy as np
def repeat_key(key, length):
    # Repeat the key until it matches the length of the image array
    return (key * (length // len(key) + 1))[:length]

def decrypt_image(cipher_image_path, key):
    # Open the cipher image file
    with Image.open(cipher_image_path) as img:
        # Convert the image data to a numpy array
        cipher_image_array = np.array(img)

        # Flatten the image array to 1D for easier processing
        flat_cipher_image_array = cipher_image_array.flatten()

        # Generate the repeated key
        temp_key = repeat_key(key, len(flat_cipher_image_array))

        # Convert the temp_key to a numpy array
        temp_key_array = np.array([ord(c) for c in temp_key])

        # Perform the decryption by subtracting the temp_key_array from the cipher_image_array
        original_image_array = flat_cipher_image_array - temp_key_array

        # Reshape the original_image_array back to the original shape
        original_image_array = original_image_array.reshape(cipher_image_array.shape)

        # Return the original image as a PIL Image object
        return Image.fromarray(np.uint8(original_image_array))

# Usage:
original_image = decrypt_image('cipher_image.png', 'mero')
original_image.save('original_image.png')
