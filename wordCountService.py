import os
import time

REQ = 'request.txt'
RES = 'response.txt'

print(f'Watching for requests in {REQ}…')

last_request = None

def count_words(text: str) -> int:
    return len(text.strip().split())

while True:
    if os.path.exists(REQ):
        with open(REQ, 'r', encoding='utf-8') as f:
            text = f.read()
        # Only re‐do if the contents have changed
        if text != last_request:
            print('Got request:', repr(text))
            cnt = count_words(text)
            with open(RES, 'w', encoding='utf-8') as f:
                f.write(str(cnt))
            print('Word Count:', cnt)
            last_request = text
    time.sleep(3.00)