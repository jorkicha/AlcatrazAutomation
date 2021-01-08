import os

import pytest
from colorama import Fore
from libs.face_detect import face_detect
import libs.data_success_rate

test_path = libs.data_success_rate.path_to_picture
test_number_face = libs.data_success_rate.number_of_faces
path = os.getcwd() + '/Tests/Resources/SuccessRateResources/'



@pytest.mark.successTest
class SuccessRateTest():

    test_path = libs.data_success_rate.path_to_picture
    test_number_face = libs.data_success_rate.number_of_faces

    def test_201_test(self):

        array_length = len(test_path)

        total_success = 0
        total_fail = 0
        for i in range(array_length):

            try:
                assert face_detect(test_path[i]) == test_number_face[i]
                total_success = total_success + 1
                print(str(face_detect(test_path[i])) + ' faces were found.')
            except AssertionError as e:
                print(str(face_detect(test_path[i])) + ' faces were found, but we expect ' + str(test_number_face[i]) + ' faces to be found.')
                total_fail = total_fail + 1

        print(Fore.RED +'\nThe total amount of FAILURES are: ' + str(total_fail))
        print(Fore.GREEN +'The total amount of the SUCCESS are: ' + str(total_success))
        total_tests = total_success + total_fail
        success_rate = (total_success / total_tests) * 100
        success_rate = round(success_rate)
        print(Fore.BLUE + 'The SUCCESS RATE for this method is: ' + str(success_rate) + '%')

