# OpenCV のインポート
import cv2
from pyzbar.pyzbar import decode
from Get_title import *

# VideoCaptureのインスタンスを作成する。
# 引数でカメラを選べれる。
cap = cv2.VideoCapture(0)
i=0
while i<100:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    # スクリーンショットを撮りたい関係で1/4サイズに縮小
    #frame = cv2.resize(frame, (int(frame.shape[1]/4), int(frame.shape[0]/4)))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 加工なし画像を表示する
    #cv2.imshow('Raw Frame', frame)

    # 何か処理（ここでは文字列「hogehoge」を表示する）
    edframe = frame
    #cv2.putText(edframe, 'Test', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv2.LINE_AA)

    # 加工済の画像を表示する
    #cv2.imshow('Edited Frame', edframe)
    try:
        #qr = cv2.QRCodeDetector()
        #data, points, straight_qrcode = qr.detectAndDecode(edframe)
        #print('データ:', data)
        data = decode(edframe)
        num=data[0][0].decode('utf-8', 'ignore')
        if '978' in num:
            print(num)
            title=Get_title(num)
            print(title)
            break
        else:
            pass
    except:
        pass
    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break
    i+=1
# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()
