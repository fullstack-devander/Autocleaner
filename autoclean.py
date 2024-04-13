import os
import configparser

conf = configparser.ConfigParser()
conf.read('autoclean.ini')

paths = conf['DEFAULT']['paths'].split('\n')

for path in paths:
    print(path)
    
    if os.path.exists(path):
        content = [item for item in os.listdir(path)]
        
        for item in content:
            removeItem = path + item
            
            if os.path.isfile(removeItem):
                os.remove(removeItem)
            
            if os.path.isdir(removeItem):
                os.rmdir(removeItem)
    else:
        print("Path {} doesn't exists", path)