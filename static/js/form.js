document.addEventListener('DOMContentLoaded', function () {
    const successMessage = document.querySelector('#contact-form-section p');

    // Если сообщение об успехе или ошибке есть — прокрутим к форме
    if (successMessage) {
        location.hash = 'contact-form';
    }
});