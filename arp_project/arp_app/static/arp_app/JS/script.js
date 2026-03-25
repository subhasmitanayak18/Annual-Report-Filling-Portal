const loginBtn = document.getElementById('loginBtn');
const loginPopup = document.getElementById('loginPopup');
const loginForm = document.getElementById('loginForm');
const layout = document.querySelector('.layout');
const footer = document.querySelector('.footer');
const imageContainer = document.querySelector('.image-container');
const forgotLink = document.getElementById('forgotLink');

// Show/hide login popup
loginBtn.addEventListener('click', (e) => {
  e.preventDefault();
  loginPopup.style.display = 'block';
  layout.classList.add('blur-background');
  footer.classList.add('blur-background');
  imageContainer.classList.add('blur-background');
});

// Forgot password (optional)
forgotLink.addEventListener('click', (e) => {
  e.preventDefault();
  alert("Password reset link sent to your registered email.");
});

// Auto-show popup if error messages exist (after failed login)
window.addEventListener('DOMContentLoaded', () => {
  if (document.querySelector('.messages li')) {
    loginPopup.style.display = 'block';
    layout.classList.add('blur-background');
    footer.classList.add('blur-background');
    imageContainer.classList.add('blur-background');
  }
});
