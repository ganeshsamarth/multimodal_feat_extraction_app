import moviepy.editor as mp
import os
class AudioExtraction:

    def __init__(self):
        pass


    def get_audio_from_video(self, path_to_video, audio_path = None):

        # takes input as a .mp4 file and extracts a .wav file
        default_audio_path = './extracted_audio/'
        if audio_path is None:
            name = path_to_video.split('/')[-1].replace('.mp4', '')
            name = name + '.wav'
            if os.path.exists(default_audio_path):
                pass
            else:
                os.mkdir(default_audio_path)
            
            audio_path = os.path.join(default_audio_path, name)

        my_clip = mp.VideoFileClip(path_to_video)
        myclip.audio.write_audiofile(audio_path)

        print('Audio Extracted')
        return
        

