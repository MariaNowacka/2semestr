# wygeneruje i odczyta kody QR (wskazówka: qrcode i OpenCV
#!pip install qrcode
import qrcode
def generowanie(a):
  """funkcja generująca kod qr o podanej treści
  input : a - treść, którą chcemy opakować wkod qr"""
  img = qrcode.make(a)
  img.save("D:\l3\kod_qr")

generowanie(r"https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#!pip install cv2
import cv2
def dekodowanie(a):
  """funkcja sczytująca informacje z kodu qr
  input : a - scieżka do pliku (zdjęcia) z kodem qr"""
  image = cv2.imread(a)
  detector = cv2.QRCodeDetector()
  data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
  if vertices_array is not None:
    print(data)
  else:
    print("error")


dekodowanie("D:\l3\kod_qr")
