
// Initialize Swiper
const heroSwiper = new Swiper('.hero-slider .swiper', {
    slidesPerView: 1,
    spaceBetween: 0,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

// Initialize AOS (Animate On Scroll)
AOS.init({
    duration: 1000,
    once: false,
});

// Counter Animation
function animateCounter() {
    const counters = document.querySelectorAll('.counter');
    counters.forEach(counter => {
        const target = parseInt(counter.textContent);
        const increment = target / 100;
        let current = 0;

        const updateCount = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current) + '+';
                setTimeout(updateCount, 20);
            } else {
                counter.textContent = target + '+';
            }
        };

        updateCount();
    });
}

// Trigger counter animation when visible
window.addEventListener('load', () => {
    const counterSection = document.querySelector('.counter');
    if (counterSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter();
                    observer.unobserve(entry.target);
                }
            });
        });
        observer.observe(counterSection);
    }
});

// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Navbar toggler
document.addEventListener('click', function (e) {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbar = document.querySelector('.navbar-collapse');

    if (navbarToggler && navbar && !navbarToggler.contains(e.target) && !navbar.contains(e.target)) {
        if (navbar.classList.contains('show')) {
            navbarToggler.click();
        }
    }
});

// Form handling
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function (e) {
        console.log('Form submitted');
    });
});

// Lazy loading images
if ('IntersectionObserver' in window) {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.src = entry.target.dataset.src;
                observer.unobserve(entry.target);
            }
        });
    });
    images.forEach(img => imageObserver.observe(img));
}

console.log('✓ Evren Academy site initialized');
