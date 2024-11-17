import random
import socket
import torch
import torchvision.transforms as transforms
from torchvision import datasets
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim
from PIL import Image
import pymysql
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image

class_names = ["papier", "plastik", "szklo"]
class_namess=["nie WIEM","papier", "plastik", "szklo"]
baza=["miesz","pap","pl","szkl"]



device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class EnhancedCNN(nn.Module):
    def __init__(self):
        super(EnhancedCNN, self).__init__()
        self.model = models.resnet18(pretrained=True)
        num_features = self.model.fc.in_features
        self.model.fc = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(num_features, len(class_names))
        )

    def forward(self, x):
        return self.model(x)

model = EnhancedCNN().to(device)
checkpoint = torch.load("model.pth", map_location=device)
model.load_state_dict(checkpoint["model_state_dict"])
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image)
    image = image.unsqueeze(0)
    return image

def predict_image(model, image_path):
    try:
        image = preprocess_image(image_path).to(device)
        with torch.no_grad():
            outputs = model(image)
            _, predicted = torch.max(outputs, 1)
            predicted_class = class_names[predicted.item()]
        return predicted_class
    except:
        return "nie WIEM"




server_ip = '192.168.0.63'
server_port = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server_ip, server_port))
    s.listen()
    print("SLUCHAM")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"POLACZNENIE Z  {addr}")
            id_data = conn.recv(4)
            device_id = int.from_bytes(id_data, 'little')

            index = int.from_bytes(conn.recv(4), "little")
            image_data = conn.recv(1000000)

            from io import BytesIO

            image_stream = BytesIO(image_data)
            predicted_class = predict_image(model, image_stream)

            liczba=str(class_namess.index(predicted_class))
            conn.sendall(liczba.encode())
            try:
                conn = pymysql.connect(
                    host="127.0.0.1",
                    user="TOMASZ",
                    password="root",
                    database="kosz",
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print("Połączono z bazą danych MySQL")
                with conn.cursor() as cursor:
                    sql="SELECT "+baza[int(liczba)]+"1"+" from uzy WHERE id = %s"
                    cursor.execute(sql, (device_id))
                    zmienna=cursor.fetchone()
                    liczba2=int(zmienna[str(baza[int(liczba)]+"1")])

                    sql = "UPDATE uzy SET "+baza[int(liczba)]+"1"+"= %s WHERE id = %s"
                    cursor.execute(sql, (liczba2+1, device_id))
                    conn.commit()
                    conn.close()

            except pymysql.MySQLError as e:
                print(f"Nie udało się połączyć z bazą danych: {e}")

            print(f"Predicted class for the image: {predicted_class}")
