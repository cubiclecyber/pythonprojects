from math import dist
from turtle import distance
import pyautogui
distance = 300
while distance > 0:
    pyautogui.drag(distance, 0,  duration=0.5) 
    distance -= 20
    pyautogui.drag(0, distance, duration=0.5)
    pyautogui.drag(-distance, 0, duration=0.5)
    distance -= 10