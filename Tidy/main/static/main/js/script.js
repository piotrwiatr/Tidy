const categories = ["laptop", "desktop", "camera"]

// shows one page and hides the other two
function showPage(page) {
    for (let i = 0; i < categories.length; i++) {
        document.querySelector(`#${categories[i]}`).style.display = "none";
    }
    document.querySelector(`#${page}`).style.display = "block";
}

document.addEventListener("DOMContentLoaded", function() {
    for (let i =0; i < categories.length; i++) {
        document.querySelector(`#${categories[i]}-btn`).onclick = function() {
            page = this.dataset.page;
            showPage(page);
        }
    }
});