async function sendData(){
      var sendData = {
        "1": document.getElementById("1").value,
        "2": document.getElementById("2").value,
        "3": document.getElementById("3").value,
        "4": document.getElementById("4").value,
        "5": document.getElementBYId("5").value
      }
       fetch('/sendHandAngles', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(sendData) 
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
 
    }

setInterval(sendData,100);
function down(){
  one = document.getElementById("1");
  two = document.getElementById("2");
  three = document.getElementById("3");
  four = document.getElementById("4");
  five = document.getElementById("5");
}