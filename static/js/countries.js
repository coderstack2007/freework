/* ISO Country Code to Country Name */

var countries = {
  AF: "Afghanistan",
  AL: "Albania",
  DZ: "Algeria",
  AO: "Angola",
  AQ: "Antarctica",
  AR: "Argentina",
  AM: "Armenia",
  AU: "Australia",
  AT: "Austria",
  AZ: "Azerbaijan",
  BD: "Bangladesh",
  BY: "Belarus",
  BE: "Belgium",
  BZ: "Belize",
  BJ: "Benin",
  BT: "Bhutan",
  BO: "Bolivia",
  BA: "Bosnia And Herzegovina",
  BW: "Botswana",
  BR: "Brazil",
  BN: "Brunei Darussalam",
  BG: "Bulgaria",
  BF: "Burkina Faso",
  BI: "Burundi",
  KH: "Cambodia",
  CM: "Cameroon",
  CA: "Canada",
  CF: "Central African Republic",
  TD: "Chad",
  CL: "Chile",
  CN: "China",
  CO: "Colombia",
  CG: "Congo",
  CD: "Congo",
  CR: "Costa Rica",
  CI: "Cote D'Ivoire",
  HR: "Croatia",
  CU: "Cuba",
  CY: "Cyprus",
  CZ: "Czech Republic",
  DK: "Denmark",
  DJ: "Djibouti",
  DO: "Dominican Republic",
  EC: "Ecuador",
  EG: "Egypt",
  SV: "El Salvador",
  GQ: "Equatorial Guinea",
  ER: "Eritrea",
  EE: "Estonia",
  ET: "Ethiopia",
  FI: "Finland",
  FR: "France",
  GF: "French Guiana",
  GA: "Gabon",
  GM: "Gambia",
  GE: "Georgia",
  DE: "Germany",
  GH: "Ghana",
  GR: "Greece",
  GL: "Greenland",
  GT: "Guatemala",
  GN: "Guinea",
  GW: "Guinea-Bissau",
  GY: "Guyana",
  HT: "Haiti",
  HN: "Honduras",
  HU: "Hungary",
  IS: "Iceland",
  IN: "India",
  ID: "Indonesia",
  IR: "Iran",
  IQ: "Iraq",
  IE: "Ireland",
  IL: "Israel",
  IT: "Italy",
  JM: "Jamaica",
  JP: "Japan",
  JO: "Jordan",
  KZ: "Kazakhstan",
  KE: "Kenya",
  KP: "North Korea",
  KR: "South Korea",
  KW: "Kuwait",
  KG: "Kyrgyzstan",
  LA: "Laos",
  LV: "Latvia",
  LB: "Lebanon",
  LS: "Lesotho",
  LR: "Liberia",
  LY: "Libya",
  LT: "Lithuania",
  LU: "Luxembourg",
  MK: "Macedonia",
  MG: "Madagascar",
  MW: "Malawi",
  MY: "Malaysia",
  ML: "Mali",
  MR: "Mauritania",
  MX: "Mexico",
  MD: "Moldova",
  MN: "Mongolia",
  ME: "Montenegro",
  MA: "Morocco",
  MZ: "Mozambique",
  MM: "Myanmar",
  NA: "Namibia",
  NP: "Nepal",
  NL: "Netherlands",
  NZ: "New Zealand",
  NI: "Nicaragua",
  NE: "Niger",
  NG: "Nigeria",
  NO: "Norway",
  OM: "Oman",
  PK: "Pakistan",
  PA: "Panama",
  PG: "Papua New Guinea",
  PY: "Paraguay",
  PE: "Peru",
  PH: "Philippines",
  PL: "Poland",
  PT: "Portugal",
  PR: "Puerto Rico",
  QA: "Qatar",
  RO: "Romania",
  RU: "Russia",
  RW: "Rwanda",
  SA: "Saudi Arabia",
  SN: "Senegal",
  RS: "Serbia",
  SL: "Sierra Leone",
  SK: "Slovakia",
  SI: "Slovenia",
  SO: "Somalia",
  ZA: "South Africa",
  ES: "Spain",
  LK: "Sri Lanka",
  SD: "Sudan",
  SS: "South Sudan",
  SR: "Suriname",
  SZ: "Swaziland",
  SE: "Sweden",
  CH: "Switzerland",
  SY: "Syria",
  TW: "Taiwan",
  TJ: "Tajikistan",
  TZ: "Tanzania",
  TH: "Thailand",
  TG: "Togo",
  TT: "Trinidad And Tobago",
  TN: "Tunisia",
  TR: "Turkey",
  TM: "Turkmenistan",
  UG: "Uganda",
  UA: "Ukraine",
  AE: "United Arab Emirates",
  GB: "United Kingdom",
  US: "United States",
  UY: "Uruguay",
  UZ: "Uzbekistan",
  VE: "Venezuela",
  VN: "Viet Nam",
  EH: "Western Sahara",
  YE: "Yemen",
  ZM: "Zambia",
  ZW: "Zimbabwe",
};
var myearth;
var localNewsMarker;
var news = [];

window.addEventListener( "earthjsload", function() {

	myearth = new Earth( document.getElementById('element'), {

		location : {lat: 18, lng: 50},
		zoom: 1.05,
		light: 'none',
		
		transparent : true,
		mapSeaColor : 'RGBA(255,255,255,0.76)',
		mapLandColor : '#383838',
		mapBorderColor : '#5D5D5D',
		mapBorderWidth : 0.25,
		mapStyles : ' #CU, #DO, #HT, #JM, #PR { fill: red; stroke: red; } ',
		mapHitTest : true,

		autoRotate: true,
		autoRotateSpeed: 0.7,
		autoRotateDelay: 4000,
		
	} );
	
	
	myearth.addEventListener( "ready", function() {
	
		this.startAutoRotate();
		
		
		// Caribbean
		
	


		


		news[2].element.addEventListener( 'click', highlightBreakingNews );
		
		myearth.addMarker( {
			location: {lat: 3.52, lng: 97.3},
			mesh : "Pin3",
			color : "red",
			scale: 0.4,
			hotspot: false,
		} );
		
		
	} );
	
	
	
	var selectedCountry;
	
	myearth.addEventListener( 'click', function( event ) {
		
		if ( event.id ) {
		
			if ( selectedCountry != event.id ) {
				selectedCountry = event.id;
				document.getElementById('country-name').innerHTML = countries[ event.id ];
				document.getElementById('local-news').classList.add( 'has-news' );
				document.getElementById('local-news').classList.toggle( 'toggle-news' );
			}
			
			// create news marker on first click
			
			if ( ! localNewsMarker ) {
			
				localNewsMarker = this.addMarker( {
					mesh : "Marker",
					color: '#257cff',
					location : event.location,
					scale: 0.01
				} );
				
				localNewsMarker.animate( 'scale', 0.9, { easing: 'out-back' } );
			
			} else {
				
				localNewsMarker.animate( 'location', event.location, { duration: 200, relativeDuration: 50, easing: 'in-out-cubic' } );
			
			}
			
		}
		
	} );
	
} );


function highlightBreakingNews( event ) {

	var overlay = event.target.closest('.earth-overlay').overlay;
	var newsId = overlay.newsId;
	
	document.getElementById( 'breaking-news-'+ newsId ).classList.add( 'news-highlight' );
	setTimeout( function(){
		document.getElementById( 'breaking-news-'+ newsId ).classList.remove( 'news-highlight' );
	}, 500 );
	
	myearth.goTo( overlay.location, { duration: 250, relativeDuration: 70 } );
	
	event.stopPropagation();
}

function gotoBreakingNews( newsId ) {

	myearth.goTo( news[ newsId ].location, { duration: 250, relativeDuration: 70 } );
	
}