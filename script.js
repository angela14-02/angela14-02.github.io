var swiper = new Swiper(".mySwiper-1", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev", // Corregido
    },
});

// Selecciona el botón "¡COMENZAMOS!"
const startButton = document.querySelector('.btn-start');

// Agrega el evento al botón
startButton.addEventListener('click', () => {
    // Obtén la imagen activa del slider
    const activeSlide = document.querySelector('.swiper-slide-active img');
    if (activeSlide) {
        const gameUrl = activeSlide.getAttribute('data-url'); // Obtén la URL del juego
        if (gameUrl) {
            window.location.href = gameUrl; // Redirige al juego
        }
    }
});
