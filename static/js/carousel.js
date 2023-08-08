let currentIndex = 0;
const images = document.querySelectorAll('.carousel-image');

function rotateCarousel() {
    images[currentIndex].style.transform = 'translateX(-100%)';
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].style.transform = 'translateX(0)';
}

setInterval(rotateCarousel, 5000);