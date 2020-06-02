import cv2

def detect_figure(font, thresh):
    contours, h = cv2.findContours(thresh, 1, 2)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        print("На изображении обнаружена фигура: ")
        if len(approx) == 3:
            print("треугольник")
            cv2.drawContours(img, [cnt], 0, (0, 255, 0), -1)
            cv2.putText(img, 'треугольник', (950, 190), font, 1, color=(120, 120, 255), thickness=2)
        elif len(approx) == 4:
            print("квадрат")
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
            cv2.putText(img, 'квадрат', (850, 190), font, 1, color=(255, 130, 130), thickness=2)
        elif len(approx) == 9:
            print("полукруг")
            cv2.drawContours(img, [cnt], 0, (255, 255, 0), -1)
            cv2.putText(img, 'полукруг', (750, 190), font, 1, color=(140, 255, 140), thickness=2)
        elif len(approx) == 13:
            print("круг")
            cv2.drawContours(img, [cnt], 0, (0, 255, 255), -1)
            cv2.putText(img, 'круг', (550, 190), font, 1, color=(0, 0, 255), thickness=2)
        else:
            n = len(approx)
            print("%d-угольник" % n)
            cv2.drawContours(img, [cnt], 0, 255, -1)
            cv2.putText(img, "%d-угольник" % n, (0, 200), font, 1, color=(0, 255, 0), thickness=2)


img = cv2.imread('resources/images/figure.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
font = cv2.FONT_HERSHEY_COMPLEX
ret, thresh = cv2.threshold(gray, 127, 255, 1)
detect_figure(font, thresh)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
