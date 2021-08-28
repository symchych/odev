from misc.setting import TestData
from pages.youtube_main_page import YoutubeMainPage
from pages.youtube_channel_page import YoutubeChannelPage
from pages.youtube_video_page import YoutubeVideoPage
from jobs.test_base import BaseTest

class Test_Open_6th(BaseTest):

    '''
    Test case:
    1. Search a video and go inside.
    2. Open a video from recommendation (Select 6th item)
    '''

    #1. Search a video and go inside.
    def search_the_video_and_click(self):
        hi = "hello"


