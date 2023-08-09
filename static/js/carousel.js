
let currentIndex = 0;
const images = document.querySelectorAll('.carousel-image');

// Adjust the width and height of all images
const targetWidth = 200; // Change this to your desired width
const targetHeight = 200; // Change this to your desired height

images.forEach(image => {
    image.style.width = targetWidth + 'px';
    image.style.height = targetHeight + 'px';
});

function rotateCarousel() {
    images[currentIndex].style.transform = 'translateX(-100%)';
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].style.transform = 'translateX(0)';
}

setInterval(rotateCarousel, 500); // Rotate every 5 seconds