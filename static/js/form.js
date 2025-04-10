document.addEventListener('DOMContentLoaded', function () {
    const successMessage = document.querySelector('#contact-form-section p');


    if (successMessage) {
        location.hash = 'contact-form';
    }
});