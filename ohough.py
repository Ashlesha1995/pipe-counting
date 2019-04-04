import sys
import os
import cv2 as cv
import numpy as np

def main(argv):
    ## [load]##
    default_file =  "..\images\p40.jpg"
    path_list = default_file.split(os.sep)
    #print (path_list)
    #print (path_list[2])
    outimg = path_list[2]
    print(outimg)
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(filename, cv.IMREAD_COLOR)

    # Check if image is loaded fine##
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
       
    ## [load]##

    ## [convert_to_gray]##
    ## [Convert it to gray]##
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ## [convert_to_gray]##

    ## [reduce_noise]##
    ## Reduce the noise to avoid false circle detection##
    gray = cv.GaussianBlur(gray,(5,5),0)
    cv.BORDER_DEFAULT
    gray = cv.medianBlur(gray, 5)
    gray = cv.bilateralFilter(gray,5,5,5)

    ## [reduce_noise]##

    ## [houghcircles]##
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows /100,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
    ## [houghcircles]##

    
    ## [draw]##
    
    if circles is not None:
    
        circles = np.around(circles[0, :].astype("int")
        
        for i,number in circles[0, :]
            center = (i[0], i[1])
            ##circle center##
            cv.circle(src, center, 5, (0, 255, 0),10 )
           
            
            ##circle outline##
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)
            
    ## [draw]##

    ## [display]##
    r = circles.shape[1]
    print(r)
    cv.imshow("detected circles", src)
    optimage ="../output/" +outimg
    print (optimage)
    cv.imwrite(optimage,src)
    edges = cv.Canny(src,100,200)
    #cv.imshow('Edges',edges)
    cv.waitKey(0)
    ## [display]##

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])

