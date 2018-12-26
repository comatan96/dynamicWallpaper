'''
    Inheritate from base class of the windows services
    changing wallpaper by time
    using macOSMojave wallpaper from:
    https://www.reddit.com/r/apple/comments/8oz25c/all_16_full_resolution_macos_mojave_dynamic/
'''

import ctypes
import time
import datetime
import os
from srvc import WindowsService

class dynamicWallpaperService(WindowsService):
    '''
        overriding the base class variables
    '''
    _svc_name_ = 'dynamicWallpaperService'
    _svc_description_ = 'macOS mojave dynamic wallpaper service'
    _svc_display_name_ = 'Dynamic Wallpaper Service'

    '''overriding start method'''
    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def main(self):
        path = 'C:\\Users\\Public\\Pictures\\mojaveDynamic\\mojave_dynamic_'
        while self.is_running:
            hour = datetime.datetime.now().time().hour
            minute = datetime.datetime.now().time().minute
            if hour >= 4 and hour < 5:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'1.jpeg', 0)
            elif hour >= 5 and hour < 6:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'2.jpeg', 0)
            elif hour >= 6 and hour < 7:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'3.jpeg', 0)
            elif hour >= 7 and hour < 8:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'4.jpeg', 0)
            elif hour >= 8 and hour < 9:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'5.jpeg', 0)
            elif hour >= 9 and hour < 10:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'6.jpeg', 0)
            elif hour >= 10 and hour < 13:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'7.jpeg', 0)
            elif hour >= 13 and hour < 14:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'8.jpeg', 0)
            elif hour >= 14 and hour < 15:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'9.jpeg', 0)
            elif hour == 15 and minute <= 30:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'10.jpeg', 0)
            elif hour >= 15 and hour < 16:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'11.jpeg', 0)
            elif hour >= 16 and hour < 17:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'12.jpeg', 0)
            elif hour >= 17 and hour < 18:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'13.jpeg', 0)
            elif hour >= 18 and hour < 19:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'14.jpeg', 0)
            elif hour >= 19 and hour < 21:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'15.jpeg', 0)
            elif hour >= 21 or hour < 4:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path+'16.jpeg', 0)
            time.sleep(5)
        
if __name__ == '__main__':
    dynamicWallpaperService.handle_cmd()
                
