import codecs
from click import File
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import json
# from PIL import ImageGrab


class FaceFeatureExtraction():
    np.random.seed(42)
    def __init__(self):
        
        pass
    # def initilize(self):
    #     self.path = 'E:\Projects\hackathon\student_recognizer\student_recognizer_backend\\backend_logic\student_Images'
    #     student_face_extraction = {}
    #     listdir = os.listdir(self.path)
    #     total_len = len(listdir)
    #     c = 1
    #     for student in listdir:
    #         face_extraction_list = []
    #         for cl in os.listdir(f"{self.path}\{student}"):
    #             # print(f'{self.path}\{cl}')
    #             curImg = cv2.imread(f'{self.path}\{student}\{cl}')
    #             img = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)
    #             tmp = face_recognition.face_encodings(img)
    #             if(len(tmp) == 0):
    #                 continue
    #             encode = tmp[0]
    #             face_extraction_list.append(encode.tolist())
    #         student_face_extraction[student] = face_extraction_list
    #         print(f"completed : {c}/{total_len}")
    #         c += 1
    #     with open("E:\Projects\hackathon\student_recognizer\student_recognizer_backend\\backend_logic\\features\\face_features.json", "w") as outfile:
    #         json.dump(student_face_extraction, outfile, indent=4, sort_keys=True)
    def initilize(self, listdir):
        self.path = 'E:\Projects\hackathon\student_recognizer\student_recognizer_backend\\backend_logic\student_Images'
        student_face_extraction = {}
        total_len = len(listdir)
        c = 1
        for student in listdir:
            face_extraction_list = []
            for cl in os.listdir(f"{self.path}\{student}"):
                # print(f'{self.path}\{cl}')
                curImg = cv2.imread(f'{self.path}\{student}\{cl}')
                img = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)
                tmp = face_recognition.face_encodings(img)
                if(len(tmp) == 0):
                    continue
                encode = tmp[0]
                face_extraction_list.append(encode.tolist())
            student_face_extraction[student] = face_extraction_list
            print(f"completed : {c}/{total_len}")
            c += 1
        with open("E:\Projects\hackathon\student_recognizer\student_recognizer_backend\\backend_logic\\features\\face_features.json", "r+") as outfile:
            # json.dump(student_face_extraction, outfile, indent=4, sort_keys=True)
            data = {}
            try:
                data = json.load(outfile)
            except:
                print()
            data.update(student_face_extraction)
            outfile.seek(0)
            json.dump(data, outfile, indent=4)

        

   

    def detectFace(self,tempPath : str) -> str:
        if(os.path.isfile('E:\Projects\hackathon\student_recognizer\student_recognizer_backend\\backend_logic\\features\\face_features.json') == False):
            self.initilize()
        detected_face = None
        with open('E:\Projects\hackathon\student_recognizer\student_recognizer_backend\\backend_logic\\features\\face_features.json') as json_file:
            try:    
                data = json.load(json_file)
                img = cv2.imread(tempPath)
                img = cv2.resize(img,(0,0),None,0.25,0.25)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
                facesCurFrame = face_recognition.face_locations(img)
                encodesCurFrame = face_recognition.face_encodings(img,facesCurFrame)
                list_detected = []
                list_detected_names = []
                for studentName in data:
                    if(len(data[studentName]) == 0):
                        continue
                    for encodeFace in encodesCurFrame:
                        matches = face_recognition.compare_faces(np.asarray(data[studentName]),encodeFace)
                        faceDis = face_recognition.face_distance((data[studentName]),encodeFace)
                        matchIndex = np.argmin(faceDis)
                        if matches[matchIndex]:
                            for i in data[studentName]:
                                list_detected.append(i)
                                list_detected_names.append(studentName)
                for encodeFace in encodesCurFrame:
                    matches1 = face_recognition.compare_faces(np.asarray(list_detected),encodeFace)
                    faceDis1 = face_recognition.face_distance(list_detected,encodeFace)
                    matchIndex1 = np.argmin(faceDis1)
                    # print(len(list_detected))
                    # print(len(list_detected_names))
                    # print(len(matches1))
                    # print(len(faceDis1))
                    # print(matchIndex1)
                    

                    if matches1[matchIndex1]:
                        detected_face = list_detected_names[matchIndex1]
            except:
                print()
        return detected_face
        
    
# # if __name__ == "__main__":
# fr = FaceFeatureExtraction()
# fr.initilize()
# print("completed init")
# print(fr.detectFace("..\media\\tmp\\test_9CS5zJG.jpg"))
# print(fr.detectFace("E:\Projects\hackathon\sarathipics.png"))
# print(fr.detectFace("E:\Projects\hackathon\\test_app\\backend_logic\student_Images\\bhuvanesh\\bhuvanesh.jpg"))

def binary_search(arr, x):
    l = 0
    r = len(arr)
    while (l <= r):
        m = l + ((r - l) // 2)
 
        res = (x == arr[m])
 
        # Check if x is present at mid
        if (res == 0):
            return m - 1
 
        # If x greater, ignore left half
        if (res > 0):
            l = m + 1
 
        # If x is smaller, ignore right half
        else:
            r = m - 1
 
    return -1

def read_all():
    with open("E:\Projects\hackathon\student_recognizer\student_recognizer_backend\\backend_logic\\features\\face_features.json","r" ) as json_file:
        Details = {}
        try:
            Details = json.load(json_file)
        except:
            print()
    return Details

all_path = 'E:\Projects\hackathon\student_recognizer\student_recognizer_backend\\backend_logic\student_Images'
all_students = os.listdir(all_path)
extraced_features_students = list(read_all().keys())
all_students.sort()
extraced_features_students.sort()

to_be_extracted_students = []
print(all_students)
print(extraced_features_students)

print(len(all_students))
print(len(extraced_features_students))
if len(all_students) != len(extraced_features_students):
    for s in all_students:
        if s not in extraced_features_students:
            to_be_extracted_students.append(s)

FaceFeatureExtraction().initilize(to_be_extracted_students)

