import 'package:flutter/material.dart';

void main() {
  runApp(const IAmPoor());
}

class IAmPoor extends StatelessWidget {
  const IAmPoor({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.blue,
          title: Center(
            child: Text("I Am Rich", style: TextStyle(color: Colors.white)),
          ),
        ),
        body: Center(child: Image.asset('images/home.png')),
      ),
    );
  }
}
