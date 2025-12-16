// Mobile sidebar toggle
document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("sidebarToggle");
    const sidebar = document.getElementById("sidebar");

    if (toggleBtn && sidebar) {
        toggleBtn.addEventListener("click", () => {
            sidebar.classList.toggle("open");
        });
    }
});

// Smooth card hover
document.querySelectorAll(".tile").forEach(tile => {
    tile.addEventListener("mouseover", () => {
        tile.style.transition = "0.25s ease";
    });
});
