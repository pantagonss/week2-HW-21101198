import cv2
import numpy as np

def cartoonify_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (500, 500))  # Resize for consistency
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 7)  # Increase blur to reduce harsh textures
    
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                  cv2.THRESH_BINARY, 11, 7)  # Use Gaussian threshold for smoother edges
    
    # Apply bilateral filter for smooth color conversion while enhancing key colors
    color = cv2.bilateralFilter(img, 9, 150, 150)  # Reduce intensity to maintain details
    
    # Enhance orange, yellow, and blue colors
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = cv2.add(hsv[:, :, 1], 40)  # Increase saturation for vibrant colors
    hsv[:, :, 2] = cv2.add(hsv[:, :, 2], 20)  # Increase brightness slightly
    color = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    # Blend color image and edges more smoothly
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)  # Convert edges to 3-channel
    cartoon = cv2.addWeighted(color, 0.85, edges, 0.15, 0)  # Blend color and edge layers
    
    # Stack original and cartoon images side by side
    combined = np.hstack((img, cartoon))
    
    # Display the original and cartoon images
    cv2.imshow("Original vs Cartoon", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
cartoonify_image('naruto2.jpg')
