# Student Recognizer

Student Recognizer is a mobile application that allows users to recognize and retrieve detailed information about students by capturing their photo. The app utilizes facial recognition technology to compare the input photo with a database of pre-trained student photos. It provides a convenient and efficient way to retrieve student details on the go.

## Features

- Capture student photo: Users can use the app's camera functionality to capture a photo of a student.
- Facial recognition: The app utilizes facial recognition algorithms to compare the captured photo with the pre-trained student photos stored in the backend.
- Retrieve student details: Upon successful recognition, the app displays the student's information, including their name, ID, and other relevant details.
- Train student data: Register new students and train their faces by providing 1 to 3 photos per student through the web interface.

## Technologies Used

- Flutter: Frontend development framework for building the mobile app.
- Django: Backend web framework that handles facial recognition and student data management.
- Student Database: Student details are stored in a JSON file named `student.json`.

## Installation

1. Clone the repository and navigate to the backend directory.
2. Set up the virtual environment and install the required packages.
3. Start the Django server.
4. Open the repository in a Flutter-compatible IDE.
5. Run the app on a connected Android or iOS device/emulator.

## Usage

1. Launch the Student Recognizer app and grant camera permissions.
2. Capture a photo of the student to recognize.
3. The app sends the photo to the backend for facial recognition.
4. If the student is recognized, their details are displayed.
5. To train new students, visit `http://domainIp/register/` in a web browser. \n`eg: http://171.248.25.10:8000/register/`
6. Fill in the student details and provide 1 to 3 photos.
7. Submit the form to register and train the student.

## Limitations and Future Improvements

- Storage: Consider migrating from a JSON file to a more scalable database solution like MongoDB.
- Performance: Optimize the app's performance for larger databases by implementing indexing and caching.
- Security: Ensure secure storage and transmission of student details.
- User interface enhancements: Add search functionality and sorting options for student details.

## Contributing

1. Fork the repository and create a new branch.
2. Make and commit your changes.
3. Push the branch and submit a pull request.

## License

This project is licensed under the MIT License.
