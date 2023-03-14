from django.http import JsonResponse
from django.shortcuts import render
from .models import Image
from django.http import HttpResponse
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from backend_logic import face_features_extraction
from .forms import StudentForm
from .JsonParsing import add_student_to_json, get_details

def getRoutes(request):
        # if request.method == 'POST':
        #     form = ImageUploadForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect('index')
        # else:
        #     form = ImageUploadForm()
        # print(request)
        routes =  {
            'student_recogonizer' : 'welcome'
        }
        
        return JsonResponse(routes, safe=False)

def showImages(request):
    form = StudentForm
    context = {
        'form' : form
    }
    return render(request,"display.html", context)

def registerStudent(request):
    # if request.method == 'GET':
    data = StudentForm()
    context = {
        'form' : data
    }
    if request.method == 'POST':
        print( "regno : " + request.POST["regno"])
        print("name : " + request.POST["name"])
        print("section : "  + request.POST["sec"])
        print("course : " + request.POST["course"])
        print("dob : " + request.POST["dob"])
        print("block : " + request.POST["block"])
        print("emailid : " + request.POST["emailid"])
        print("mobile number :" + request.POST["Mobile Number"])
        print("Father Name : " + request.POST["fathername"])
        print("Mother Name : " + request.POST["mothername"])
        print("Parents Contact : " + request.POST["parents contact"])
        print("Co-ordinator : " + request.POST["Co-ordinator"])
        print("Boarding Point : " + request.POST["Boarding Point"])
        print("Sex : " + request.POST["sex"])
        print("state : " + request.POST["state"])
        print("District : " + request.POST["District"])
        print("Academic Year : " + request.POST["year"])
        # print("Image Upload : " + request.POST["District"])

        regno = request.POST["regno"]
        name = request.POST["name"]
        section = request.POST["sec"]
        course = request.POST["course"]
        dob = request.POST["dob"]
        block = request.POST["block"]
        emailid = request.POST["emailid"]
        mobilenumber = request.POST["Mobile Number"]
        fatherName = request.POST["fathername"]
        motherName = request.POST["mothername"]
        parents_number = request.POST["parents contact"]
        co_ordinator = request.POST["Co-ordinator"]
        boardingPoint = request.POST["Boarding Point"]
        Sex = request.POST["sex"]
        state = request.POST["state"]
        district = request.POST["District"]
        academicYear = request.POST["year"]
        add_student_to_json(
            name=name,
            regno=regno,
            dob=dob,
            email=emailid,
            course=course,
            co_ordinator=co_ordinator,
            block=block,
            father_name=fatherName,
            mother_name=motherName,
            mobile_num=mobilenumber,
            parents_number= parents_number,
            sec=section,
            academicYear=academicYear,
            b_point=boardingPoint,
        )
        files = request.FILES.getlist('files')
        for image in files:
            path_to_save = f"E:\Projects\hackathon\student_recognizer\student_recognizer_backend\\backend_logic\student_Images\{regno}"
            if not (os.path.isdir(path_to_save)):
                os.mkdir(path_to_save)
            file_path = os.path.join(path_to_save, image.name)
            with open(file_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
    return render(request,"register_student.html    ", context)

# def registerStudent(request):
#     # if request.method == 'GET':
#     data = StudentForm()
#     context = {
#         'form' : data
#     }
#     if request.method == 'POST':
#         form = StudentForm(request.POST or None)
#         if form.is_valid():
#             name= form.cleaned_data.get("name")
#             regno= form.cleaned_data.get("regno")
#             print(name)
#             print(regno)
#             image = request.FILES['image']
#             path_to_save = f"E:\Projects\hackathon\student_recognizer\student_recognizer_backend\\backend_logic\student_Images\{regno}"
#             if not (os.path.isdir(path_to_save)):
#                 os.mkdir(path_to_save)
#             file_path = os.path.join(path_to_save, image.name)
#             with open(file_path, 'wb+') as destination:
#                 for chunk in image.chunks():
#                     destination.write(chunk)
#     return render(request,"register.html", context)

   
    

def get_student_details(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        print("file recieved")
        # Process the uploaded file here
        path = default_storage.save('tmp/test.jpg', ContentFile(uploaded_file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        faceDetection = face_features_extraction.FaceFeatureExtraction()
        face_regno = faceDetection.detectFace(tmp_file)
        print(f"register no is {face_regno}")

        return JsonResponse([{"details" : get_details(face_regno)}],safe=False)
    else:
        print("file not recieved")
        return HttpResponse('Invalid request method')
    

