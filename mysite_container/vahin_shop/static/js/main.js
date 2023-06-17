const images = document.querySelectorAll('.slider .slider_line img');
const sliderLine = document.querySelector('.slider_line');
let index = 0;
let width;

function init() {
    console.log('resize');
    width = document.querySelector('.slider').offsetWidth;
    sliderLine.style.width = width * images.length + 'px';
    images.forEach(item => {
        item.style.width = width + 'px';
        item.style.height = 'auto';
    });
    rollSlider();
}

window.addEventListener('resize', init);
init();

// document.querySelector('radio').addEventListener('click', function () {
//     index--;
//     if (index < 0) {
//         index = images.length - 1;
//     }
//     rollSlider();
// });

// document.querySelector('.slider_next').addEventListener('click', function () {
//     index++;
//     if (index >= images.length) {
//         index = 0;
//     }
//     rollSlider();
// });

function rollSlider() {
    sliderLine.style.transform = 'translate(-' + index * width + 'px)';
}

setInterval(function () {
    rollSlider(index)
    index++;
    if (index == 4) {
        index = 0;
    }
}, 5000)

function slides_number(i) {
    var dots = document.querySelectorAll(".dot")
    dots[index].className.replace("checked", "");

    for (var i = 0; i < dots.length; i++) {
        if (i !== index) {
            dots[index].className.replace("", "checked");
        }
    }
    rollSlider(index);
    index = i;
    rollSlider()
}