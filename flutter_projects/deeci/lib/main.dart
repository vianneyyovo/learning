import 'package:flutter/material.dart';

void main() {
  runApp(const Deeci());
}

class Deeci extends StatelessWidget {
  const Deeci({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.red,
        appBar: AppBar(
          backgroundColor: Colors.red,
          title: Center(
            child: const Text(
              'Deeci',
              style: TextStyle(
                color: Colors.white,
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ),
        body: const DeeciPage(),
      ),
    );
  }
}

class DeeciPage extends StatelessWidget {
  const DeeciPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.red,
      child: Expanded(
        child: Center(
          child: Row(
            children: <Widget>[
              Expanded(child: Image.asset('images/dice1.png', height: 150)),
              Expanded(child: Image.asset('images/dice2.png', height: 150)),
            ],
          ),
        ),
      ),
    );
  }
}
