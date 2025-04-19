function navbar_logic() {
    let menu = document.getElementById('menu');
    let cross = document.getElementById('cross');
    let hidden_navbar = document.querySelector('.hidden_navbar');
    let seen_navbar = document.querySelector('.seen_navbar');


    menu.onclick = () => {
        hidden_navbar.classList.add('navbar_hidden_navbar_logic');
        seen_navbar.style.display = 'none';
        menu.style.display = 'none';
        cross.style.display = 'flex';
        cross.setAttribute('data-active', 'navbar');
    };
}


function search_logic() {
    let menu = document.getElementById('menu');
    let cross = document.getElementById('cross');
    let seen_navbar = document.querySelector('.seen_navbar');
    let hidden_search = document.querySelector('.hidden_search');

    let search = document.getElementById('search');
    let search_icon = document.getElementById('search_icon');

    search.onclick = () => {
        cross.style.display = 'flex';
        menu.style.display = 'none';
        seen_navbar.style.display = 'none';
        hidden_search.classList.add('navbar_hidden_search_logic');
        cross.setAttribute('data-active', 'search');
    };

    search_icon.onclick = () => {
        hidden_search.classList.remove('navbar_hidden_search_logic');
        cross.style.display = 'none';
        menu.style.display = 'flex';
        seen_navbar.style.display = 'flex';
    };
}


function product_logic() {
    let menu = document.getElementById('menu');
    let cross = document.getElementById('cross');
    let seen_navbar = document.querySelector('.seen_navbar');
    let hidden_product = document.querySelector('.hidden_product');
    let product = document.getElementById('product');

    product.onclick = () => {
        hidden_product.classList.add('navbar_hidden_product_logic');
        cross.style.display = 'flex';
        menu.style.display = 'none';
        seen_navbar.style.display = 'none';
        cross.setAttribute('data-active', 'product');
    };

}

function cross_logic() {
    let cross = document.getElementById('cross');
    cross.onclick = () => {
        let activeSection = cross.getAttribute('data-active');
        let seen_navbar = document.querySelector('.seen_navbar');
        let hidden_product = document.querySelector('.hidden_product');
        let hidden_search = document.querySelector('.hidden_search');
        let hidden_navbar = document.querySelector('.hidden_navbar');
        let menu = document.getElementById('menu');

        if (activeSection === 'navbar') {
            hidden_navbar.classList.remove('navbar_hidden_navbar_logic');
            setTimeout(() => {
                seen_navbar.style.display = 'flex';
            });
        }

        else if (activeSection === 'search') {
            hidden_search.classList.remove('navbar_hidden_search_logic');
            setTimeout(() => {
                seen_navbar.style.display = 'flex';
            });
        }

        else if (activeSection === 'product') {
            hidden_product.classList.remove('navbar_hidden_product_logic');
            setTimeout(() => {
                seen_navbar.style.display = 'flex';
            });
        }

        cross.style.display = 'none';
        menu.style.display = 'flex';
        cross.removeAttribute('data-active');
    };
}

function Animate() {
    let items = document.querySelectorAll('.item.one, .item.two, .item.three');

    let item_count = items.length;
    let active = 1;
    let autoPlay;

    items[0].classList.add('prev');
    items[1].classList.add('active');

    autoPlay = setInterval(() => {
        active = active + 1 >= item_count ? 0 : active + 1;
<<<<<<< HEAD
        let prev = active - 1 < 0 ? item_count-1 : active - 1;

        let old_active = document.querySelector('.active')
        if(old_active) {
=======
        let prev = active - 1 < 0 ? item_count - 1 : active - 1;

        let old_active = document.querySelector('.active')
        if (old_active) {
>>>>>>> branch
            old_active.classList.remove('active');
        }

        let old_prev = document.querySelector('.prev')
<<<<<<< HEAD
        if(old_prev) old_prev.classList.remove('prev');
=======
        if (old_prev) old_prev.classList.remove('prev');
>>>>>>> branch

        items[active].classList.add('active');
        items[prev].classList.add('prev');

    }, 5000);

    return autoPlay;
}

<<<<<<< HEAD
=======
function wishlist() {
    let wishlist_button = document.getElementsByClassName("add_to_wishlist");

    Array.from(wishlist_button).forEach((btn) => {
        btn.addEventListener("click",function(e){
            e.preventDefault();
            let path = btn.querySelector("path");
            const current_color = path.getAttribute("fill");
            if (current_color === "gray") {
                path.setAttribute("fill", "none");
            } else {
                path.setAttribute("fill", "gray");
            }
        });
    });
}

>>>>>>> branch
document.addEventListener("DOMContentLoaded", () => {
    navbar_logic();
    product_logic();
    search_logic();
    cross_logic();
    // Animate();
<<<<<<< HEAD
=======
    wishlist();
>>>>>>> branch
})