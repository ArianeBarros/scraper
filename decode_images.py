import json
import base64

def main():
    f = open("marcas.json", "r")
    jsonstring = f.read()
    dic = json.loads(jsonstring)
    cont = 0
    for x in dic:
        content = base64.b64decode(x['url'].split(',')[-1])
        with open('image'+str(cont)+'.png','wb') as f:
            f.write(content)
        cont += 1
main()