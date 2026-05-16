// ==========================================
// EVREN ACADEMY - MAIN JAVASCRIPT
// ==========================================

document.addEventListener('DOMContentLoaded', function () {
    console.log('✓ Evren Academy site initialized');

    // ==========================================
    // HERO SWIPER
    // ==========================================
    if (typeof Swiper !== 'undefined' && document.querySelector('.hero-slider .swiper')) {
        new Swiper('.hero-slider .swiper', {
            slidesPerView: 1,
            spaceBetween: 0,
            loop: true,
            speed: 1000,
            effect: 'fade',
            fadeEffect: {
                crossFade: true,
            },
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
                pauseOnMouseEnter: true,
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
    }

    // ==========================================
    // AOS ANIMATION
    // ==========================================
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 1000,
            easing: 'ease-in-out',
            once: true,
            offset: 50,
        });
    }

    // ==========================================
    // COUNTER ANIMATION
    // ==========================================
    function animateCounter(counter) {
        const rawValue = counter.textContent.replace(/[^\d]/g, '');
        const target = parseInt(rawValue, 10);

        if (isNaN(target)) return;

        const suffix = counter.textContent.replace(/[\d]/g, '');
        let current = 0;
        const increment = Math.max(target / 100, 1);

        function update() {
            current += increment;

            if (current < target) {
                counter.textContent = Math.floor(current) + suffix;
                requestAnimationFrame(update);
            } else {
                counter.textContent = target + suffix;
            }
        }

        update();
    }

    const counters = document.querySelectorAll('.counter');

    if ('IntersectionObserver' in window && counters.length > 0) {
        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    obs.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.5,
        });

        counters.forEach(counter => observer.observe(counter));
    }

    // ==========================================
    // SMOOTH SCROLLING
    // ==========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');

            if (!href || href === '#') return;

            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();

                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start',
                });
            }
        });
    });

    // ==========================================
    // MOBILE NAVBAR AUTO CLOSE
    // ==========================================
    document.addEventListener('click', function (e) {
        const toggler = document.querySelector('.navbar-toggler');
        const collapse = document.querySelector('.navbar-collapse');

        if (!toggler || !collapse) return;

        const clickedOutside =
            !toggler.contains(e.target) &&
            !collapse.contains(e.target);

        if (clickedOutside && collapse.classList.contains('show')) {
            toggler.click();
        }
    });

    // ==========================================
    // FORM SUBMIT LOG
    // ==========================================
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function () {
            console.log('Form submitted');
        });
    });

    // ==========================================
    // LAZY LOAD IMAGES
    // ==========================================
    if ('IntersectionObserver' in window) {
        const lazyImages = document.querySelectorAll('img[data-src]');

        const imageObserver = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;

                    img.src = img.dataset.src;

                    img.onload = function () {
                        img.removeAttribute('data-src');
                    };

                    obs.unobserve(img);
                }
            });
        });

        lazyImages.forEach(img => imageObserver.observe(img));
    }

    // ==========================================
    // STICKY HEADER SHADOW
    // ==========================================
    const navbar = document.querySelector('.navbar');

    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 20) {
                navbar.classList.add('shadow-sm');
            } else {
                navbar.classList.remove('shadow-sm');
            }
        });
    }
});