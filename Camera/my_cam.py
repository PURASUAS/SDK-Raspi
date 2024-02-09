import os
import time
import cv2
import sys

def main():

    if len(sys.argv)!= 2 :
        total_minute = 5
        print(f"Total Time = {total_minute} minute. \nLET'SSSS GOOOOOOOOOOO!!!!!!!!!")

    else:
        total_minute = sys.argv[1]
        print(f"Total Time = {total_minute} minute. \nLET'SSSS GOOOOOOOOOOO!!!!!!!!!")


    cap = cv2.VideoCapture(0)


    if not cap.isOpened():
        print("ERROR : CAMERA NOT OPENED !!!")
        exit()


    capture_duration = 60 * total_minute
    capture_interval = 1

    output_folder = "captured_photos"
    os.makedirs(output_folder,exist_ok = True)

    start_time = time.time()
    capture_end_time = start_time + capture_duration

    while time.time() < capture_end_time:
        ret,frame = cap.read()

        if not ret:
            print("ERROR : FAILED TO CAPTURE FRAME!!!")
            break
        # Remove hash if you run raspberry with monitor
        # cv2.imshow(window_name,frame)

        current_time = time.time()
        image_name = f"{output_folder}/capture_{str(round(float(current_time-start_time),2))}.jpg"
        cv2.imwrite(image_name, frame)
        time.sleep(capture_interval)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    main()