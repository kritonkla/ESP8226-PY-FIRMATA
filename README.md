# ESP8226-PY-FIRMATA
## PREREQUISITE
### 1. ESP8266 board (preferably nodeMCU)
### 2.Customized Firmata firmware
The StandardFirmata.ino given in the arduino IDE doesn't actually work with ESP8266, despite it successfully compiled.  
The problem is with the pin layout config in the original firmware, which doesn't match the actual pin on the board.
### 3. pyfirmata package  
You can install it using ```pip install pyfirmata``` once installed, you need to edit  ```pyfirmata.py```<br>  find the line ```len_args = len(inspect.getargspec(func)[0]) ``` and change it into  ```len_args = len(inspect.getfullargspec(func)[0]) ```  
This is because pyfirmata is based on Python 2.7, 3.3 and 3.4. and ```getargspec()``` is already removed in Python 3.11.
### 4. other python packages
only if you are going to do the project using the provided codes:  
```pip install cv2``` ```pip install mediapipe``` ```pip install cvzone```
