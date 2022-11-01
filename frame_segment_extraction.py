# Given a path to a video extract frames or segments

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import cv2
from random import sample

class VideoParsing:

    def __init__(self, video_path):
        self.video_path = video_path

    def segment_extraction(self,segment_timestamp_file_path = None, output_dir = None):

        if not os.path.exists(segment_timestamp_file_path):
            print('Segment File Path Not Found')
            return 

        if not os.path.exists(output_dir):
            output_dir = './segments/'
            os.mkdir(output_dir)

        with open(segment_timestamp_file_path) as f:

            times = f.readlines()
            times = [x.strip() for x in times]

            for time in times:
                starttime = float(time.split("-")[0])
                endtime = float(time.split("-")[1])

                ffmpeg_extract_subclip(required_video_file, starttime, endtime, 
                                    targetname=  os.path.join(output_dir, str(times.index(time)+1)+".mp4"))

        return


    def frame_extraction(self, sample_rate = 20, output_dir = None):
        
        if not os.path.exists(output_dir):
            output_dir = './frames/'
            os.mkdir(output_dir)

        video = cv2.VideoCapture(self.video_path)
        count = 0
        while(video.isOpened()):
            ret, frame = video.read()
            if ret == False:
                break
            
            if count%sample_rate==0:
                cv2.imwrite(os.path.join(output_dir, str(count) + 'jpg'), frame)
            
            count+=1

        video.release()
        cv2.destroyAllWindows()



        


    






