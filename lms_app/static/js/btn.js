window.onload = flash_msg();

function flash_msg() {
  var flash_msg = document.getElementById("flash_msg");
  if (flash_msg.innerText !== "") {
    flash_msg.style.display = "block";

    setTimeout(function () {
      flash_msg.style.display = "none";
    }, 5000); // 10000 milliseconds = 10 seconds
  } else {
    flash_msg.style.display = "none"; // Use "none" as a string
  }
}
