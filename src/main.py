# imports
from pytube import YouTube
import pytube.request
import os
from random import choice
from string import ascii_letters
pytube.request.default_range_size = 9437184  # MB
# # # # # # # # # # # # # # # # # # # # # #  # KB 

class MediaConvertor(object):
    _OPTIONS = ['MP3' , 'MP4']
    _DEFAULT_DOWNLOAD_FOLDER = os.path.join(os.path.dirname(__file__) , 'static' , 'output')
    @staticmethod
    def Download(link:str , option:str , debug:bool) -> dict | None:

        Y_obj = YouTube(link, use_oauth=False, allow_oauth_cache=True)
        Y_obj.bypass_age_gate()

        random_name:str = ""

        for i in range(0 , 12):
            random_name += choice(ascii_letters)

        if option == "MP4":
            random_name += '.mp4'
            try:
                video = Y_obj.streams.get_highest_resolution()
                video.download(filename=random_name , output_path=MediaConvertor._DEFAULT_DOWNLOAD_FOLDER)
                return {'status' : 'Completed' , 'type' : 'MP4' , 'anchor' : f'output/{random_name}'}
            except FileExistsError as error:
                return {'status' : 'Completed' , 'type' : 'MP4' , 'anchor' : f'output/{random_name}'}

        elif option == "MP3":
            random_name += '.mp3'
            try:
                video = Y_obj.streams.filter(only_audio=True).first()
                video.download(filename=random_name , output_path=MediaConvertor._DEFAULT_DOWNLOAD_FOLDER)
                return {'status' : 'Completed' , 'type' : 'MP3' , 'anchor' : f'output/{random_name}'}
            except FileExistsError as error:
                return {'status' : 'Completed' , 'type' : 'MP3' , 'anchor' : f'output/{random_name}'}