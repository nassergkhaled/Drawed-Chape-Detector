import cv2

def recognizeShapes():
    img = cv2.imread("inputImg.jpg")
    if img is None:
        print('no image')
    else:
        imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _,thrash = cv2.threshold(imgGrey, 235, 255, cv2.THRESH_BINARY)
        contours,_ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.011 * cv2.arcLength(contour, True), True)
            area = cv2.contourArea(contour)
            if ((len(approx) > 8) and (len(approx) < 23) and (area > 30)):
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)
                cv2.circle(img, center, radius, (0, 0, 255), -1)
            elif len(approx) == 3:
                cv2.drawContours(img, [contour] , 0, (0, 0 , 255), -1)
            elif len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                if x!=0 and y!=0:
                    img = cv2.rectangle(img , (x, y) , (x + w, y + h) , (0,0,255) , -1)

            image=img
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            _, thresh = cv2.threshold(gray, 235, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            output = cv2.imread("inputImg.jpg")
            for contour in contours:
                font = cv2.FONT_HERSHEY_COMPLEX
                ShapeN = "unidentified"
                epsilon = 0.01 * cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)
                cv2.drawContours(thresh, [approx], -1, (0, 0, 255), 2)
                x = approx.ravel()[0] - 25
                y = approx.ravel()[1] - 5

                epsilon2 = 0.04 * cv2.arcLength(contour, True)
                approx2 = cv2.approxPolyDP(contour, epsilon2, True)
                cv2.drawContours(thresh, [approx2], -1, (0, 0, 255), 2)
                x2 = approx.ravel()[0] - 25
                y2 = approx.ravel()[1] - 5
                if len(approx2) == 3:
                    ShapeN = "Triangle"
                    cv2.rectangle(output,(x,y),(x+w+25,y-h+15),(255,150,150),-1)
                    cv2.putText(output, ShapeN, (x2, y2), font, 0.5, (0, 0, 0))
                elif len(approx) == 4:
                    ShapeN = "Rectangle"
                    cv2.rectangle(output,(x,y),(x+w+35,y-h+15),(255,255,0),-1)
                    cv2.putText(output, ShapeN, (x, y), font, 0.5, (0, 0, 0))
                elif len(approx) == 15:
                    ShapeN = "Car Class 3"
                    cv2.rectangle(output,(x,y),(x+w+60,y-h+15),(255,0,255),-1)
                    cv2.putText(output, ShapeN, (x, y), font, 0.5, (0, 0, 0))
                elif len(approx) == 21:
                    ShapeN = "Car Class 2"
                    cv2.rectangle(output,(x,y),(x+w+60,y-h+15),(0,255,255),-1)
                    cv2.putText(output, ShapeN, (x, y), font, 0.5, (0, 0, 0))
                elif (len(approx)!=15) and (len(approx)!=16) and (len(approx)!=21) and (len(approx)!=3) and (len(approx)!=4):
                    ShapeN = "Circle"
                    cv2.rectangle(output,(x,y),(x+w,y-h+15),(0,255,0),-1)
                    cv2.putText(output, ShapeN, (x, y), font, 0.5, (0, 0, 0))

        cv2.imwrite("output.jpg", output)

def recognizeClassOne():
    img = cv2.imread("inputImg.jpg")
    if img is None:
        print('no image')
    else:
        imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _,thrash = cv2.threshold(imgGrey, 235, 255, cv2.THRESH_BINARY)
        contours,_ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.011 * cv2.arcLength(contour, True), True)
            area = cv2.contourArea(contour)
            if ((len(approx) > 8) and (len(approx) < 23) and (area > 30)):
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)
                cv2.circle(img, center, radius, (0, 0, 255), -1)
            elif len(approx) == 3:
                cv2.drawContours(img, [contour] , 0, (0, 0 , 255), -1)
            elif len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                if x!=0 and y!=0:
                    img = cv2.rectangle(img , (x, y) , (x + w, y + h) , (0,0,255) , -1)

        image=img
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, 235, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        output2 = cv2.imread("output.jpg")
        for contour in contours:
            font = cv2.FONT_HERSHEY_COMPLEX
            ShapeN = "unidentified"
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            cv2.drawContours(thresh, [approx], -1, (0, 0, 255), 2)
            x = approx.ravel()[0] - 25
            y = approx.ravel()[1] - 5
            if len(approx) == 16:
                ShapeN = "Car Class 1"
                cv2.rectangle(output2,(x,y-67),(x+w+60,y-h-60),(0,0,255),-1)
                cv2.putText(output2, ShapeN, (x+10, y-75), font, 0.5, (0, 0, 0))
                cv2.imwrite("output.jpg", output2)

output=recognizeShapes()
recognizeClassOne()

img = cv2.imread("inputImg.jpg")
cv2.imshow("input", img)

final = cv2.imread("output.jpg")
cv2.imshow("output", final)
cv2.waitKey(0)
cv2.destroyAllWindows()