#Dictionary containing telephone numbers for COVID-19 assistance through Argentina provided by Ministerio de Salud de Argentina

nacional = '<a class="aLight" href="tel:120">Llamá al: 120</a>'
telefonos = {
	'Buenos-Aires-Autonomous-City': ' Ciudad Autónoma de Buenos Aire<br><a class="aLight" href="tel:148"> Llamá al: 148</a>',
	'Buenos-Aires-Province': 		' Provincia de Buenos Aire<br><a class="aLight" href="tel:383-15-423-8872"> Llamá al: 383-15-423-8872</a>',
	'Catamarca':				 	' Catamarc<br><a class="aLight" href="tel:0800-444-0829"> Llamá al: 0800-444-0829</a>',
	'Chaco': 						' Chaco<br><a class="aLight" href="tel:0800-222-2676"> Llamá al: 0800-222-2676</a>',
	'Chubut': 						' Chubu<br><a class="aLight" href="tel:107"> Llamá al: 107</a>',
	'Córdoba': 						' Córdoba<br><a class="aLight" href="tel:0800-122-1444"> Llamá al: 0800-122-1444</a>',
	'Corrientes': 					' Corrientes<br><a class="aLight" href="tel:0379-497-4811"> Llamá al: 0379-497-4811</a>',
	'Entre-Ríos': 					' Entre Ríos<br><a class="aLight" href="tel:0800-777-8476"> Llamá al: 0800-777-8476</a>',
	'Formosa': 						' Formosa<br><a class="aLight" href="tel:107"> Llamá al: 107</a>',
	'Jujuy': 						' Jujuy<br><a class="aLight" href="tel:0800-888-4767"> Llamá al: 0800-888-4767</a>',
	'La-Pampa': 					' La Pampa<br><a class="aLight" href="tel:0800-333-1135"> Llamá al: 0800-333-1135</a>',
	'La-Rioja': 					' La Rioja<br><a class="aLight" href="tel:107"> Llamá al: 107</a>',
	'Mendoza': 						' Mendoza<br><a class="aLight" href="tel:0800-800-26843"> Llamá al: 0800-800-26843</a>',
	'Misiones': 					' Misiones<br><a class="aLight" href="tel:0800-444-3400"> Llamá al: 0800-444-3400</a>',
	'Neuquén': 						' Neuquén<br><a class="aLight" href="tel:0800-333-1002"> Llamá al: 0800-333-1002</a>',
	'Río-Negro': 					' Río Negro<br><a class="aLight" href="tel:911"> Llamá al: 911</a>',
	'Salta': 						' Salta<br><a class="aLight" href="tel:911"> Llamá al: 911</a>',
	'San-Juan': 					' San Luis<br><a class="aLight" href="tel:107"> Llamá al: 107</a>',
	'San-Luis': 					' San Juan<br><a class="aLight" href="tel:107"> Llamá al: 107</a>',
	'Santa-Cruz': 					' Santa Cruz<br><a class="aLight" href="tel:107"> Llamá al: 107</a>',
	'Santa-Fe': 					' Santa Fe<br><a class="aLight" href="tel:0800-555-6549"> Llamá al: 0800-555-6549</a>',
	'Santiago-del-Estero': 			' Santiago del Estero<br><a class="aLight" href="tel:0800-888-6737"> Llamá al: 0800-888-6737</a>',
	'Tierra-del-Fuego': 			' Tierra del Fuego Antártida e Islas del Atlántico Sur<br><a class="aLight" href="tel:107"> Llamá al: 107</a>',
	'Tucuman': 						' Tucumán<br><a class="aLight" href="tel:0800-555-8478"> Llamá al: 0800-555-8478</a>'
}

def mensaje_contacto(provincia):
	mensaje = '<b>Ministerio de Salud</b><br>'+nacional+'<br>'+ telefonos[provincia]
	return mensaje