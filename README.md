# TermProject1_The-Cycle

1. Prepare video and background images.
2. In terminal, type 'cd dir_name' (dir_name --> Folder where video and photos are stored)
3. Using Trackbar Function, check the color range of the part I want to extract.
4. Using imshow, make sure that the range of the mask comes out properly(cv.imshow("mask",mask) / cv.imshow("res",res)) also check if the chroma-key video comes out well(cv.imshow("Formatt",Formatt))
5.If the Formatt video doesn't come out well, then change Formatt = np.where(f!=0,image,res) --> Formatt = np.where(f==0,image,f)
6. When the basic setting is all done, type python python_filename input_video.mp4(..) background_img.png(jpg/jpeg/..) result_videoname.mp4(..)
7. Check your folder, then you will find a new Chroma Key video created!
