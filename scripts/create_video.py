from pathlib import Path

import cv2

img_array = []
root = Path("data/images")
for filename in sorted(root.glob("*")):  # glob.glob("C:/New folder/Images/*.jpg"):
    img = cv2.imread(str(filename))
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)


out = cv2.VideoWriter("project.avi", cv2.VideoWriter_fourcc(*"DIVX"), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
