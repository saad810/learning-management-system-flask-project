window.onload = flash_msg;

function flash_msg() {
  var flash_msg = document.getElementById("flash_msg");
  if (flash_msg.innerHTML == "") {
    flash_msg.style.display = "none";
  } else {
    flash_msg.style.display = "block";

    setTimeout(function () {
      flash_msg.style.display = "none";
    }, 5000); // 5000 milliseconds = 5 seconds
  }
}
