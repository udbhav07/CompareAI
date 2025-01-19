import cv2
from skimage.metrics import structural_similarity as ssim
import cv2

def resize_image(image_path, output_path, width=800):
    image = cv2.imread(image_path)
    height = int(image.shape[0] * (width / image.shape[1]))
    resized_image = cv2.resize(image, (width, height))
    cv2.imwrite(output_path, resized_image)

image = cv2.imread('path_to_your_image.jpg')  # Add the correct path to your image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def compare_images(image1_path, image2_path):
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    score, diff = ssim(image1, image2, full=True)
    diff = (diff * 255).astype("uint8")
    return score, diff

score, diff = compare_images('original.png', 'modified.png')
print(f"SSIM Score: {score}")
