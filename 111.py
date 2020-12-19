import numpy as np
import cv2

point_loc = []
count = 0

def mouse_click(event, x, y, flags, param):
    global point_loc, count, img_basic

    if event == cv2.EVENT_LBUTTONDOWN:
        print("(%d, %d)" % (x, y))
        point_loc.append((x, y))
        print(point_loc)
        cv2.circle(img_basic, (x, y), 3, (0, 0, 255), -1) #클릭 시 빨간 점이 찍힘


cv2.namedWindow('basic')
cv2.setMouseCallback('basic', mouse_click)
img_original = cv2.imread('test.jpg')
img_basic = cv2.resize(img_original,dsize=(480,640),interpolation=cv2.INTER_LINEAR)

while(True):
    cv2.imshow("basic", img_basic)
    if cv2.waitKey(1)&0xFF == 32: # 스페이스바
        break


# 좌표 찍는 순서 : 좌상단, 우상단, 좌하단, 우하단
pts1 = np.float32([list(point_loc[0]),list(point_loc[1]),list(point_loc[2]),list(point_loc[3])])
pts2 = np.float32([[0,0],[480,0],[0,640],[480,640]]) # 기본 세팅 : 480 * 640, 3:4비율

print(pts1)
print(pts2)

M = cv2.getPerspectiveTransform(pts1,pts2)
img_result = cv2.warpPerspective(img_basic, M, (480,640))

cv2.imshow("result", img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
