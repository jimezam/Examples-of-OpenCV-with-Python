import cv2

# Define the path to the image file
filename = r"image.png"

'''
enum cv::ImreadModes {
  cv::IMREAD_UNCHANGED = -1,
  cv::IMREAD_GRAYSCALE = 0,
  cv::IMREAD_COLOR = 1,
  cv::IMREAD_ANYDEPTH = 2,
  cv::IMREAD_ANYCOLOR = 4,
  cv::IMREAD_LOAD_GDAL = 8,
  cv::IMREAD_REDUCED_GRAYSCALE_2 = 16,
  cv::IMREAD_REDUCED_COLOR_2 = 17,
  cv::IMREAD_REDUCED_GRAYSCALE_4 = 32,
  cv::IMREAD_REDUCED_COLOR_4 = 33,
  cv::IMREAD_REDUCED_GRAYSCALE_8 = 64,
  cv::IMREAD_REDUCED_COLOR_8 = 65,
  cv::IMREAD_IGNORE_ORIENTATION = 128
}

Reference: https://docs.opencv.org/4.3.0/d4/da8/group__imgcodecs.html#ga61d9b0126a3e57d9277ac48327799c80
'''

# Open the image file: filename, mode
# Reference: https://docs.opencv.org/4.3.0/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

# Create a monochrome version of the image
# Reference: 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show the image loaded in a window: title, image
# Reference: https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563
cv2.imshow("Colored Image", image)

# Show the monocrhome image: title, image
cv2.imshow("Monochrome Image", gray)

# Read any key from keyboard: timeout (milliseconds)
# Reference: https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7
k = cv2.waitKey(0)

# If user pressed 's' saves the monochrome image
if k == ord('s'): 
    # Saves the image: name, image, parameters
    # Reference: https://docs.opencv.org/4.3.0/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce
    cv2.imwrite("mono.png", gray)

# Destroy all windows opened
# Reference: https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga6b7fc1c1a8960438156912027b38f481
cv2.destroyAllWindows()