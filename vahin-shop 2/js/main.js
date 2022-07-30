let slides = document.querySelectorAll('.slide');

let index = 0;

slides.forEach((slide, i) => {
    if (i === index) {
        slide.style.display = 'block';
    }
    else {
        slide.style.display = 'none';
    }
})

let nextSlide = () => {
    if (index !== slides.length)
        index++;
}

let prevSlide = () => {
    if (index !== 0)
        index--;
}

let nextButton = document.querySelector('.next')
nextButton.addEventListener('click', nextSlide)

let prevButton = document.querySelector('.prev')
prevButton.addEventListener('click', prevSlide)