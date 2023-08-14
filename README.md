# watermarker-center
A Python script to add a watermark to multiple photos in a folder.
In order for the script to work, you will need the following first:
-The os Python library installed
-The image Python library installed
-A folder containing all the photos required to watermark
-A watermark in .png format stored in the working directory

The script works as such:
1. Find the watermark image in the working directory and store it as the watermark object.
2. Loop through all the files in the working directory.
3. Within the loop, check if the file is an image ending in .jpg or .png AND is not the watermark image.
4. If the above conditions are fulfilled, check if the resolution of the image is larger than the resolution of the watermark.
5. If the above condition is met, overlay the watermark onto the image in the centre. If not, resize the watermark to a fraction of the resolution of the image, then overlay.
6. Keep repeating until every image has been modified.

The finished product will look like the images here: https://isaactee.glitch.me/vehicles.html
