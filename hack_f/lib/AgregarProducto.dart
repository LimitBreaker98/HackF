import 'package:flutter/material.dart';
import 'dart:async';

class AgrefarProducto extends StatefulWidget {
  @override
  _AgrefarProductoState createState() => _AgrefarProductoState();
}

// Nombre,
// descripcion
// precio
// ubicacion
// unidad de media
// tipo de ptoducto
// fecha de cosecha
// campesino
// oferta
List<DropdownMenuItem> tiposMedidas = [
  DropdownMenuItem(
    child: Text('Kg'),
    value: 'Kg',
  ),
  DropdownMenuItem(
    child: Text('Lb'),
    value: 'Lb',
  ),
];

List<DropdownMenuItem> campesinos;

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
String _selectedProd;

class _AgrefarProductoState extends State<AgrefarProducto> {
  String _selectedmed;
  String _selectedcampe;

  DateTime _birthDay = new DateTime(
      DateTime.now().year - 18, DateTime.now().month, DateTime.now().day);

  /// selecciona el dia de nacimiento
  Future seleccioarDia(BuildContext context) async {
    DateTime picked = await showDatePicker(
        context: context,
        initialDate: _birthDay,
        firstDate: DateTime(1940, 1),
        lastDate: new DateTime(3000));
    if (picked != null && picked != _birthDay)
      setState(() {
        _birthDay = picked;
      });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Agregar Productos'),
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
                      tag: 'carrito',
                      child: Column(
                        children: <Widget>[
                          Icon(
                            Icons.add_shopping_cart,
                            size: 200,
                            color: Theme.of(context).secondaryHeaderColor,
                          ),
                          Text('Agregar producto',
                              style: Theme.of(context).textTheme.headline),
                        ],
                      ),
                    )),
                  ),
                  Flexible(
                    flex: 5,
                    child: ConstrainedBox(
                      constraints:
                          BoxConstraints(maxWidth: 1200, maxHeight: 650),
                      child: Padding(
                        padding: const EdgeInsets.symmetric(
                            horizontal: 30, vertical: 0),
                        child: Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: ConstrainedBox(
                            child: Card(
                              elevation: 8,
                              child: Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: Form(
                                    child: Column(
                                  children: <Widget>[
                                    SizedBox(
                                      height: 20,
                                    ),
                                    DropdownButtonFormField(
                                      value: _selectedProd,
                                      hint: Text('producto'),
                                      items: productos,
                                      onChanged: (value) {
                                        setState(() {
                                          _selectedProd = value;
                                        });
                                      },
                                    ),
                                    TextFormField(
                                      decoration:
                                          InputDecoration(labelText: 'Nombre'),
                                    ),
                                    TextFormField(
                                      decoration: InputDecoration(
                                          labelText: 'Ubicacion'),
                                    ),
                                    SizedBox(
                                      height: 30,
                                    ),
                                    DropdownButtonFormField(
                                      value: _selectedProd,
                                      hint: Text('Tipo Medida'),
                                      items: tiposMedidas,
                                      onChanged: (value) {
                                        setState(() {
                                          _selectedmed = value;
                                        });
                                      },
                                    ),
                                    SizedBox(
                                      height: 30,
                                    ),
                                    TextFormField(
                                      keyboardType: TextInputType.multiline,
                                      decoration: InputDecoration(
                                          labelText: 'Descripcón'),
                                      maxLines: 3,
                                    ),
                                    SizedBox(
                                      height: 30,
                                    ),
                                    Row(
                                      children: <Widget>[
                                        RaisedButton(
                                          onPressed: () =>
                                              seleccioarDia(context),
                                          child: Text(
                                            "seleccionar..",
                                          ),
                                        ),
                                        SizedBox(
                                          width: 20,
                                        ),
                                        Container(
                                          child: (_birthDay == null)
                                              ? Text('Seleccionar')
                                              : Text(
                                                  '${_birthDay.day}/${_birthDay.month}/${_birthDay.year}',
                                                  style: Theme.of(context)
                                                      .textTheme
                                                      .subtitle),
                                        ),
                                      ],
                                    ),
                                    SizedBox(
                                      height: 20,
                                    ),
                                    DropdownButtonFormField(
                                      value: _selectedProd,
                                      hint: Text('producto'),
                                      items: campesinos,
                                      onChanged: (value) {
                                        setState(() {
                                          _selectedProd = value;
                                        });
                                      },
                                    ),
                                    SizedBox(
                                      height: 20,
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
                            constraints:
                                BoxConstraints(maxHeight: 1100, maxWidth: 300),
                          ),
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
