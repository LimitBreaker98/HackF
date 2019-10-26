import 'package:flutter/material.dart';

class profileCreator extends StatefulWidget {
  @override
  _profileCreatorState createState() => _profileCreatorState();
}

class _profileCreatorState extends State<profileCreator> {
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      resizeToAvoidBottomPadding: false,
      resizeToAvoidBottomInset: true,
      appBar: AppBar(
        title: Text('Crear un perfil'),
      ),
      body: Container(
        child: SingleChildScrollView(
          child: Column(
            children: <Widget>[
              SizedBox(height: 10, width: 10),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Flexible(
                    flex: 2,
                    child: Container(
                        child: Hero(
                      tag: 'assignment_ind',
                      child: Column(
                        children: <Widget>[
                          Icon(
                            Icons.assignment_ind,
                            size: 200,
                            color: Theme.of(context).secondaryHeaderColor,
                          ),
                          Text('Crear un perfil',
                              style: Theme.of(context).textTheme.headline),
                        ],
                      ),
                    )),
                  ),
                  Flexible(
                    flex: 5,
                    child: ConstrainedBox(
                      constraints:
                          BoxConstraints(maxWidth: 1000, maxHeight: 650),
                      child: Padding(
                        padding: const EdgeInsets.symmetric(
                            horizontal: 30, vertical: 150),
                        child: Card(
                          elevation: 8,
                          child: Form(
                              child: Column(
                            children: <Widget>[
                              SizedBox(
                                height: 30,
                              ),
                              Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: ConstrainedBox(
                                  constraints: BoxConstraints(
                                      maxHeight: 100, maxWidth: 300),
                                  child: TextFormField(
                                    decoration:
                                        InputDecoration(labelText: 'Nombre'),
                                  ),
                                ),
                              ),
                              Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: ConstrainedBox(
                                  constraints: BoxConstraints(
                                      maxHeight: 100, maxWidth: 300),
                                  child: TextFormField(
                                    decoration:
                                        InputDecoration(labelText: 'Ubicación'),
                                  ),
                                ),
                              ),
                              SizedBox(
                                height: 30,
                              ),
                              RaisedButton(
                                child: Text('Crear'),
                                color: Theme.of(context).buttonColor,
                                onPressed: () {
                                  Navigator.pop(context);
                                },
                              )
                            ],
                          )),
                        ),
                      ),
                    ),
                  )
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
