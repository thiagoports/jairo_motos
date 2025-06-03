document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("cartModal");
    const btn = document.getElementById("openCart");
    const span = document.getElementById("closeCart");

    if (btn && modal && span) {
        btn.onclick = function () {
            modal.style.display = "block";
        }

        span.onclick = function () {
            modal.style.display = "none";
        }

        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    } else {
        console.warn("Modal not found");
    }
});
