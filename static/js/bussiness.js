document.addEventListener("DOMContentLoaded", function () {
    // Handle "Compare Plans" button
    const comparePlansBtn = document.querySelector('.compare-plans');
    if (comparePlansBtn) {
        comparePlansBtn.addEventListener('click', () => {
            alert('Comparing plans...');
        });
    }

    // Handle "Learn More" buttons
    const learnMoreButtons = document.querySelectorAll('.learn-more');
    learnMoreButtons.forEach(button => {
        button.addEventListener('click', () => {
            alert('Learning more...');
        });
    });

    // Get modal elements
    const loginModal = document.getElementById("loginModal");
    const registerModal = document.getElementById("registerModal");

    // Get buttons
    const loginBtn = document.getElementById("loginBtn");
    const closeLogin = document.getElementById("closeLogin");
    const closeRegister = document.getElementById("closeRegister");
    const registerLink = document.getElementById("registerLink");
    const loginLink = document.getElementById("loginLink");

    // Open login modal
    if (loginBtn && loginModal) {
        loginBtn.addEventListener("click", function () {
            loginModal.style.display = "block";
        });
    }

    // Close login modal
    if (closeLogin && loginModal) {
        closeLogin.addEventListener("click", function () {
            loginModal.style.display = "none";
        });
    }

    // Close registration modal
    if (closeRegister && registerModal) {
        closeRegister.addEventListener("click", function () {
            registerModal.style.display = "none";
        });
    }

    // Switch to register modal
    if (registerLink && loginModal && registerModal) {
        registerLink.addEventListener("click", function (event) {
            event.preventDefault();
            loginModal.style.display = "none";
            registerModal.style.display = "block";
        });
    }

    // Switch to login modal
    if (loginLink && registerModal && loginModal) {
        loginLink.addEventListener("click", function (event) {
            event.preventDefault();
            registerModal.style.display = "none";
            loginModal.style.display = "block";
        });
    }

    // Click outside of modal closes it
    window.addEventListener("click", function (event) {
        if (event.target === loginModal) {
            loginModal.style.display = "none";
        }
        if (event.target === registerModal) {
            registerModal.style.display = "none";
        }
    });
});
