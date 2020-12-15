# This is a Python project with tests for face_detect method.

###Prerequisites:
1.  Python installed (Python3.7)

### Test execution:
````
pip install -r requirements.txt
pytest <path_to_tests_file> (e.g. pytest /Tests/test_face_detect.py
if you are in the project directory)

OR

you can simply use pytest - m faceRecognitionTest in the (/automation)
direcotry
````
If you want to run the tests with html report
````
pytest <path_to_test_file> -v --html==report-test.html
pytest -m faceRecognitionTest -v --html=report-test.html
````
Test photos are located in:
````
/<path_to_the_project>/Tests/Resources
````
