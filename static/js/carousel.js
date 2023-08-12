document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector(".carousel");
    const prevButton = document.querySelector(".prev-button");
    const nextButton = document.querySelector(".next-button");

    let currentIndex = 0;
    const albumsPerPage = 3; // Number of albums displayed per slide

    function showSlide(index) {
        const translateXValue = -index * (100 / albumsPerPage); // Display albumsPerPage albums at a time
        carousel.style.transform = `translateX(${translateXValue}%)`;
    }

    function nextSlide() {
        currentIndex = (currentIndex + albumsPerPage) % albumsData.length;
        showSlide(currentIndex);
    }

    function prevSlide() {
        currentIndex = (currentIndex - albumsPerPage + albumsData.length) % albumsData.length;
        showSlide(currentIndex);
    }

    prevButton.addEventListener("click", prevSlide);
    nextButton.addEventListener("click", nextSlide);

    showSlide(currentIndex);
});