import cv2
import sys
import numpy as np
imagem_cinza = cv2.imread(sys.argv[1], 0)
equ = cv2.equalizeHist(imagem_cinza)
res = np.hstack((imagem_cinza, equ))  # stacking images side-by-side
cv2.imshow('res', equ)
cv2.imwrite('res.png', equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
