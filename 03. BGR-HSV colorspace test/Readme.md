Either run this python script with sudo privileges or create a folder called "Results" first, then run the code. All the images will be stored in the Results folder.

Splitting color/ property channels

BGR
===
B, G, R = cv2.split(image)
B -> Blue Channel
G -> Green Channel
R -> Red Channel


HSV
===
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv_image[:, :, 0] -> Hue Channel
hsv_image[:, :, 1] -> Saturation Channel
hsv_image[:, :, 2] -> Value Channel
