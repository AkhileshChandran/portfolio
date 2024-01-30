
document.addEventListener('DOMContentLoaded', function () {
    var options = {
        strings: ['Python','Django','HTML','CSS','Bootstrap','React','MySQL'],
        typeSpeed: 50,
        backSpeed: 50,
        loop: true
    };

    var typed = new Typed('.text', options);
});



function scrollToAbout() {
    document.getElementById('about-me').scrollIntoView({ behavior: 'smooth' });
}


document.addEventListener('DOMContentLoaded', function () {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        });

     
const animatedElements = document.querySelectorAll('.animate-me');
        animatedElements.forEach(element => {
            observer.observe(element);
        });
    });

