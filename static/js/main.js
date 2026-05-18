document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    const navbar = document.querySelector('.navbar');
    const backToTop = document.querySelector('.back-to-top');

    function setPopupState(isOpen) {
        body.classList.toggle('popup-open', isOpen);
    }

    function setupAdmissionPopup() {
        const popup = document.getElementById('admissionPopup');
        const close = document.getElementById('admissionPopupClose');
        const openers = document.querySelectorAll('.js-open-admission');

        if (!popup) return;

        const open = function () {
            popup.classList.add('show');
            popup.setAttribute('aria-hidden', 'false');
            setPopupState(true);
        };

        const dismiss = function () {
            popup.classList.remove('show');
            popup.setAttribute('aria-hidden', 'true');
            setPopupState(false);
        };

        openers.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                open();
            });
        });

        if (close) close.addEventListener('click', dismiss);
        popup.addEventListener('click', event => {
            if (event.target === popup) dismiss();
        });
    }

    function setupSitePopup() {
        const popup = document.getElementById('sitePopup');
        if (!popup) return;

        const close = popup.querySelector('.site-popup__close');
        const showOnce = popup.dataset.once === 'true';
        const storageKey = 'evrenSitePopupShown';

        if (showOnce && sessionStorage.getItem(storageKey)) return;

        const dismiss = function () {
            popup.classList.remove('show');
            setPopupState(false);
            if (showOnce) sessionStorage.setItem(storageKey, 'true');
        };

        setTimeout(function () {
            popup.classList.add('show');
            setPopupState(true);
        }, 1100);

        if (close) close.addEventListener('click', dismiss);
        popup.addEventListener('click', event => {
            if (event.target === popup) dismiss();
        });
    }

    function setupHeroSlider() {
        const heroSlider = document.querySelector('.hero-slider');
        if (!heroSlider || typeof Swiper === 'undefined') return;

        if (heroSlider.dataset.mediaFit) {
            heroSlider.style.setProperty('--hero-media-fit', heroSlider.dataset.mediaFit);
        }

        const autoplayDelay = parseInt(heroSlider.dataset.autoplay || '5500', 10);
        const transitionSpeed = parseInt(heroSlider.dataset.speed || '1400', 10);

        new Swiper('.hero-slider .swiper', {
            slidesPerView: 1,
            loop: true,
            speed: transitionSpeed,
            effect: 'fade',
            fadeEffect: { crossFade: true },
            autoplay: {
                delay: autoplayDelay,
                disableOnInteraction: false,
                pauseOnMouseEnter: true,
            },
            pagination: {
                el: '.hero-slider .swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.hero-slider .swiper-button-next',
                prevEl: '.hero-slider .swiper-button-prev',
            },
        });
    }

    function setupTestimonials() {
        if (typeof Swiper === 'undefined' || !document.querySelector('.testimonialSwiper')) return;

        new Swiper('.testimonialSwiper', {
            slidesPerView: 1,
            spaceBetween: 24,
            loop: true,
            autoplay: {
                delay: 4500,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.testimonialSwiper .swiper-pagination',
                clickable: true,
            },
            breakpoints: {
                768: { slidesPerView: 2 },
                1200: { slidesPerView: 3 },
            },
        });
    }

    function animateCounter(counter) {
        const rawValue = counter.textContent.replace(/[^\d]/g, '');
        const target = parseInt(rawValue, 10);
        if (Number.isNaN(target)) return;

        const suffix = counter.textContent.replace(/[\d]/g, '');
        let current = 0;
        const increment = Math.max(target / 90, 1);

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

    function setupCounters() {
        const counters = document.querySelectorAll('.counter');
        if (!('IntersectionObserver' in window) || counters.length === 0) return;

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => observer.observe(counter));
    }

    function setupSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (event) {
                const href = this.getAttribute('href');
                if (!href || href === '#') return;

                const target = document.querySelector(href);
                if (!target) return;

                event.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            });
        });
    }

    function setupMobileNavClose() {
        document.addEventListener('click', function (event) {
            const toggler = document.querySelector('.navbar-toggler');
            const collapse = document.querySelector('.navbar-collapse');
            if (!toggler || !collapse) return;

            const clickedOutside = !toggler.contains(event.target) && !collapse.contains(event.target);
            if (clickedOutside && collapse.classList.contains('show')) toggler.click();
        });
    }

    function syncScrollState() {
        const isScrolled = window.scrollY > 24;
        if (navbar) navbar.classList.toggle('is-scrolled', isScrolled);
        if (backToTop) backToTop.classList.toggle('show', window.scrollY > 500);
    }

    window.addEventListener('scroll', syncScrollState, { passive: true });
    if (backToTop) {
        backToTop.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    document.addEventListener('keydown', function (event) {
        if (event.key !== 'Escape') return;
        document.querySelectorAll('.site-popup.show, .popup-overlay.show').forEach(popup => {
            popup.classList.remove('show');
        });
        setPopupState(false);
    });

    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 850,
            easing: 'ease-out-cubic',
            once: true,
            offset: 70,
        });
    }

    setupAdmissionPopup();
    setupSitePopup();
    setupHeroSlider();
    setupTestimonials();
    setupCounters();
    setupSmoothScroll();
    setupMobileNavClose();
    syncScrollState();
});
