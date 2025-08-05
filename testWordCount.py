import os
import time

REQ = 'request.txt'
RES = 'response.txt'



sample_text = 'No matter what..'
print('Writing request:', sample_text)
with open(REQ, 'w', encoding='utf-8') as f:
    f.write(sample_text)

time.sleep(3.0)

if os.path.exists(RES):
    with open(RES, 'r', encoding='utf-8') as f:
        print('Got response:', f.read().strip())
else:
    print('No response.txt found yet.')