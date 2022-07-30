let slides = document.querySelectorAll('.slide');

let index = 0;

let changeSlider = (index) => {
    slides.forEach((slide, i) => {
        if (i === index) {
            slide.style.display = 'block';
        }
        else {
            slide.style.display = 'none';
        }
    })
}

changeSlider(index)

let nextSlide = () => {
    if (index !== slides.length - 1) {
        index++
        changeSlider(index);
    }

}

let prevSlide = () => {
    if (index !== 0) {
        index--;
        changeSlider(index);
    }
}



let nextButton = document.querySelector('.next')
nextButton.addEventListener('click', nextSlide)

let prevButton = document.querySelector('.prev')
prevButton.addEventListener('click', prevSlide)
