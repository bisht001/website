

function navbar_design() {
    let sliding_menu = document.querySelector('.sliding_menu');
    let menu = document.querySelector('.menu');
    let cross = document.querySelector('.cross');

    menu.onclick = () => {
        sliding_menu.classList.add('hidden');
        menu.style.display = 'none';
        cross.style.display = 'flex';
    }

    cross.onclick = () => {
        sliding_menu.classList.remove('hidden');
        menu.style.display = 'flex';
        cross.style.display = 'none';
    }
}

document.addEventListener("DOMContentLoaded", () => {
    navbar_design(); 
});