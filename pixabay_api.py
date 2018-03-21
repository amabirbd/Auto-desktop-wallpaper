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


