import cv2 as cv
import numpy as np
import helper as h


images = [
    cv.imread(f"Images/rider-1.jpg"),
    cv.imread(f"Images/rider-2.jpg"),
    cv.imread(f"Images/rider-3.jpg"),
    cv.imread(f"Images/rider-4.jpg"),
    cv.imread(f"Images/rider-5.jpg"),
    cv.imread(f"Images/rider-6.jpg"),
    cv.imread(f"Images/rider-7.jpg"),
    cv.imread(f"Images/rider-8.jpg"),
    cv.imread(f"Images/rider-9.jpg"),
    cv.imread(f"Images/rider-10.jpg"),

]

# images = images[:9]

# Check if all images are loaded successfully
if all(image is not None for image in images):
    print("All images loaded successfully!")
else:
    print("Error loading some images. Please check paths.")
    exit()

# Output image size
desired_size = (900, 1500, 3)
sizes = h.grid(len(images), desired_size[0], desired_size[1])
collage = np.zeros(desired_size, dtype="uint8")

x = 0
y = 0

# a = np.vstack(images[:5])
# b = np.vstack(images[5:])
# c = np.hstack([a, b])
# cv.imshow("v", c)
# cv.waitKey(0)

if (len(images) % 2 == 0):
    for i in range(len(images)):
        images[i] = cv.resize(images[i], (sizes[0][1][1], sizes[0][0][1]))
        cv.imshow("Collage", images[i])
        print(images[i].shape)
        print(collage[sizes[i][1][0]:sizes[i][1][1], sizes[i]
                      [0][0]:sizes[i][0][1], :].shape)
        collage[sizes[i]
                [0][0]:sizes[i][0][1], sizes[i][1][0]:sizes[i][1][1], :] = images[i]
else:
    for i in range(len(images)-1):
        images[i] = cv.resize(images[i], (sizes[0][1][1], sizes[0][0][1]))
        cv.imshow("Collage", images[i])
        print(images[i].shape)
        print(collage[sizes[i][1][0]:sizes[i][1][1], sizes[i]
                      [0][0]:sizes[i][0][1], :].shape)
        collage[sizes[i]
                [0][0]:sizes[i][0][1], sizes[i][1][0]:sizes[i][1][1], :] = images[i]
    images[len(images)-1] = cv.resize(images[len(images)-1],
                                      (sizes[0][1][1]*2, sizes[0][0][1]))
    print(
        f'last image shae={sizes[-1][1][0]}:{sizes[-1][1][1]}')
    collage[sizes[-1]
            [0][0]:sizes[-1][0][1], sizes[-2][1][0]:sizes[-1][1][1], :] = images[-1]


cv.imshow("Collage", collage)
cv.waitKey(0)
cv.imwrite("collage.jpg", collage)
