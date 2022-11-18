# Given a path to a video extract Segments, Frames and Audio
# Each of these elements of the video are saved in the default that includes 
# frames/<VIDEO_NAME>/frame_count.jpg
# segments/<VIDEO_NAME>/segment_count.mp4
# audio/<VIDEO_NAME>.wav

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import cv2
from random import sample
import moviepy.editor as mp

class VideoParsing:

    def __init__(self, video_path):
        self.video_path = video_path
        self.extension = '.' + self.video_path.split('.')[-1]
        self.name = self.video_path.split('/')[-1].replace(extension, '')

    def segment_extraction(self,segment_timestamp_file_path = None, output_dir = None):

        if not os.path.exists(segment_timestamp_file_path):
            print('Segment File Path Not Found')
            return 

        # if the given output path is None then create an output directory called segments
        
        if not os.path.exists(output_dir):
            output_dir = './segments/'
            os.mkdir(output_dir)
            os.mkdir(output_dir + self.name)
            output_dir = os.path.join(output_dir, self.name)

        with open(segment_timestamp_file_path) as f:

            times = f.readlines()
            times = [x.strip() for x in times]

            for time in times:
                starttime = float(time.split("-")[0])
                endtime = float(time.split("-")[1])

                ffmpeg_extract_subclip(required_video_file, starttime, endtime, 
                                    targetname=  os.path.join(output_dir, str(times.index(time)+1)+".mp4"))


    def frame_extraction(self, sample_rate = 20, output_dir = None):
        
        # if the given output path is None then create a directory called frames
        if not os.path.exists(output_dir):
            output_dir = './frames/'
            os.mkdir(output_dir)
            os.mkdir(output_dir + self.name)
            output_dir = os.path.join(output_dir, self.name)

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

    def audio_extraction(self,audio_path = None):

        name = self.name + '.wav'

        default_audio_path = './audio/'
        if audio_path is None:
            
            if not os.path.exists(default_audio_path):
                os.mkdir(default_audio_path)
                
            audio_path = os.path.join(default_audio_path, name)

        my_clip = mp.VideoFileClip(self.video_path)
        myclip.audio.write_audiofile(audio_path)

        print('Audio Extracted')




        


    






