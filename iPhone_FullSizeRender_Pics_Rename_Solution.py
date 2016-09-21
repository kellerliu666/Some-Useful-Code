'''We took a lot of pictures by iPhone every day, and get used to backup our photo library from iPhone to hardrive regularly.
I personally like to edit photos by using Apple original photo editor (crop or color adjust), but this would generate a 
bunch of renamed files like FullSizeRender001.jpg. This causes duplicated file name problem when I do backup, so I write a 
Python to generate some random name for them instead of FullSizeRenderxxx.jpg.'''
import os
import random
for file in os.listdir('.'):
    rand_num = random.randint(1000000000, 9999999999)
    if file.startswith('F'):
        os.rename(file, 'Apple'+str(rand_num)+'.jpg')
        
