import cv2
import visdom
import numpy as np

cap = cv2.VideoCapture(0)

# 設定擷取影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

img_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
img_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

vis = visdom.Visdom(server='http://visdom')

vis_f = np.zeros((3,img_h,img_w))

while(cap.isOpened()):

    ret, cv_f = cap.read()

    if ret == True:
        vis_f[0,:,:] = cv_f[:,:,2]
        vis_f[1,:,:] = cv_f[:,:,1]
        vis_f[2,:,:] = cv_f[:,:,0]

        vis.image(vis_f, win='Video')

    else:
        break


# 釋放所有資源
cap.release()
cv2.destroyAllWindows()



# 以迴圈從影片檔案讀取影格，並顯示出來
# while(cap.isOpened()):
#   ret, frame = cap.read()
#
#   cv2.imshow('frame',frame)
#   h,w,c = frame.shape
#   cv_f = frame.reshape(c,h,w)
#   vis.image(cv_f, win='Video')
#
#
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break
# cap.release()
# cv2.destroyAllWindows()
