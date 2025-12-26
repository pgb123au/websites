/**
 * Kindly Call - Landing Page JavaScript
 * Simple, accessible interactivity
 */

// Smooth scroll for anchor links
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scroll for all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Form submission handler
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', handleFormSubmit);
    }

    // Add scroll animation for elements
    observeElements();

    // Mobile menu toggle (if needed in future)
    setupMobileMenu();
});

/**
 * Handle contact form submission
 * @param {Event} e - Form submit event
 */
function handleFormSubmit(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        phone: formData.get('phone'),
        message: formData.get('message')
    };

    // For MVP, just show a thank you message
    // In production, this would send to backend
    console.log('Form submission:', data);

    // Show success message
    showSuccessMessage(e.target);
}

/**
 * Show success message after form submission
 * @param {HTMLFormElement} form - The form element
 */
function showSuccessMessage(form) {
    const successDiv = document.createElement('div');
    successDiv.className = 'form-success';
    successDiv.innerHTML = `
        <h3 style="color: #10B981; margin-bottom: 16px;">✓ Thank You!</h3>
        <p>We've received your information and will be in touch within 24 hours to set up your free trial.</p>
        <p style="margin-top: 16px; font-size: 0.875rem; color: #6B7280;">
            Questions? Call us at <a href="tel:1800000000">1800 XXX XXX</a>
        </p>
    `;
    successDiv.style.cssText = `
        padding: 32px;
        background: #F0FDF4;
        border: 2px solid #10B981;
        border-radius: 12px;
        text-align: center;
    `;

    form.replaceWith(successDiv);

    // Scroll to success message
    successDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

/**
 * Set up intersection observer for scroll animations
 */
function observeElements() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements that should animate
    const animateElements = document.querySelectorAll('.step, .pricing-card, .trust-item, .faq-item, .testimonial');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

/**
 * Add fade-in animation class
 */
const style = document.createElement('style');
style.textContent = `
    .fade-in {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
`;
document.head.appendChild(style);

/**
 * Set up mobile menu toggle (placeholder for future enhancement)
 */
function setupMobileMenu() {
    // Check if we need a mobile menu
    const nav = document.querySelector('.nav');
    if (!nav) return;

    // Only add mobile menu for small screens
    if (window.innerWidth <= 768) {
        // Future: Add hamburger menu toggle
        console.log('Mobile view detected');
    }

    // Listen for resize
    window.addEventListener('resize', () => {
        if (window.innerWidth <= 768) {
            console.log('Mobile view');
        }
    });
}

/**
 * Track CTA button clicks (for analytics)
 * @param {string} buttonName - Name of the button clicked
 */
function trackCTAClick(buttonName) {
    // For MVP, just log
    // In production, send to analytics (PostHog, GA, etc.)
    console.log('CTA clicked:', buttonName);

    // Example for future implementation:
    // if (window.posthog) {
    //     window.posthog.capture('cta_clicked', { button: buttonName });
    // }
}

// Add click tracking to all CTA buttons
document.addEventListener('DOMContentLoaded', () => {
    const ctaButtons = document.querySelectorAll('.btn-primary, .btn-pricing');
    ctaButtons.forEach(button => {
        button.addEventListener('click', () => {
            const buttonText = button.textContent.trim();
            trackCTAClick(buttonText);
        });
    });
});

/**
 * Add active state to nav links based on scroll position
 */
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav a[href^="#"]');

    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.scrollY >= sectionTop - 100) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Add active link style
const navStyle = document.createElement('style');
navStyle.textContent = `
    .nav a.active {
        color: #0D9488;
        font-weight: 600;
    }
`;
document.head.appendChild(navStyle);
