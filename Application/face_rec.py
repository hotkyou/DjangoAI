from facenet_pytorch import MTCNN
from PIL import Image, ImageDraw
from facenet_pytorch import MTCNN, InceptionResnetV1
import numpy as np

def FaceRec(image, picture):
    # 顔検出のAI
    # image_size: 顔を検出して切り取るサイズ
    # margin: 顔まわりの余白
    mtcnn = MTCNN(image_size=160, margin=10)

    # 切り取った顔を512個の数字にするAI
    # 学習済みのモデルをダウンロード
    resnet = InceptionResnetV1(pretrained='vggface2').eval()

    image_path1 = image
    image_path2 = picture

    # 画像データ取得
    img1 = Image.open(image_path1) 
    try:
        img_cropped1 = mtcnn(img1)
        img_embedding1 = resnet(img_cropped1.unsqueeze(0))
    except:
        return None
    img2 = Image.open(image_path2) 
    try:
        img_cropped2 = mtcnn(img2)
        img_embedding2 = resnet(img_cropped2.unsqueeze(0))
    except:
        return ""

    # 類似度の関数
    def cos_similarity(p1, p2): 
        return np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))

    # 512個の数字にしたものはpytorchのtensorという型なので、numpyの方に変換
    p1 = img_embedding1.squeeze().to('cpu').detach().numpy().copy()
    p2 = img_embedding2.squeeze().to('cpu').detach().numpy().copy()

    # 類似度を計算して顔認証
    img1vs2 = cos_similarity(p1, p2)
    
    print("1つ目と2つ目の比較", str(img1vs2))
    img1vs2 = str(img1vs2)
    return img1vs2
