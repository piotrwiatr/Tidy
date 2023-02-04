document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("form").onsubmit = function() {
        const categoryForm = document.querySelector("#categories");
        const index = categoryForm.selectedIndex;
        const category = categoryForm[index].value;
        alert(`${category}`);
    };
});