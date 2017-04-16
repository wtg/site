// jshint esversion: 6

let header_element = document.querySelector('.header');
let jumbotrop_element = document.querySelector('.jumbotron');
let projects_element = document.querySelector('.projects');

let scrollFunc = function() {
    let y = window.scrollY;
    if (jumbotrop_element.getBoundingClientRect().bottom <= 47) {
        if (!header_element.classList.contains('show')){
            header_element.classList.add('show');
        }
    } else {
        if (header_element.classList.contains('show')) {
            header_element.classList.remove('show');
        }
    }
};

window.addEventListener("scroll", scrollFunc);
