document.addEventListener("DOMContentLoaded", function () {
    const questions = document.querySelectorAll(".faq-question");

    questions.forEach((q) => {
        q.addEventListener("click", function () {
            const answer = this.nextElementSibling;
            answer.style.display = answer.style.display === "block" ? "none" : "block";
        });
    });

    const search = document.getElementById("faq-search");
    search.addEventListener("input", function () {
        const term = this.value.toLowerCase();
        document.querySelectorAll(".faq-item").forEach((item) => {
            const text = item.querySelector(".faq-question").textContent.toLowerCase();
            item.style.display = text.includes(term) ? "block" : "none";
        });
    });
});
