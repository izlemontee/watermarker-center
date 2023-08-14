import os 
path = 'D:/Pictures/watermarking' #set the path
os.chdir(path) #change cwd
from PIL import Image #import image library

watermark = 'watermark_transparency.png' #the watermark of your choice, MAKE SURE IT'S IN THE WORKING DIRECTORY

logoIm = Image.open(watermark) #use the watermark picture as logoIm
logoWidth, logoHeight = logoIm.size
os.makedirs('withLogo',exist_ok = True) #creates a withLogo folder to store the finished images with logos, True keyword to keep os.makedirs() from raising an exception if withLogo exists

#loop over all files in the working directory
for filename in os.listdir('.'): #if it's os.listdir('.') it returns a list of the files in the cwd
    if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.PNG'))\
        or filename == watermark: #skip if it's the watermark
        continue #skip non-image files and the logo file itself
    im = Image.open(filename)
    width,height = im.size
    #check if image needs to be resized
    if width < logoWidth or height < logoHeight:
        #calculate new width and height to resize to
        watermark_edit = logoIm.copy()
        editWidth, editHeight = watermark_edit.size
        if width < editWidth:
            editWidth = int(width*0.4)
        if height< editHeight: 
            editHeight = int(height*0.4)
        #square the watermark
        if editWidth > editHeight:
            editWidth = editHeight
        elif editHeight > editWidth:
            editHeight = editWidth
        #resize image
        print('Resizing logo for %s...'%(filename))
        watermark_edit = watermark_edit.resize((editWidth,editHeight))
        centre_x =int(width/2 - editWidth/2)
        centre_y = int(height/2- editHeight/2)
        #add logo
        print('Adding logo to %s...'%(filename))
        im.paste(watermark_edit,(centre_x,centre_y),watermark_edit) #pastes logo onto coordinates
        #save changes
        im.save(os.path.join('withLogo',filename)) #saves the changes to a filename in the withLogo directory
    else:
        centre_x =int(width/2 - logoWidth/2)
        centre_y = int(height/2- logoHeight/2)
        #add logo
        print('Adding logo to %s...'%(filename))
        im.paste(logoIm,(centre_x,centre_y),logoIm) #pastes logo onto coordinates
        #save changes
        im.save(os.path.join('withLogo',filename)) #saves the changes to a filename in the withLogo directory
