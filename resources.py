#Dictionary containing html formated telephone numbers for COVID-19 assistance through Argentina provided by Ministerio de Salud de Argentina

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

traduccion = {
	'United States': 'Estados Unidos',
	'Brazil': 'Brasil',
	'India': 'India',
	'Russia': 'Rusia',
	'South Africa': 'Sudáfrica',
	'Mexico': 'México',
	'Peru': 'Perú',
	'Colombia': 'Colombia',
	'Chile': 'Chile',
	'Iran': 'Irán',
	'Spain': 'España',
	'United Kingdom': 'Reino Unido',
	'Saudi Arabia': 'Arabia Saudita',
	'Pakistan': 'Pakistán',
	'Bangladesh': 'Bangladesh',
	'Argentina': 'Argentina',
	'Italy': 'Italia',
	'Turkey': 'Turquía',
	'Germany': 'Alemania',
	'France': 'Francia',
	'Iraq': 'Irak',
	'Philippines': 'Filipinas',
	'Indonesia': 'Indonesia',
	'Canada': 'Canadá',
	'Qatar': 'Qatar',
	'Kazakhstan': 'Kazajistán',
	'Egypt': 'Egipto',
	'Ecuador': 'Ecuador',
	'Bolivia': 'Bolivia',
	'Israel': 'Israel',
	'China': 'China',
	'Sweden': 'Suecia',
	'Ukraine': 'Ucrania',
	'Oman': 'Omán',
	'Dominican Republic': 'República Dominicana',
	'Panama': 'Panamá',
	'Belgium': 'Bélgica',
	'Kuwait': 'Kuwait',
	'Belarus': 'Bielorrusia',
	'Romania': 'Rumania',
	'United Arab Emirates': 'Emiratos Árabes Unidos',
	'Netherlands': 'Países Bajos',
	'Guatemala': 'Guatemala',
	'Singapore': 'Singapur',
	'Portugal': 'Portugal',
	'Poland': 'Polonia',
	'Japan': 'Japón',
	'Honduras': 'Honduras',
	'Nigeria': 'Nigeria',
	'Bahrain': 'Bahrein',
	'Ghana': 'Ghana',
	'Armenia': 'Armenia',
	'Kyrgyzstan': 'Kirguizistán',
	'Afghanistan': 'Afganistán',
	'Switzerland': 'Suiza',
	'Algeria': 'Argelia',
	'Morocco': 'Marruecos',
	'Azerbaijan': 'Azerbaiyán',
	'Uzbekistan': 'Uzbekistán',
	'Serbia': 'Serbia',
	'Moldova': 'Moldavia',
	'Ireland': 'Irlanda',
	'Kenya': 'Kenia',
	'Venezuela': 'Venezuela',
	'Nepal': 'Nepal',
	'Costa Rica': 'Costa Rica',
	'Ethiopia': 'Etiopía',
	'Austria': 'Austria',
	'Australia': 'Australia',
	'El Salvador': 'El Salvador',
	'Czech Republic': 'Republica Checa',
	'Cameroon': 'Camerún',
	'Ivory Coast': 'Costa de Marfil',
	'Denmark': 'Dinamarca',
	'Palestine': 'Palestina',
	'Bosnia and Herzegovina': 'Bosnia y Herzegovina',
	'South Korea': 'Corea del Sur',
	'Bulgaria': 'Bulgaria',
	'Madagascar': 'Madagascar',
	'North Macedonia': 'Macedonia del norte',
	'Sudan': 'Sudán',
	'Senegal': 'Senegal',
	'Kosovo': 'Kosovo',
	'Norway': 'Noruega',
	'Puerto Rico': 'Puerto Rico',
	'DR Congo': 'República Democrática del Congo',
	'Malaysia': 'Malasia',
	'Zambia': 'Zambia',
	'Gabon': 'Gabón',
	'Guinea': 'Guinea',
	'Tajikistan': 'Tayikistán',
	'Haiti': 'Haití',
	'Finland': 'Finlandia',
	'Luxembourg': 'Luxemburgo',
	'Paraguay': 'Paraguay',
	'Lebanon': 'Líbano',
	'Mauritania': 'Mauritania',
	'Albania': 'Albania',
	'Greece': 'Grecia',
	'Croatia': 'Croacia',
	'Libya': 'Libia',
	'Djibouti': 'Yibuti',
	'Maldives': 'Maldivas',
	'Equatorial Guinea': 'Guinea Ecuatorial',
	'Zimbabwe': 'Zimbabue',
	'Hungary': 'Hungría',
	'Malawi': 'Malawi',
	'Central African Republic': 'República Centroafricana',
	'Hong Kong': 'Hong Kong',
	'Nicaragua': 'Nicaragua',
	'Montenegro': 'Montenegro',
	'Congo': 'Congo',
	'Thailand': 'Tailandia',
	'Eswatini': 'Eswatini',
	'Namibia': 'Namibia',
	'Somalia': 'Somalia',
	'Cuba': 'Cuba',
	'Cape Verde': 'Cabo Verde',
	'Sri Lanka': 'Sri Lanka',
	'Slovakia': 'Eslovaquia',
	'Mali': 'Mali',
	'Suriname': 'Surinam',
	'South Sudan': 'Sudán del Sur',
	'Mozambique': 'Mozambique',
	'Lithuania': 'Lituania',
	'Slovenia': 'Eslovenia',
	'Estonia': 'Estonia',
	'Rwanda': 'Ruanda',
	'Guinea-Bissau': 'Guinea-Bisáu',
	'Iceland': 'Islandia',
	'Donetsk PR': 'República Popular de Donetsk',
	'Sierra Leone': 'Sierra Leona',
	'Benin': 'Benin',
	'Yemen': 'Yemen',
	'Tunisia': 'Túnez',
	'Angola': 'Angola',
	'Uruguay': 'Uruguay',
	'Uganda': 'Uganda',
	'Latvia': 'Letonia',
	'Jordan': 'Jordán',
	'Syria': 'Siria',
	'Georgia': 'Georgia',
	'Cyprus': 'Chipre',
	'Liberia': 'Liberia',
	'The Gambia': 'Gambia',
	'New Zealand': 'Nueva Zelanda',
	'Burkina Faso': 'Burkina Faso',
	'Niger': 'Níger',
	'Malta': 'Malta',
	'USS Theodore Roosevelt': 'USS Theodore Roosevelt',
	'Charles de Gaulle': 'Charles de Gaulle',
	'Togo': 'Togo',
	'Jamaica': 'Jamaica',
	'Andorra': 'Andorra',
	'Bahamas': 'Bahamas',
	'Chad': 'Chad',
	'São Tomé and Príncipe': 'Santo Tomé y Príncipe',
	'Vietnam': 'Vietnam',
	'Somaliland': 'Somalia',
	'Lesotho': 'Lesoto',
	'Aruba': 'Aruba',
	'Diamond Princess': 'Diamond Princess',
	'San Marino': 'San Marino',
	'Luhansk PR': 'Luhansk PR',
	'Guyana': 'Guayana',
	'U.S. Virgin Islands': 'Islas Vírgenes de EE.UU',
	'Taiwan': 'Taiwán',
	'Guam': 'Guam',
	'Burundi': 'Burundi',
	'Comoros': 'Comoras',
	'Myanmar': 'Myanmar',
	'Jersey': 'Jersey',
	'Mauritius': 'Islas Mauricio',
	'Isle of Man': 'Isla del hombre',
	'Faroe Islands': 'Islas Faroe',
	'Mongolia': 'Mongolia',
	'Eritrea': 'Eritrea',
	'Trinidad and Tobago': 'Trinidad y Tobago',
	'Cambodia': 'Camboya',
	'Guernsey': 'Guernesey',
	'Botswana': 'Botswana',
	'Artsakh': 'artsakh',
	'Turks and Caicos Islands': 'Islas Turcas y Caicos',
	'Papua New Guinea': 'Papúa Nueva Guinea',
	'Sint Maarten': 'Sint Maarten',
	'Cayman Islands': 'Islas Caimán',
	'Gibraltar': 'Gibraltar',
	'Northern Cyprus': 'El norte de Chipre',
	'Bermuda': 'islas Bermudas',
	'Belize': 'Belice',
	'Costa Atlantica': 'Costa Atlantica',
	'Barbados': 'Barbados',
	'Brunei': 'Brunei',
	'Abkhazia': 'Abjasia',
	'Monaco': 'Mónaco',
	'Greg Mortimer': 'Greg Mortimer',
	'Seychelles': 'Seychelles',
	'Bhutan': 'Bután',
	'Antigua and Barbuda': 'Antigua y Barbuda',
	'South Ossetia': 'Osetia del Sur',
	'Liechtenstein': 'Liechtenstein',
	'French Polynesia': 'Polinesia francés',
	'Saint Vincent': 'San Vicente',
	'Northern Mariana Islands': 'Islas Marianas del Norte',
	'Macau': 'Macao',
	'MS Roald Amundsen': 'MS Roald Amundsen',
	'Curaçao': 'Curaçao',
	'Fiji': 'Fiji',
	'East Timor': 'Timor del Este',
	'Saint Lucia': 'Santa Lucía',
	'Grenada': 'Granada',
	'New Caledonia': 'Nueva Caledonia',
	'Laos': 'Laos',
	'Dominica': 'dominica',
	'Saint Kitts and Nevis': 'Saint Kitts y Nevis',
	'Greenland': 'Groenlandia',
	'Falkland Islands': 'Islas Malvinas',
	'Montserrat': 'Montserrat',
	'MS Zaandam': 'MS Zaandam',
	'Coral Princess': 'Coral Princess',
	'Vatican City': 'Ciudad del Vaticano',
	'British Virgin Islands': 'Islas Vírgenes Británicas',
	'HNLMS Dolfijn': 'HNLMS Dolfijn',
	'Bonaire': 'Bonaire',
	'Saba': 'Saba',
	'Saint Pierre and Miquelon': 'San Pedro y Miquelón',
	'Anguilla': 'Anguilla',
	'Sint Eustatius': 'San Eustaquio',
	'Tanzania': 'Tanzania'
}


#Country key equivalence between Watsons existing (Country Entity Value/covid19api key) and spanish natural language.
 
natural = {"afghanistan": "Afganistán",
"ala-aland-islands": "ALA Islas Aland",
"albania": "Albania",
"algeria": "Argelia",
"american-samoa": "Samoa Americana",
"andorra": "Andorra",
"angola": "Angola",
"anguilla": "Anguilla",
"antarctica": "Antártida",
"antigua-and-barbuda": "Antigua y Barbuda",
"argentina": "Argentina",
"armenia": "Armenia",
"aruba": "Aruba",
"australia": "Australia",
"austria": "Austria",
"azerbaijan": "Azerbaiyán",
"bahamas": "Bahamas",
"bahrain": "Bahrein",
"bangladesh": "Bangladesh",
"barbados": "Barbados",
"belarus": "Bielorrusia",
"belgium": "Bélgica",
"belize": "Belice",
"benin": "Benin",
"bermuda": "islas Bermudas",
"bhutan": "Bután",
"bolivia": "Bolivia",
"bosnia-and-herzegovina": "Bosnia y Herzegovina",
"botswana": "Botswana",
"bouvet-island": "Isla Bouvet",
"brazil": "Brasil",
"british-indian-ocean-territory": "Territorio Británico del Océano Índico",
"british-virgin-islands": "Islas Vírgenes Británicas",
"brunei": "Brunei Darussalam",
"bulgaria": "Bulgaria",
"burkina-faso": "Burkina Faso",
"burundi": "Burundi",
"cambodia": "Camboya",
"cameroon": "Camerún",
"canada": "Canadá",
"cape-verde": "Cabo Verde",
"cayman-islands": "Islas Caimán",
"central-african-republic": "República Centroafricana",
"chad": "Chad",
"chile": "Chile",
"china": "China",
"christmas-island": "Isla de Navidad",
"cocos-keeling-islands": "Cocos (Keeling)",
"colombia": "Colombia",
"comoros": "Comoras",
"congo-brazzaville": "Congo (Brazzaville)",
"congo-kinshasa": "Congo (Kinshasa)",
"cook-islands": "Islas Cook",
"costa-rica": "Costa Rica",
"cote-divoire": "Costa de Marfil",
"croatia": "Croacia",
"cuba": "Cuba",
"cyprus": "Chipre",
"czech-republic": "Republica checa",
"denmark": "Dinamarca",
"djibouti": "Djibouti",
"dominica": "dominica",
"dominican-republic": "República Dominicana",
"ecuador": "Ecuador",
"egypt": "Egipto",
"el-salvador": "El Salvador",
"equatorial-guinea": "Guinea Ecuatorial",
"eritrea": "Eritrea",
"estonia": "Estonia",
"ethiopia": "Etiopía",
"falkland-islands-malvinas": "Islas Malvinas (Falkland)",
"faroe-islands": "Islas Faroe",
"fiji": "Fiji",
"finland": "Finlandia",
"france": "Francia",
"french-guiana": "Guayana francés",
"french-polynesia": "Polinesia francés",
"french-southern-territories": "Territorios Franceses del Sur",
"gabon": "Gabón",
"gambia": "Gambia",
"georgia": "Georgia",
"germany": "Alemania",
"ghana": "Ghana",
"gibraltar": "Gibraltar",
"greece": "Grecia",
"greenland": "Groenlandia",
"grenada": "Granada",
"guadeloupe": "Guadalupe",
"guam": "Guam",
"guatemala": "Guatemala",
"guernsey": "Guernesey",
"guinea": "Guinea",
"guinea-bissau": "Guinea-Bissau",
"guyana": "Guayana",
"haiti": "Haití",
"heard-and-mcdonald-islands": "Islas Heard y McDonald",
"holy-see-vatican-city-state": "Santa Sede (Ciudad del Vaticano)",
"honduras": "Honduras",
"hong-kong-sar-china": "Hong Kong",
"hungary": "Hungría",
"iceland": "Islandia",
"india": "India",
"indonesia": "Indonesia",
"iran": "Irán",
"iraq": "Irak",
"ireland": "Irlanda",
"isle-of-man": "Isla del hombre",
"israel": "Israel",
"italy": "Italia",
"jamaica": "Jamaica",
"japan": "Japón",
"jersey": "Jersey",
"jordan": "Jordán",
"kazakhstan": "Kazajstán",
"kenya": "Kenia",
"kiribati": "Kiribati",
"korea-north": "Corea (del Norte)",
"korea-south": "Corea del Sur)",
"kuwait": "Kuwait",
"kyrgyzstan": "Kirguizistán",
"lao-pdr": "República Democrática Popular Lao",
"latvia": "Letonia",
"lebanon": "Líbano",
"lesotho": "Lesoto",
"liberia": "Liberia",
"libya": "Libia",
"liechtenstein": "Liechtenstein",
"lithuania": "Lituania",
"luxembourg": "Luxemburgo",
"macao-sar-china": "macao",
"macedonia": "macedonia",
"madagascar": "Madagascar",
"malawi": "Malawi",
"malaysia": "Malasia",
"maldives": "Maldivas",
"mali": "mali",
"malta": "Malta",
"marshall-islands": "Islas Marshall",
"martinique": "Martinica",
"mauritania": "Mauritania",
"mauritius": "Isla mauricio",
"mayotte": "Mayotte",
"mexico": "México",
"micronesia": "micronesia",
"moldova": "Moldavia",
"monaco": "Mónaco",
"mongolia": "Mongolia",
"montenegro": "Montenegro",
"montserrat": "Montserrat",
"morocco": "Marruecos",
"mozambique": "Mozambique",
"myanmar": "Myanmar",
"namibia": "Namibia",
"nauru": "Nauru",
"nepal": "Nepal",
"netherlands": "Países Bajos",
"netherlands-antilles": "Antillas Holandesas",
"new-caledonia": "Nueva Caledonia",
"new-zealand": "Nueva Zelanda",
"nicaragua": "Nicaragua",
"niger": "Níger",
"nigeria": "Nigeria",
"niue": "Niue",
"norfolk-island": "Isla Norfolk",
"northern-mariana-islands": "Islas Marianas del Norte",
"norway": "Noruega",
"oman": "Omán",
"pakistan": "Pakistán",
"palau": "Palau",
"palestine": "Territorio Palestino",
"panama": "Panamá",
"papua-new-guinea": "Papúa Nueva Guinea",
"paraguay": "Paraguay",
"peru": "Perú",
"philippines": "Filipinas",
"pitcairn": "Pitcairn",
"poland": "Polonia",
"portugal": "Portugal",
"puerto-rico": "Puerto Rico",
"qatar": "Katar",
"kosovo": "República de Kosovo",
"réunion": "Reunión",
"romania": "Rumania",
"russia": "Federación Rusa",
"rwanda": "Ruanda",
"saint-helena": "Santa Helena",
"saint-kitts-and-nevis": "Saint Kitts y Nevis",
"saint-lucia": "Santa Lucía",
"saint-pierre-and-miquelon": "San Pedro y Miquelón",
"saint-vincent-and-the-grenadines": "San Vicente y Granadinas",
"saint-barthélemy": "San Bartolomé",
"saint-martin-french-part": "San Martín (parte francesa)",
"samoa": "Samoa",
"san-marino": "San Marino",
"sao-tome-and-principe": "Santo Tomé y Príncipe",
"saudi-arabia": "Arabia Saudita",
"senegal": "Senegal",
"serbia": "Serbia",
"seychelles": "Seychelles",
"sierra-leone": "Sierra Leone",
"singapore": "Singapur",
"slovakia": "Eslovaquia",
"slovenia": "Eslovenia",
"solomon-islands": "Islas Salomón",
"somalia": "Somalia",
"south-africa": "Sudáfrica",
"south-georgia-and-the-south-sandwich-islands": "Georgia del sur y las islas Sandwich del sur",
"south-sudan": "Sudán del Sur",
"spain": "España",
"sri-lanka": "Sri Lanka",
"sudan": "Sudán",
"suriname": "Surinam",
"svalbard-and-jan-mayen-islands": "Svalbard y Jan Mayen",
"swaziland": "Swazilandia",
"sweden": "Suecia",
"switzerland": "Suiza",
"syria": "Siria (Siria)",
"taiwan": "Taiwán",
"tajikistan": "Tayikistán",
"tanzania": "Tanzania",
"thailand": "Tailandia",
"timor-leste": "Timor del Este",
"togo": "Ir",
"tokelau": "Tokelau",
"tonga": "Tonga",
"trinidad-and-tobago": "Trinidad y Tobago",
"tunisia": "Túnez",
"turkey": "pavo",
"turkmenistan": "Turkmenistán",
"turks-and-caicos-islands": "Islas Turcas y Caicos",
"tuvalu": "Tuvalu",
"uganda": "Uganda",
"ukraine": "Ucrania",
"united-arab-emirates": "Emiratos Árabes Unidos",
"united-kingdom": "Reino Unido",
"united-states": "Estados Unidos de America",
"uruguay": "Uruguay",
"us-minor-outlying-islands": "Islas periféricas menores de los Estados Unidos",
"uzbekistan": "Uzbekistán",
"vanuatu": "Vanuatu",
"venezuela": "Venezuela (República Bolivariana)",
"vietnam": "Vietnam",
"virgin-islands": "Islas Virgenes",
"wallis-and-futuna-islands": "Wallis y Futuna",
"western-sahara": "Sahara Occidental",
"yemen": "Yemen",
"zambia": "Zambia",
"zimbabwe": "Zimbabue"}