import os,sys
from pathlib import Path
import cv2 as cv
import numpy as np

#chroma_key.py  input_video.mp4  background.png output_video.mp4 --> argv[0] ,argv[1],argv[2],argv[3]

if(len(sys.argv)!=4):
    print("인자의 갯수가 부족합니다") #인자의 갯수가 부족할 때 오류 처리
    
else: 
    input_video = str(sys.argv[1])
    background_image = str(sys.argv[2])

    video = cv.VideoCapture(str(input_video))
    image = cv.imread(str(background_image)) 

    width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv.CAP_PROP_FPS) 
    nframes = int(video.get(cv.CAP_PROP_FRAME_COUNT))
    fourcc = int(video.get(cv.CAP_PROP_FOURCC))
        
    recorder = cv.VideoWriter(str(sys.argv[3]), 
                                    cv.VideoWriter_fourcc(*'MP4V'), 
                                    fps, 
                                    (640, 480))
        

    #내가 남기고 싶거나 지우고 싶은 부분의 범위를 확인할 수 있는 trackbar

    '''def nothing():
        pass

    cv.namedWindow("Trackbars") #색 범위 확인할 trackbar 300,300size로 만들기
    cv.resizeWindow("Trackbars",300,300)
    cv.createTrackbar("L-H","Trackbars",0,179,nothing)
    cv.createTrackbar("L-S","Trackbars",0,255,nothing)
    cv.createTrackbar("L-V","Trackbars",0,255,nothing)
    cv.createTrackbar("U-H","Trackbars",179,179,nothing)
    cv.createTrackbar("U-S","Trackbars",255,255,nothing)
    cv.createTrackbar("U-V","Trackbars",255,255,nothing)'''
    #opnecv -->H:0-179 S,V:0-255

    while video.isOpened():
        ret,frame = video.read()
        frame = cv.resize(frame,(640,480))
        image = cv.resize(image,(640,480))
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV) #hsv로 바꾸기

        '''l_h = cv.getTrackbarPos("L-H","Trackbars") #Trackbar를 이용해 마스크 지정범위 알아내기 
        l_s = cv.getTrackbarPos("L-S","Trackbars")
        l_v = cv.getTrackbarPos("L-V","Trackbars")
        u_h = cv.getTrackbarPos("U-H","Trackbars")
        u_s = cv.getTrackbarPos("U-S","Trackbars")
        u_v = cv.getTrackbarPos("U-V","Trackbars")'''

        #l_background = np.array([l_h,l_s,l_v])
        #u_background = np.array([u_h,u_s,u_v])
        
        l_background = np.array([0,34,0])
        u_background = np.array([179,255,255])
        
        mask = cv.inRange(hsv,l_background,u_background) #원하는 부분만 분리
        res = cv.bitwise_and(frame,frame,mask=mask) #우리가 원하는 부분

        f = frame - res 
        
        Formatt = np.where(f!=0,image,res) #f!=0인 곳 ->배경 -->그 부분을 image로 대체(f==0인 부분 우리가 원하는 부분)
        
        #cv.imshow("Frame",frame) #frame:origin video
        #cv.imshow("Mask",mask)
        #cv.imshow("Res",res) #우리가 원하는 부분만 추출한 영상
        cv.imshow("Formatting",Formatt) #배경 합성한 영상 --> 최종적으로 우리가 원하는 결과
        
        recorder.write(Formatt) 
        if cv.waitKey(20)==27:break
    
    recorder.release()   
    cv.destroyAllWindows()
        
        