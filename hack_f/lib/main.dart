import 'package:flutter/material.dart';
import 'package:hack_f/AgregarProducto.dart';
import 'package:hack_f/datos.dart';
import 'package:hack_f/profileCreator.dart';

import 'contratos.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AgroMatch',
      theme: ThemeData(
          primarySwatch: Colors.green, secondaryHeaderColor: Colors.cyan),
      home: MyHomePage(title: 'Acciones'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Center(child: Text(widget.title)),
      ),
      body: Container(
          child: Column(
        children: <Widget>[
          Image.asset(
            'assets/logo-social.png',
            scale: 1.5,
          ),
          Container(
            margin: EdgeInsets.symmetric(horizontal: 20, vertical: 50),
            child: ConstrainedBox(
              constraints: BoxConstraints(maxHeight: 400),
              child: ListView(
                padding: EdgeInsets.symmetric(horizontal: 20),
                scrollDirection: Axis.horizontal,
                children: <Widget>[
                  Padding(
                    padding:
                        const EdgeInsets.symmetric(horizontal: 15, vertical: 8),
                    child: InkWell(
                      onTap: goToCrearPerfil,
                      child: Card(
                        elevation: 7,
                        child: Column(
                          children: <Widget>[
                            Hero(
                              tag: 'assignment_ind',
                              child: Column(
                                children: <Widget>[
                                  Icon(
                                    Icons.assignment_ind,
                                    size: 200,
                                    color:
                                        Theme.of(context).secondaryHeaderColor,
                                  ),
                                  Text('Crear un perfil',
                                      style:
                                          Theme.of(context).textTheme.headline),
                                ],
                              ),
                            ),
                            Padding(
                              padding: EdgeInsets.symmetric(
                                  horizontal: 10, vertical: 30),
                              child: Text(
                                'Crear un perfilamiento para el campesino, \nde esta manera es posible generar la información \npara poder ofrecerle contratos con los mayoristas.',
                                softWrap: true,
                                textAlign: TextAlign.left,
                                style: Theme.of(context).textTheme.body2,
                              ),
                            )
                          ],
                        ),
                      ),
                    ),
                  ),
                  Padding(
                    padding:
                        const EdgeInsets.symmetric(horizontal: 15, vertical: 8),
                    child: InkWell(
                      onTap: goToAgregarProducto,
                      child: Card(
                        elevation: 8,
                        child: Column(
                          children: <Widget>[
                            Hero(
                              tag: 'carrito',
                              child: Column(
                                children: <Widget>[
                                  Icon(
                                    Icons.add_shopping_cart,
                                    size: 200,
                                    color:
                                        Theme.of(context).secondaryHeaderColor,
                                  ),
                                  Text('Agregar producto',
                                      style:
                                          Theme.of(context).textTheme.headline),
                                ],
                              ),
                            ),
                            Padding(
                              padding: EdgeInsets.symmetric(
                                  horizontal: 10, vertical: 30),
                              child: Text(
                                'Agregar un porducto que un campesino quiere \ncultivar y/o que quiere obtener un credito \npara este cultivo.',
                                softWrap: true,
                                textAlign: TextAlign.left,
                                style: Theme.of(context).textTheme.body2,
                              ),
                            )
                          ],
                        ),
                      ),
                    ),
                  ),
                  Padding(
                    padding:
                        const EdgeInsets.symmetric(horizontal: 15, vertical: 8),
                    child: InkWell(
                      onTap: goToDatos,
                      child: Card(
                        elevation: 8,
                        child: Column(
                          children: <Widget>[
                            Icon(
                              Icons.data_usage,
                              size: 200,
                              color: Theme.of(context).secondaryHeaderColor,
                            ),
                            Text('Ver los datos',
                                style: Theme.of(context).textTheme.headline),
                            Padding(
                              padding: EdgeInsets.symmetric(
                                  horizontal: 10, vertical: 30),
                              child: Text(
                                'Visualizar los datos de los precios \nde los productos de forma histórica que le \npueden ser de utilidad al campesino.',
                                softWrap: true,
                                textAlign: TextAlign.left,
                                style: Theme.of(context).textTheme.body2,
                              ),
                            )
                          ],
                        ),
                      ),
                    ),
                  ),
                  Padding(
                    padding:
                        const EdgeInsets.symmetric(horizontal: 15, vertical: 8),
                    child: InkWell(
                      onTap: goToContratos,
                      child: Card(
                        elevation: 8,
                        child: Column(
                          children: <Widget>[
                            Hero(
                              tag: 'trabajo',
                              child: Column(
                                children: <Widget>[
                                  Icon(
                                    Icons.work,
                                    size: 200,
                                    color:
                                        Theme.of(context).secondaryHeaderColor,
                                  ),
                                  Text(
                                    'Ver contratos',
                                    style: Theme.of(context).textTheme.headline,
                                    textAlign: TextAlign.center,
                                  ),
                                ],
                              ),
                            ),
                            Padding(
                              padding: EdgeInsets.symmetric(
                                  horizontal: 10, vertical: 30),
                              child: Text(
                                'visualizar los datos de los contratos \nque empareja el campesino con la empresa \nminoritaria.',
                                softWrap: true,
                                textAlign: TextAlign.left,
                                style: Theme.of(context).textTheme.body2,
                              ),
                            )
                          ],
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      )),
    );
  }

  goToAgregarProducto() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => AgrefarProducto()),
    );
  }

  goToCrearPerfil() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => profileCreator()),
    );
  }

  goToDatos() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => datos()),
    );
  }

  goToContratos() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => contratos()),
    );
  }
}
