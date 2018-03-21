"""
	Aurhor : Abir

"""
import urllib.request
import python_pixabay
import os
import ctypes
from random import *
# pixabay_api_key='4119664-75cc2144f4a944b21e461e646'
pix = python_pixabay.Pixabay('4119664-75cc2144f4a944b21e461e646')
# custom image search
cis = pix.image_search(q='',
                       response_group = 'high_resolution',
                       safesearch = 'true',
                       order = 'latest',)


# if directory doesn't exist creat directory to save the pictures
myPath="C:\\pix"
if not os.path.exists(myPath):
        os.makedirs(myPath)


def get_images(num=randint(1,20)):
    """get image url of the random list indexes between 1 - 20"""
    #get the url of the image
    u =cis['hits'][num]['largeImageURL']
    return u

i=1
while i<2:
    #call get_images function that returns a string containing url
    img_url = get_images()

    print('Downloading file ')

	#regular expression  to get the name of the file after the "/"
    filename=img_url.split('/')[-1]
	#joining the path of the downloaded file to th directory
    fullfilename = os.path.join(myPath,filename)
    #print(fullfilename)
    urllib.request.urlretrieve(img_url,fullfilename)
    i+=1
#setting desktop wallpaper for windows
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, fullfilename , 0)
