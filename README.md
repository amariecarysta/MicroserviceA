# Communication Contract
Microservice A processes requests via text files in the working directory. It watches for a file named request.txt and, whenever it detects a new or updated file, it:

Reads the file contents (plain UTF-8 text)

Counts the number of words (splitting on whitespace)

Writes the result as a decimal integer into response.txt

# Requesting Data

Your code must create or overwrite request.txt in the same directory where the service is running. The file’s contents should be exactly the text to be counted (UTF‑8 encoded), for example:

Python example
text_to_count = "Whatever words you choose to type.."


with open("request.txt", "w", encoding="utf-8") as req:
    
    req.write(text_to_count)
    
# Receiving Data
After writing request.txt, watch for response.txt to be created or updated, then read the contents to get the word count:

Python example


import os, time

while not os.path.exists("response.txt"):


    time.sleep(0.1)

with open("response.txt", "r", encoding="utf-8") as res:


    count = int(res.read().strip())


print("Word count =", count)


# UML

<img width="979" height="637" alt="Screenshot 2025-08-04 at 17 51 23" src="https://github.com/user-attachments/assets/8923950d-9f14-41b2-90b8-976c218fe056" />
