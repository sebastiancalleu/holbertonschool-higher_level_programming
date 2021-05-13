fetch("https://fourtonfish.com/hellosalut/?lang=fr")
.then(response => response.json())
.then(function(data){
  $("#hello").text(data.hello)
});
