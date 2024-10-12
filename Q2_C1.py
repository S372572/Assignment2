import time
import numpy as np # This time, we will use numpy as was recommended. Numpy is used for array manipulation, allowing us to handle pixel data of the image.
from PIL import Image as img # For ease of understanding and explanation, we will be importing Image as img. This module is used to load, modify, and save images.

# Firstly, we'll have to load the images
question_image = 'chapter1.jpg'  # In the question_image variable, we are saving the original provided image, as it's in the same directory, we don't need to modify the path. 
ans_image = 'chapter1out.png'  # In the ans_image variable, we are saving the new generated image.

# Secondly, we'll open the image in our code alongwith their pixels.
open_img = img.open(question_image) # We will open the image in our code using the Image function of the pillow module.
np_img_pixels = np.array(open_img) # We will then use the array function of the numpy module to save the pixels in an array format in our np_image_pixels variable.

# Thirdly, we'll run the code mentioned in our question to generate a random "n" value, this will be added in the pixel's values.
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print(generated_number)

# The value "n" will now be added to each pixel's (red, green, blue) values. The clip function of numpy is used to keep the value
# of the pixels inbetween 0 and 255. The original pixel value of each color in np_img_pixels is added to the "n" value which is then clipped.  
new_np_img_pixels = np.clip(np_img_pixels + generated_number, 0, 255)

# Now we convert the array back to image using Image module, the "astype" function converts the pixel data to an 8-bit unsigned integer format.
# as required for image storage.
new_img = img.fromarray(new_np_img_pixels.astype('uint8'))
new_img.save(ans_image)

# The sum function will add all the red pixel's values which are represented with a 0 value at the end of the array. 
red_sum = np.sum(new_np_img_pixels[:, :, 0])

# Finally, we will print the success statement and the sum of red pixels.
print(f'New image saved as: {ans_image}')
print(f'Sum of red pixel values: {red_sum}')