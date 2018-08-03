import numpy as np
import cv2
from openalpr import Alpr

alpr = Alpr("id", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(1)
alpr.set_default_region("id")

cap = cv2.VideoCapture("http://0.0.0.0:4747/mjpegfeed?640x480")
#cap = cv2.VideoCapture("http://192.168.200.22:4747/mjpegfeed?640x480")
#cap = cv2.VideoCapture("sample/1.mp4")
#cap = cv2.VideoCapture(1)

while(True):    
    ret, frame = cap.read() 

    if ret:        
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        cv2.imwrite("img.jpg", frame)

        results = alpr.recognize_file("img.jpg")

        i = 0
        
        for plate in results['results']:
            i += 1
            print("Plate #%d" % i)
            print("   %12s %12s" % ("Plate", "Confidence"))
            for candidate in plate['candidates']:
                prefix = "-"
                if candidate['matches_template']:
                    prefix = "*"

                print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))       
    else:
        break;

    

# When everything done, release the capture
cap.release()
alpr.unload()
cv2.destroyAllWindows()
