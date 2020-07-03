import cv2

# Define the source of the video
#   filename - read video from filesystem
#   integer  - read video stream from webcam

# capture = cv2.VideoCapture("/my/file/video.mp4")
capture = cv2.VideoCapture(0)

index = 0

while True:
    # Read a image frame from video stream
    # grabbed (bool) - check if frame was successfuly read
    # frame          - image frame read
    (grabbed, frame) = capture.read()

    # If video ended/failed then finishes the loop
    if not grabbed:
        break
   
    # Show the curren image frame 
    cv2.imshow("Video", frame)

    # Read a key from user
    key = cv2.waitKey(25)

    # If key is 's' then save the image frame on file 
    if key == ord('s'):
        # Define a new filename
        filename = "image" + str(index) + ".png"
        
        # Save the image frame with filename
        cv2.imwrite(filename, frame)
        
        # Print a message on stdout
        print("Saving ... " + filename)

        # Update the index for next save
        index += 1
    
    # If key is ESC then ends the application
    if key == 27:   #esc
        break

# Release the video capture resources
capture.release()

# Destroy all UI windows
cv2.destroyAllWindows()
