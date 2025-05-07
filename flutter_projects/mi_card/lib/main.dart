import 'package:flutter/material.dart';

void main() {
  runApp(const MiCard());
}

class MiCard extends StatelessWidget {
  const MiCard({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: SafeArea(
          child: Container(
            alignment: Alignment.center,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                const CircleAvatar(
                  radius: 50.0,
                  backgroundImage: AssetImage('images/avatar.png'),
                ),
                Container(
                  margin: EdgeInsets.only(top: 10.0),
                  child: Text(
                    'Vianney YOVO',
                    style: TextStyle(
                      fontSize: 25.0,
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontFamily: 'Pacifico',
                    ),
                  ),
                ),
                const Text(
                  'FLUTTER DEVELOPER',
                  style: TextStyle(
                    fontFamily: 'SourceSans3',
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                    fontSize: 15.0,
                    letterSpacing: 3,
                  ),
                ),
                SizedBox(
                  height: 20.0,
                  width: 100.0,
                  child: Divider(color: Colors.teal.shade100),
                ),
                Card(
                  margin: EdgeInsets.symmetric(
                    vertical: 10.0,
                    horizontal: 25.0,
                  ),
                  color: Colors.white,
                  child: ListTile(
                    leading: Icon(Icons.call, color: Colors.teal, size: 20.0),
                    title: Text('+228 91694791'),
                  ),
                ),
                Card(
                  margin: EdgeInsets.symmetric(
                    vertical: 10.0,
                    horizontal: 25.0,
                  ),
                  color: Colors.white,
                  child: ListTile(
                    leading: Icon(Icons.email, color: Colors.teal, size: 20.0),
                    title: Text('vianney.yovo@epitech.eu'),
                  ),
                ),
              ],
            ),
          ),
        ),
        backgroundColor: Colors.teal,
      ),
    );
  }
}
