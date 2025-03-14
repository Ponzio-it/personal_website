const carousel = document.querySelector(".certificates-grid");
const cards = document.querySelectorAll(".certificate-card");
const prevButton = document.querySelector(".carousel-btn.prev");
const nextButton = document.querySelector(".carousel-btn.next");

let cardsToShow = getCardsToShow(); // Number of cards visible at a time
const totalCards = cards.length;
let totalSlides = Math.ceil(totalCards / cardsToShow);
let currentSlide = 0;



function getCardsToShow() {
    if (window.innerWidth <= 768) {
        return 1
    } else {
        return 2
    }
}

// Function to update the total number of slides
function updateTotalSlides() {
    cardsToShow = getCardsToShow();
    totalSlides = Math.ceil(totalCards / cardsToShow);
}

// Function to update the carousel position
function updateCarousel() {
    const cardStyle = window.getComputedStyle(cards[0]);
    const cardWidth = cards[0].offsetWidth + parseFloat(cardStyle.marginRight);
    const offset = currentSlide * cardsToShow * -cardWidth;
    carousel.style.transform = `translateX(${offset}px)`;
}


// Event listener for the "Next" button
nextButton.addEventListener("click", () => {
    currentSlide++;
    if (currentSlide >= totalSlides) {
        currentSlide = 0; // Loop back to the start
    }
    updateCarousel();
});

// Event listener for the "Previous" button
prevButton.addEventListener("click", () => {
    currentSlide--;
    if (currentSlide < 0) {
        currentSlide = totalSlides - 1; // Loop back to the end
    }
    updateCarousel();
});

// Recalculate on window resize (for responsive design)
window.addEventListener("resize", () => {
    updateTotalSlides();
    updateCarousel();
});

// Initialize the carousel
updateTotalSlides();
updateCarousel();
