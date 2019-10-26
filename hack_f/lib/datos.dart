import 'package:flutter/material.dart';
import 'dart:async' show Future;
import 'package:flutter/services.dart' show rootBundle;

class datos extends StatefulWidget {
  @override
  _datosState createState() => _datosState();
}

class _datosState extends State<datos> {
  List<DropdownMenuItem> productos = [
    DropdownMenuItem(
      child: Text('Ajo'),
      value: 'Ajo',
    ),
    DropdownMenuItem(
      child: Text('Aguacate Hass'),
      value: 'Aguacate Hass',
    ),
    DropdownMenuItem(
      child: Text('Ahuyama'),
      value: 'Ahuyama',
    ),
    DropdownMenuItem(
      child: Text('Apio'),
      value: 'Apio',
    ),
    DropdownMenuItem(
      child: Text('Cebolla cabezona blanca'),
      value: 'Cebolla cabezona blanca',
    ),
  ];
  String _selected;

  Future<String> loadAsset() async {
    return await rootBundle.loadString('assets/promedio.txt');
  }

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Datos'),
      ),
      body: Container(
        margin: EdgeInsets.all(50),
        child: Card(
          child: Column(
            children: <Widget>[
              DropdownButtonFormField(
                hint: Text('Productos'),
                value: _selected,
                items: productos,
                onChanged: (value) {
                  setState(() {
                    _selected = value;
                  });
                },
              ),
              ConstrainedBox(
                constraints: BoxConstraints(maxHeight: 500),
                child: _selected != null
                    ? Image.asset('assets/$_selected.png')
                    : Center(child: Text('Seleccione un producto')),
              )
            ],
          ),
        ),
      ),
    );
  }
}
