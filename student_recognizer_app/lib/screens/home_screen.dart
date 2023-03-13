import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';
import 'package:student_recognizer/screens/constants/constants.dart';

import '../env.sample.dart';
import '../models/student.dart';

class HomeScreen extends StatefulWidget {
  @override
  HomeScreenState createState() => HomeScreenState();
}

class HomeScreenState extends State<HomeScreen> {
  final employeeListKey = GlobalKey<HomeScreenState>();
  late ImagePicker imagePicker;

  @override
  void initState() {
    super.initState();
    imagePicker = ImagePicker();
  }

  void selectPhoto() async {
    setState(() {
      imageToShow = null;
    });
    var file = await imagePicker.pickImage(source: ImageSource.gallery);
    if (file == null) {
      return;
    }
    sendImage(file);
  }

  void takePhoto() async {
    setState(() {
      imageToShow = null;
    });
    var xFile = await imagePicker.pickImage(source: ImageSource.camera);
    if (xFile == null) {
      return;
    }
    sendImage(xFile);
  }

  var loading = false;

  void sendImage(XFile xFile) async {
    setState(() {
      loading = true;
    });
    currentStudent == null;
    currentStudentMap == null;
    try {
      // final uri = Uri.parse("${Env.URL_PREFIX}/upload");
      File file = File(xFile.path);
      setState(() {
        imageToShow = file;
      });
      String url = '${Env.URL_PREFIX}/upload/';
      var request = http.MultipartRequest('POST', Uri.parse(url));
      var fileStream = http.ByteStream(file.openRead());
      var fileLength = await file.length();
      var multipartFile = http.MultipartFile('file', fileStream, fileLength,
          filename: "send image");
      request.files.add(multipartFile);
      print("loading");
      var response = await request.send();
      if (response.statusCode == 200) {
        // json.decode(response.).cast<Map<String, dynamic>>();
        dynamic data = json
            .decode(await response.stream.bytesToString())
            .cast<Map<String, dynamic>>();
        print("file sent");
        print(data);

        setState(() {
          loading = false;

          if (data[0]["name"] != null) {
            currentStudent = Student.fromJson(
              Map<String, dynamic>.from(student_details[data[0]["name"]]!),
            );
            currentStudentMap = student_details[data[0]["name"]]!;

            showCustomDialog();
          } else {
            showDialog(
              context: context,
              builder: (context) => Dialog(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(20.0)),
                child: const SizedBox(
                  width: 300,
                  height: 300,
                  child: Center(
                    child: Text("cannot detect face. Try Again!"),
                  ),
                ),
              ),
            );
          }
        });
      } else {
        print("file not send");
      }
    } catch (error) {
      print(error);
    }
  }

  TextStyle infoTextStyle1 =
      const TextStyle(fontSize: 18, fontWeight: FontWeight.w600);
  TextStyle infoTextStyle2 =
      const TextStyle(fontSize: 18, fontWeight: FontWeight.w400);
  Student? currentStudent;
  Map<String, dynamic>? currentStudentMap;
  void showCustomDialog() {
    if (currentStudent == null || currentStudentMap == null) {
      return;
    } else {
      showDialog(
        context: context,
        builder: (context) => Dialog(
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(12.0)),
          child: Container(
            height: 500.0,
            width: 600.0,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Padding(
                  padding: EdgeInsets.all(10.0),
                  child: Text(
                    currentStudent!.name,
                    style: const TextStyle(
                        fontSize: 28, fontWeight: FontWeight.w500),
                  ),
                ),
                Flexible(
                  child: SingleChildScrollView(
                    child: Column(
                        children: currentStudentMap!.entries
                            .map((e) => Padding(
                                  padding: const EdgeInsets.only(
                                      left: 15.0, top: 8, bottom: 8, right: 8),
                                  child: Row(
                                    mainAxisAlignment:
                                        MainAxisAlignment.spaceAround,
                                    children: [
                                      Expanded(
                                          flex: 2,
                                          child: Text(
                                            "${e.key}: ",
                                            style: infoTextStyle1,
                                          )),
                                      (e.key != "Email")
                                          ? Expanded(
                                              flex: 3,
                                              child: Text(
                                                e.value.toString(),
                                                style: infoTextStyle2,
                                              ),
                                            )
                                          : Expanded(
                                              flex: 3,
                                              child: FittedBox(
                                                child: Text(
                                                  e.value.toString(),
                                                  style: infoTextStyle2,
                                                ),
                                              ),
                                            ),
                                    ],
                                  ),
                                ))
                            .toList()),
                  ),
                )
              ],
            ),
          ),
        ),
      );
    }
  }

  File? imageToShow;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: employeeListKey,
      appBar: AppBar(
        title: const Text(
          'Student Regonizer',
        ),
        centerTitle: true,
      ),
      body: Stack(children: [
        Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Expanded(
                  child: ClipRRect(
                borderRadius: BorderRadius.circular(20),
                child: Card(
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(20)),
                  child: Container(
                    child: (imageToShow == null)
                        ? Image.asset("assets/images/empty_image.png")
                        : GestureDetector(
                            onDoubleTap: showCustomDialog,
                            child: Image.file(imageToShow!)),
                  ),
                ),
              )),
              Container(
                margin: const EdgeInsets.all(10),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    ElevatedButton(
                      onPressed: takePhoto,
                      child: const Text("Take  Photo"),
                    ),
                    ElevatedButton(
                      onPressed: selectPhoto,
                      child: const Text("Select photo"),
                    ),
                  ],
                ),
              ),
              // Text(FaceName)
            ],
          ),
        ),
        loading
            ? Container(
                width: double.infinity,
                height: double.infinity,
                color: Color.fromARGB(167, 223, 222, 219),
                child: const Center(child: CircularProgressIndicator()),
              )
            : const SizedBox.shrink(),
      ]),
    );
  }
}
