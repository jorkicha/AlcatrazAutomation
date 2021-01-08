import os

import pytest

from libs.face_detect import face_detect

path = os.getcwd() + '/Tests/Resources/'


@pytest.mark.faceRecognitionTest
class FaceRecognitionTest():

    def test_0100_detection_of_four_faces(self):
        for i in range(10):
            assert face_detect(path + "/abba.png") == 4

    def test_101_detection_of_one_face(self):
        assert face_detect(path + "/oneFace.jpeg") == 1

    def test_102_detection_of_cartoon_faces(self):
        assert face_detect(path + "/cartoon.jpg") == 0

    def test_103_detection_of_objects_different_from_face(self):
        assert face_detect((path + "/cars.jpeg")) == 0

    def test_104_detection_of_animal_lenivec_face(self):
        assert face_detect(path + "/animalfaceLenivec.jpeg") == 0

    def test_105_detection_of_animal_lion_face(self):
        assert face_detect(path + "/faceanimalLion.jpg") == 0

    def test_106_detection_of_multiple_animal_faces(self):
        assert face_detect((path + "/multipleanimals.jpg")) == 0

    def test_107_detection_of_black_face_male(self):
        assert face_detect(path + "/blackfacemale.jpeg") == 1

    def test_108_detection_of_black_face_female(self):
        assert face_detect(path + "/blackfacefemale.jpg") == 1

    def test_109_detection_of_seven_black_faces(self):
        assert face_detect(path + '/blackpeople.jpg') == 7

    def test_110_detection_of_asian_male(self):
        assert face_detect((path + "/asianmale.jpg")) == 1

    def test_111_detection_of_asian_female(self):
        assert face_detect(path + "/asianfemale.jpeg") == 1

    def test_112_detection_of_six_asians(self):
        assert face_detect(path + "/asianfamily.jpeg") == 6

    def test_113_detection_of_five_people_looking_down(self):
        assert face_detect(path + '/five_people_looking_down.jpg') == 5

    def test_114_detection_of_thirteen_people_smiling(self):
        assert face_detect(path + '/thirteen_people_smileing.jpg') == 13

    def test_115_detection_of_six_people_cartoon(self):
        assert face_detect(path + '/six_people_cartoon.png') == 0

    def test_116_detection_of_four_babies(self):
        assert face_detect(path + '/four_babies.jpg') == 4

    def test_117_detection_of_thirteen_babies_in_circle(self):
        assert face_detect(path + '/thirteen_babies_in_circle.jpg') == 13

    def test_118_detection_of_five_baby_faces_in_circle_large_format(self):
        assert face_detect(path + '/five_baby_faces_in_circle.jpg') == 5

    def test_119_detection_pf_five_baby_faces_in_circle_small_format(self):
        assert face_detect(path + '/face_in_circle.jpeg') == 5

    def test_120_wrong_input(self):
        try:
            assert face_detect(2) == 0
        except:
            print('Unexpected file format')
            raise

    def test_121_different_file_format_from(self):
        try:
            assert face_detect(path + 'Prilojenie-02A-NRD-2018-MD-20-04-2018.pdf') == 0
        except:
            print('Unexpected file format')
            raise

    def test_122_corupted_png_file(self):
        try:
            assert face_detect(path + '/coruptedPNGFile.png') == 0
        except:
            print('This file is corrupted')
            raise

    def test_123_array(self):
        try:
            assert face_detect([0,2]) == 0
        except:
            print('This should not be array')
            raise

    def test_124_char(self):
        try:
            assert face_detect('a') == 0
        except:
            print('Unexpected input')
            raise




#How to get logs from different env