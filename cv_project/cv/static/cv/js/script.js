// Memunculkan section dengan halus saat masuk layar
document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".reveal");

    if (!("IntersectionObserver" in window)) {
        items.forEach((el) => el.classList.add("is-visible"));
        return;
    }

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.1 }
    );

    items.forEach((el) => observer.observe(el));

    // Tutup menu mobile setelah link diklik
    const menu = document.getElementById("navMenu");
    if (menu && window.bootstrap) {
        menu.querySelectorAll(".nav-link").forEach((link) => {
            link.addEventListener("click", () => {
                const instance = bootstrap.Collapse.getInstance(menu);
                if (instance && menu.classList.contains("show")) instance.hide();
            });
        });
    }
});