import os
from shutil import copy, rmtree
from PIL import Image

src = r"C:\Users\Andrew\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
dst = r"D:\Coding\2017\scripts\spotlight images\temp"

list_of_files = os.listdir(src)
for f in list_of_files :
	fname = os.path.join(src, f)
	if os.path.isfile(fname) :
		copy(fname, dst)

os.chdir(dst)
list_of_files = os.listdir('.')
for f in list_of_files :
	os.rename(f,f+".jpg")

ctr = 1

list_of_files = os.listdir('.')
for f in list_of_files :	
	im = Image.open(f)
	w,h = im.size
	if w == 1920 :	
		copy(f, r"D:\Coding\2017\scripts\spotlight images\images")
		#os.rename(os.path.join(r"D:\Coding\2017\scripts\spotlight images\images",f), os.path.join(r"D:\Coding\2017\scripts\spotlight images\images", str(ctr)) + ".jpg" )
		#ctr = ctr + 1

#rmtree(dst, ignore_errors = True)
#os.mkdir(dst)