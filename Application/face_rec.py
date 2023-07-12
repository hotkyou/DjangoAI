from facenet_pytorch import MTCNN
from PIL import Image, ImageDraw
from facenet_pytorch import MTCNN, InceptionResnetV1
import numpy as np

#画像クロップ
def ImgCrop(imagepicture):
    
    # 顔検出のAI
    # image_size: 顔を検出して切り取るサイズ margin: 顔まわりの余白
    mtcnn = MTCNN(image_size=160, margin=10)
    
    # 切り取った顔を512個の数字にする学習済みのAIモデルをダウンロード
    resnet = InceptionResnetV1(pretrained='vggface2').eval()
    img = Image.open(imagepicture)
    
    try:
        img_embedding = resnet(mtcnn(img).unsqueeze(0))
    except:
        return None
    
    return img_embedding

# 類似度の関数
def cos_similarity(p1, p2): 
    return np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))

def createAPI(data):
    if data == "img1":
        return {"error": "データが不正です。", "reason": "身分証明書の顔に影がかかっているか、見切れているため認識できませんでした。"}
    elif data == "img2":
        return {"error": "データが不正です。", "reason": "現在の顔の画像に影がかかっているか、見切れているため認識できませんでした。"}
    else:
        return {"correct": "データが正常です。", "reason": data}
        
def FaceRec(image, picture):
    
    img1 = ImgCrop(image)
    img2 = ImgCrop(picture)
    
    if img1 == None:
        return createAPI("img1")
    if img2 == None:
        return createAPI("img2")

    # 512個の数字にしたものはpytorchのtensorという型なので、numpyの方に変換
    p1 = img1.squeeze().to('cpu').detach().numpy().copy()
    p2 = img2.squeeze().to('cpu').detach().numpy().copy()

    # 類似度を計算して顔認証
    img1vs2 = str(cos_similarity(p1, p2))
    print("1つ目と2つ目の比較", img1vs2)
    
    return createAPI(img1vs2)
