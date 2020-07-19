document.getElementById('usrMessageInput').focus();

const colors = ["rgb(255,186,73)", "rgb(242,103,74)", "rgb(32,163,158)"];
const randomColor = colors[Math.floor(Math.random() * colors.length)];
document.body.style.backgroundColor = randomColor;


var input = document.getElementById("usrMessageInput");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13 && input.value !== '') {
    event.preventDefault();
    send()
  }
});

function send(){
	var check = document.getElementById('usrMessageInput').value;
	if (check != ''){
		sendForReals();
	}
}
var listNode = document.getElementById('messages');

function createBubble(text, clase){
	
	if (text.includes('http')){
		listNode.innerHTML += '<a href="'+text+'"><div class="botMessage frame"><img class="media" src="'+text+'"></div></a>';
	}
	else{
		var liNode2 = document.createElement("div"),
					txtNode2 = document.createTextNode(text);
					liNode2.className = clase;
		liNode2.appendChild(txtNode2);
		listNode.appendChild(liNode2);
	}
	listNode.innerHTML += '<div class="divider"></div>';
	listNode.scrollIntoView({ behavior: 'smooth', block: 'end' });
}

function sendForReals(){
	var txtVal = document.getElementById('usrMessageInput').value;
	createBubble(txtVal+'\u200E', "usrMessage" );
	
	//Agrego bubble con texto ingresado por el usr
	
	listNode.innerHTML += '<div id="loadingLi"><img class="loading" src="static/loading.gif"></div>';
	
	//call a nuestra api
	const url = window.location.href + 'input?msg=' + txtVal;

	document.getElementById('usrMessageInput').value = '';

	var request = new Request(url, {method: 'GET'});
	//console.log('request =', request);
	var responseVal;
	fetch(request)
		.then(function(response) {
			//console.log('response =', response);
			return response.text();
		})
		.then(function(data) {
			var loading = document.getElementById('loadingLi');
			loading.parentNode.removeChild(loading);
			
			responseVal = data;
			console.log(responseVal)
			if (responseVal.includes("DOCTYPE")){
				responseVal = "Lo sentimos hubo un error al procesar tu mensaje, intente de nuevo."
			}
			
			var res = responseVal.split("\n");
			for (var i = 0; i<res.length; i++){
				createBubble(res[i], "botMessage");
			}
		})
		.catch(function(err) {
			console.error(err);
		});
}