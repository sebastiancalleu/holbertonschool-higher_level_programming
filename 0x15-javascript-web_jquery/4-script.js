$("#toggle_header").click(function(){
  if ($("header").hasClass("green")) {
    $("header").removeClass("green")
    $("header").toggleClass("red");
  } else {
    $("header").removeClass("red")
    $("header").toggleClass("green");
  }
});
