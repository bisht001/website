function navbar_logic() {
    console.log("hi");
    let menu = document.getElementById('menu');
    let cross = document.getElementById('cross');
    let hidden_navbar = document.querySelector('.hidden_navbar');
    let seen_navbar = document.querySelector('.seen_navbar');


    menu.onclick = () => {
        hidden_navbar.classList.add('hidden_navbar_logic');
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
        hidden_search.classList.add('hidden_search_logic');
        cross.setAttribute('data-active', 'search');
    };

    search_icon.onclick = () => {
        hidden_search.classList.remove('hidden_search_logic');
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
        hidden_product.classList.add('hidden_product_logic');
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
            hidden_navbar.classList.remove('hidden_navbar_logic');
            setTimeout(() => {
                seen_navbar.style.display = 'flex';
            }, 800);
        }

        else if (activeSection === 'search') {
            hidden_search.classList.remove('hidden_search_logic');
            setTimeout(() => {
                seen_navbar.style.display = 'flex';
            }, 500);
        }

        else if (activeSection === 'product') {
            hidden_product.classList.remove('hidden_product_logic');
            setTimeout(() => {
                seen_navbar.style.display = 'flex';
            }, 800);
        }

        cross.style.display = 'none';
        menu.style.display = 'flex';
        cross.removeAttribute('data-active');
    };
}

function animation() {
    let items = document.querySelectorAll('.item')
    items.forEach((item) => {
        item.display = "none";
    });

    let item_count = items.length;
    let active = 1;
    let autoPlay;

    console.log("Active Item:", active, "Prev Item:", prev);

    autoPlay = setInterval(() => {
        active = active + 1 >= item_count ? 0 : active + 1;
        let prev = active - 1 < 0 ? item_count-1 : active - 1;

        let old_active = document.querySelector('.active')
        if(old_active) old_active.classList.remove('active');

        let old_prev = document.querySelector('.prev')
        if(old_prev) old_prev.classList.remove('prev');

        items[active].classList.add('active');
        items[prev].classList.add('prev');
    }, 5000);

    return autoPlay;
}
document.addEventListener("DOMContentLoaded", () => {
    navbar_logic();
    product_logic();
    search_logic();
    cross_logic();
    animation();
})