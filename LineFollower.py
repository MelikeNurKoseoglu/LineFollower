import cv2
import numpy as np
import RPi.GPIO as GPIO

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

GPIO.setmode(GPIO.BOARD)

Ena1=12
Ena2=32
IN1=7
IN2=11
IN3=13
IN4=15

GPIO.setup(Ena1, GPIO.OUT)
GPIO.setup(Ena2, GPIO.OUT)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

pwm1 = GPIO.PWM(Ena1, 100)
pwm2 = GPIO.PWM(Ena2, 100)

pwm1.start(50)
pwm2.start(50)

while True:
    
    ret, frame = cap.read()
    
    frame=cv2.flip(frame,1)
    
    lower_black = np.uint8([70,70,70])
    
    upper_black = np.uint8([0,0,0])
    
    mask = cv2.inRange(frame, upper_black, lower_black)
    
    contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0 :

        c = max(contours, key=cv2.contourArea)
        
        M = cv2.moments(c)
            
        cx = int(M['m10']/M['m00'])
        
        cy = int(M['m01']/M['m00'])
        
        cv2.drawContours(frame, c, -1, (0,255,0), 1)
        
        print("CX : "+str(cx)+"  CY : "+str(cy))
            
        if cx >= 480 :
            print("Sağa git")
            
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)
            GPIO.output(IN3, GPIO.HIGH)
            GPIO.output(IN4, GPIO.LOW)
            
            
        if cx < 480 and cx > 160 :
            print("düz git")
            
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
            GPIO.output(IN3, GPIO.HIGH)
            GPIO.output(IN4, GPIO.LOW)
            

        if cx <=160 :
            print("sola git")
            
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.HIGH)
            
            
        cv2.circle(frame, (cx,cy), 5, (255,255,255), -1)
        
    else :
        print("çizgi yok")
        
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        
    font=cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(frame,"Cizgi Takibi",(10,50),font,3,(0,0,200))
    
    cv2.imshow("Mask",mask)
    cv2.imshow("Frame",frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        break
        
    
    
cap.release()
cv2.destroyAllWindows()
