import numpy as np
import cv2
import time
import os

# Đầu tiên tạo thư mục data cùng cấp với file make_data
# Label: Tên mỗi người, đổi tên theo tên mỗi người
label = "MinhDuong"

cap = cv2.VideoCapture(0)

# Biến đếm, để chỉ lưu dữ liệu sau khoảng 60 frame vì lúc đầu cần chuẩn bị 
i=0
while(True):
    # Capture frame-by-frame
    i+=1
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, dsize=None,fx=0.3,fy=0.3)

    # Hiển thị
    cv2.imshow('frame',frame)

    # Lưu dữ liệu
    # Chỉ lấy ảnh sau mỗi 3 frame
    if i>60 and i<=1060 and i%3==0:
        print("Số ảnh capture = ",i-60)

        cv2.imwrite('data/' + str(label) + "/" + str(i-60) + ".png",frame)

    if(i == 1070): print('\n---Bấm Q để thoát!---')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Khi xong thì giải phóng camera
cap.release()
cv2.destroyAllWindows()
