import cv2

cap = cv2.VideoCapture(0)
#vis = visdom.Visdom(server='http://visdom')

while(cap.isOpened()):
  ret, frame = cap.read()
  cv2.imshow('frame', frame)

  # if ret == True:
  #     vis_f[0,:,:] = cv_f[:,:,2]
  #     vis_f[1,:,:] = cv_f[:,:,1]
  #     vis_f[2,:,:] = cv_f[:,:,0]
  #
  #     vis.image(vis_f, win='Video')

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
