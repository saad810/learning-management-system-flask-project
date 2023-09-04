var flash_msg = document.getElementById('flash_msg');

if (flash_msg.innerText !== "") {
    flash_msg.style.display = 'block';

      setTimeout(function() {
        flash_msg.style.display = 'none';
    }, 10000); // 4000 milliseconds = 4 seconds
}else{
    flash_msg.style.display = none;
}
