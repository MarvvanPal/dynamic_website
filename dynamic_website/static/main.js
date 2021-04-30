const menuBtn = document.querySelector('.menu-btn');
let menuOpen = false;

function myFunction(){
    menuBtn.addEventListener('click', () => {
        if(!menuOpen) {
            menuBtn.classList.add('open');
            menuOpen = true;
        } else {
            menuBtn.classList.remove('open');
            menuOpen = false;
        }
    });
}

document.getElementById("menu-btn").addEventListener("click", function(){myFunction()});