import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert' as convert;

class contratos extends StatefulWidget {
  @override
  _contratosState createState() => _contratosState();
}

class _contratosState extends State<contratos> {
  var _selected;

  @override
  void initState() {
    getCampesinos();

    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Contratos"),
        ),
        body: Container(
          child: Column(
            children: <Widget>[
              Hero(
                tag: 'trabajo',
                child: Column(
                  children: <Widget>[
                    Icon(
                      Icons.work,
                      size: 100,
                      color: Theme.of(context).secondaryHeaderColor,
                    ),
                    Text(
                      'Ver contratos',
                      style: Theme.of(context).textTheme.headline,
                      textAlign: TextAlign.center,
                    ),
                  ],
                ),
              ),
              Text('Usuario'),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: ConstrainedBox(
                    constraints: BoxConstraints(maxHeight: 100, maxWidth: 300),
                    child: DropdownButtonFormField(
                      value: _selected,
                      items: ['hello1', 'hello2']
                          .map((label) => DropdownMenuItem(
                                child: Text(label),
                                value: label,
                              ))
                          .toList(),
                      onChanged: (value) {
                        setState(() => _selected = value);
                      },
                    )),
              ),
              Expanded(
                child: SizedBox(
                  height: 400,
                  child: GridView.count(
                    children: <Widget>[
                      MatchWidget('empresa', 'oferta', 'papas',
                          ['Ectarias', 'cercania', 'calidad']),
                      MatchWidget('empresa', 'oferta', 'papas',
                          ['Ectarias', 'cercania', 'calidad']),
                      MatchWidget('empresa', 'oferta', 'papas',
                          ['Ectarias', 'cercania', 'calidad']),
                      MatchWidget('empresa', 'oferta', 'papas',
                          ['Ectarias', 'cercania', 'calidad']),
                    ],
                    crossAxisCount: 3,
                  ),
                ),
              ),
            ],
          ),
        ));
  }

  void getCampesinos() async {
    var response = await http.get('http://157.253.227.85:8000/campesinos');
    var jsonResponse = convert.jsonDecode(response.body);

    print(jsonResponse);
  }
}

class MatchWidget extends StatelessWidget {
  var empresa;

  var oferta;

  List<String> razones;

  var producto;

  MatchWidget(this.empresa, this.producto, this.oferta, this.razones);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(20),
      child: Card(
        elevation: 8,
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(children: <Widget>[
            Text(
              'Empresa',
              style: Theme.of(context).textTheme.title,
            ),
            Text(
              empresa,
              style: Theme.of(context).textTheme.display1,
            ),
            Text(
              'Producto',
              style: Theme.of(context).textTheme.title,
            ),
            Text(
              producto,
              style: Theme.of(context).textTheme.display1,
            ),
            Text(
              'Oferta',
              style: Theme.of(context).textTheme.title,
            ),
            Text(
              oferta,
              style: Theme.of(context).textTheme.display1,
            ),
            Text(
              'Razones',
              style: Theme.of(context).textTheme.title,
            ),
            Text(
              razones.toString(),
              textAlign: TextAlign.center,
              style: Theme.of(context).textTheme.display1,
            ),
          ]),
        ),
      ),
    );
  }
}
