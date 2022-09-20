
function getLocation() {
  if (navigator.geolocation) {
    console.log(navigator.geolocation.getCurrentPosition(showPosition));
  } else {
    window.alert("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
    console.log("Latitude: " + position.coords.latitude);
    console.log("Longitude: " + position.coords.longitude);
    var mapsUrl = "https://www.google.com/maps/embed/v1/directions?key=AIzaSyBsep33o3nQJ7aGEMyak2QIvS4YaeHIVVg&origin="+String(position.coords.latitude)+","+String(position.coords.longitude)+"&destination={{imovel.endereco}},{{imovel.bairro}},{{imovel.cidade}}&avoid=tolls|highways"
    document.getElementById('mapa').src = mapsUrl
}
