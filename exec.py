#Criado por Allef Anderson
#Email: allef.anderson@hotmail.com
#Instagram allef.anderson.7    -   Segue la!

from PIL import Image
from google.cloud import vision
from sinesp_client import SinespClient
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def detect_text(path):
   
    client = vision.ImageAnnotatorClient()
    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    try:
        conv = texts[0].description
        if(conv[3] == '-' or conv[3] == ' '):
            conv =conv.replace(conv[3],"")
        if(conv[7] == "\n"):
            conv =conv.replace(conv[7],"")
        print(conv)
        aux = str(conv)
        sinesp(aux)
    except:
        print("Placa nao encontrada")

def resize(image):
    # open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
    imageFile = image
    im1 = Image.open(imageFile)
    # adjust width and height to your needs
    width = 500
    height = 300
    # use one of these filter options to resize the image
    im3 = im1.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
    ext = ".jpg"
    im3.save("BILINEAR" + ext)
    detect_text("BILINEAR.jpg")

def sinesp(placa):
    sc = SinespClient()
    result = sc.search(placa)
    print(result['model'] + "\n" + result['color'] + "\n" + result['year'] + "\n" + result['return_message']+ "\n" 
        + result['status_message'] + "\n" + result['chassis'])

while (True):
    aux = input("Imagem: ")
    try:
    	resize(aux)
    except:
        print("Placa nao identificada")
