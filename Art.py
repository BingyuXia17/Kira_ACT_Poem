import time, os, random

os.system('clear')

count = 0
while True:
   b = True if random.uniform(0,1) < .5 else False
   if b:
    print ("Art is eternal.")
    count = count + 1

   if not b:
    print ("Art it ephemeral.")
    time.sleep(0.5)
    os.system('clear')
    for c in range(count):
        print ("Art is eternal.")
   time.sleep(1)

   if count == 22:
   	os.system('clear')
   	count = 0
