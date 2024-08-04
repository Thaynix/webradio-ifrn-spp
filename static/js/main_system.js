document.addEventListener("DOMContentLoaded", function() {
    let btn = document.getElementById("btn");
    let sidebar = document.getElementsByClassName("sidebar")[0];

    btn.onclick = function() {
        sidebar.classList.toggle("active");
    }
});