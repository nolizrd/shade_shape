import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
import cv2

def rgb2hsv(rgb_image):
    return cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

image = plt.imread("balls_and_rects.png")
labeled = label(image.mean(2) > 0)
print(f"Количество фигур всего: {np.max(labeled)}")

# Convert to HSV
hsv = rgb2hsv(image)
h = hsv[:, :, 0]

colors = []
circle_colors = []
rect_colors = []
for region in regionprops(labeled):
    bbox = region.bbox

    if region.eccentricity == 0:
        r = h[bbox[0]:bbox[2], bbox[1]:bbox[3]]
        circle_colors.extend(np.unique(r)[1:].astype(int))
    else:
        
        rect_colors.extend(np.unique(r)[1:].astype(int))


unique_circles = set(circle_colors)

for elem in unique_circles:
    print(f"Оттенок {elem} - {circle_colors.count(elem)} кругов")

unique_rects = set(rect_colors)
for elem in unique_rects:
    print(f"Оттенок {elem} - {rect_colors.count(elem)} прямоугольников")
