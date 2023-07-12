from pathlib import Path
from PIL import Image
from google.cloud import vision
import os
import environ


class CharacterRecognition:
    def __init__(self):
        self.env = environ.Env()
        self.env.read_env('../.env')
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.env('CHARA_KEY')
        
    def imageSave(self, image):
        self.img = Image.open(image)
        self.img.save('material/images/image.jpg')
        self.image = '../material/images/image.jpg'
        
    def imageOpen(self):
        p = Path(__file__).parent / self.image
        with p.open('rb') as image_file:
            self.content = image_file.read()
        
    def startRecognition(self):
        self.client = vision.ImageAnnotatorClient()
        try:
            image = vision.Image(content=self.content)
            response = self.client.text_detection(image=image)
            texts = response.text_annotations[0].description
            self.texts = texts.splitlines()
            os.remove('material/images/image.jpg')
        except:
            return True
        
class CreateAPI:
    def __init__(self):
        self.CharacterRecognition = CharacterRecognition()
        self.appendcount = 0
        self.result = {}
        
    def infoExtraction(self):
        for text in self.CharacterRecognition.texts:
            if '氏名'in text:
                self.result['name'] = text[text.find('氏名')+3:]
                self.appendcount += 1
            elif '住所' in text:
                self.result['address'] = text[text.find('住所')+3:]
                self.appendcount += 1
            elif '日生' in text:
                self.result['birthday'] = text[:text.find('生')]
                self.appendcount += 1
        
        if len(self.result) != 3:
            return True
        
    def makeJSON(self, data):
        if data == None:
            return {"error": "データが不正です。", "reason": "文字が見つかりませんでした"}
        elif data == "count":
            return {"error": "データが不正です。", "reason": "指定された文字が見つかりませんでした"}
        else:
            return {"error": "データが不正です。", "reason": "例外が発生しました"}
        
    def main(self, image):
        self.CharacterRecognition.imageSave(image)
        self.CharacterRecognition.imageOpen()
        if self.CharacterRecognition.startRecognition(): return self.makeJSON(None)
        if self.infoExtraction(): return self.makeJSON("count")
        print(self.result)
        
        return self.result