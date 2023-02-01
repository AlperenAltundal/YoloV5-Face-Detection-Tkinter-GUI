import torch            
import numpy as np      
import cv2             
from time import time   
import imutils
import matplotlib.pyplot as plt
import threading
import numpy as np


class FaceDetector:   
    

    def __init__(self, capture_index, model_name): 
        self.capture_index = capture_index                             
        self.model = self.load_model(model_name)                        
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'    
        print("Using Device: ", self.device)                       

    def get_video_capture(self):        
        return cv2.VideoCapture(0)
       

    def load_model(self, model_name):
        if model_name:
            model = torch.hub.load('C:/Users/pc/yolov5-master', 'custom',source = 'local', 
            path=model_name, force_reload=True)   
        else:
            model = torch.hub.load("C:/Users/pc/yolov5-master/data", 'custom', 
            path='best_face_2.pt', source='local')    
        return model
    
    counter=0
    count=0
    cx1=200
    offset=6

    def score_frame(self, frame):
     
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord


    def class_to_label(self, x):
        return self.classes[int(x)]       
    

    def plot_boxes(self, results, frame,TouchSayac):  
        
        #düz çizgi
        BoundCizgi=cv2.line(frame,(275,250),(275,450),(0,250,246),2)
        #kare
        kare = cv2.rectangle(frame, (175,250), (375,450), (0,191,255), 2)

        Z_ekseni=cv2.circle(frame, (1000,250), 5, (0,0,255), 10) 
        
        CounterTouch=0
       
        labels, cord = results
        
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.7:
                
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape),int(row[2]*x_shape), int(row[3]*y_shape)

                bgr = (0, 255, 0)
                sayi = float(row[4])
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr,2)

                rectx1, recty1 = ((x1+x2)/2, (y1+y2)/2)
                rectcenter = int(rectx1),int(recty1)
                cx=rectcenter[0]
                cy=rectcenter[1]
                cv2.circle(frame,(cx,cy),5,(0,255,0),-1)
          
                KeyPoint=cx,cy
                
                if (cx >=270) and (cx <= 280) and (cy >=250) and(cy <= 450): 
                    print("Etiketi: " + self.class_to_label(labels[i]) + " olan, keypoint noktasi " + str(KeyPoint) + ' olarak temas ettigi tespit edildi.')
                    cv2.circle(frame, (200,150), 10, (0,255,255), 10) 
                    cv2.putText(frame,'degdi',(210,150),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA)
                    TouchSayac+=1
                    print(TouchSayac) 

                cv2.putText(frame, self.class_to_label(labels[i])+'    '+  str(KeyPoint) + '    '+ str(round(sayi, 2)),
                            (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)


        result = dict()
        result['frm'] = frame
        result['count'] = TouchSayac

        return result

    def __call__(self):                 
        cap = self.get_video_capture()
        assert cap.isOpened()
        cx1=200
    
        TouchCount1=0
        

        while True:
            
            ret, frame = cap.read()
            assert ret

            frame = cv2.resize(frame, (1280, 720))    
            
            start_time = time()                   
            results = self.score_frame(frame)
            result = self.plot_boxes(results, frame,TouchCount1)
            frame=result["frm"]
            TouchCount1=result["count"]
            
            end_time = time()
            fps = 1/np.round(end_time - start_time, 2)

            cv2.putText(frame, f'FPS: {int(fps)}', (25,30), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)   
            cv2.imshow('YOLOv5 Detection', frame)   
            if cv2.waitKey(5) & 0xFF == ord('e'):   
                break        

                    
        cap.release()                  
        cv2.destroyAllWindows()   


alperen = 'yolov5s.pt'
alperen = "C:/Users/pc/vs_code/Z16_Face_Detect_2/best_face_2.pt"

detector = FaceDetector(capture_index=0, model_name=alperen)     
detector()

