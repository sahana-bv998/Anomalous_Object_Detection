#.................................Preprocess_The_Traindata.....................#
import cv2
import os

def video_to_frames(video, path_output_dir):
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()

#video_to_frames('Test/Smoke.mp4', 'AbnormalBehavior_Data/Train/smoke')
#video_to_frames('Test/Gun.mp4', 'AbnormalBehavior_Data/Train/Gun')
#video_to_frames('Test/Fight.mp4', 'AbnormalBehavior_Data/Train/Fight')

