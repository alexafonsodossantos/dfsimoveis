
    /* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
  var width = window.innerWidth;
  if (width < 768 ) {
    document.getElementById("mySidebar").style.width = "100%";
    document.getElementById("main").style.marginLeft = width.toString()+"px";
  } else {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }

}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}
