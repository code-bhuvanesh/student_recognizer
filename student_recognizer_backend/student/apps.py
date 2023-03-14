from django.apps import AppConfig
from backend_logic.face_features_extraction import FaceFeatureExtraction



class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'
    # fr = FaceFeatureExtraction()
    # fr.detectFace("backend_logic\images\IMG20230308071333.jpg")
    # fr.initilize()
  
