import os


for root, subs, files in os.walk('.'):
    for name in files:
        # if name.startswith('call'):
        print(root, name)





