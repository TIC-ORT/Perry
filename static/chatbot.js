var input = document.getElementById("usrMessageInput");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13 && input.value !== '') {
    event.preventDefault();
    send()
  }
});
function send(){
	var txtVal = document.getElementById('usrMessageInput').value,
		listNode = document.getElementById('messages'),
		liNode = document.createElement("li")
		txtNode = document.createTextNode(txtVal+'\u200E');

	liNode.className = "usrMessage";
	liNode.appendChild(txtNode);
	listNode.appendChild(liNode);

	const url = 'https://Chatbot--ignaciopardo.repl.co/input?msg=' + txtVal

	document.getElementById('usrMessageInput').value = '';
	var request = new Request(url, {method: 'GET'});
	console.log('request =', request);
	var responseVal;
	fetch(request)
		.then(function(response) {
			console.log('response =', response);
			return response.text();
		})
		.then(function(data) {
			responseVal = data;
			var liNode2 = document.createElement("li"),
				txtNode2 = document.createTextNode(responseVal);
				liNode2.className = "botMessage";
				liNode2.appendChild(txtNode2);
				listNode.appendChild(liNode2);
		})
		.catch(function(err) {
			console.error(err);
		});
}