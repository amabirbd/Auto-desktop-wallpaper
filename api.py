"""pixabay_api_key='4119664-75cc2144f4a944b21e461e646'
	Aurhor : Abir

"""
import urllib.request
import python_pixabay
from bs4 import BeautifulSoup
import os
import ctypes
from random import *

pix = python_pixabay.Pixabay('4119664-75cc2144f4a944b21e461e646')
# custom image search
cis = pix.image_search(q='',
                       response_group = 'high_resolution',
                       safesearch = 'true',
                       order = 'latest',)


#myPath="C:\\Users\\Freeware Sys\\Desktop\\pix"
myPath="C:\\pix"
if not os.path.exists(myPath):
        os.makedirs(myPath)


def get_images(num=randint(1,20)):
    """get image url of the random list indexes"""
    #print(cis['hits'][i]['largeImageURL'])
    u =cis['hits'][num]['largeImageURL']
    return u

i=1
while i<2:
    #call get_images function that returns a string containing url
    img_url = get_images()

    print('Downloading file ')

    filename=img_url.split('/')[-1]
    fullfilename = os.path.join(myPath,filename)
    #print(fullfilename)
    urllib.request.urlretrieve(img_url,fullfilename)
    i+=1

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, fullfilename , 0)
#print(images)




"""
myPath="C:\\Users\\Freeware Sys\\Desktop\\pix"

fullfilename = os.path.join(myPath, 'filename.jpg')
urllib.request.urlretrieve(u, fullfilename)
"""


"""
#after this im using beautiful soup to parse html
#it's really not necessesary.I can just use lareImageURL
#to directly download the image.

#ob=urllib.request.urlretrieve(u, "local.html")
#soup=BeautifulSoup('local.html','html.parser')
#make a function to do all these
#refactor
ob=urllib.request.urlopen(u)
print(type(ob))
soup=BeautifulSoup(ob,'html.parser')
#print(soup.prettify())

all_links=soup.find_all('a')

images = [img for img in soup.findAll('img')]
print (str(len(images)) + "images found.")
"""
