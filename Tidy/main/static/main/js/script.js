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

    // document.querySelectorAll('form').forEach(form => {
    //     form.onsubmit = () => {
    //         const typeOfForm = form.parentElement.id;
    //         let screenSize = "";
    //         let brand = document.querySelector(`#${typeOfForm}-brand`).value;
    //         let condition = document.querySelector(`#${typeOfForm}-condition`).value;
    //         let price = document.querySelector(`#${typeOfForm}-price`).value;
    //         let img = document.querySelector(`#${typeOfForm}-image`).value;
    //         if (typeOfForm === "laptop") {
    //             screenSize = document.querySelector(`#${typeOfForm}-screen-size`).value;
    //         }
            
    //         returnJson = {
    //             "type":typeOfForm,
    //             "brand": brand,
    //             "screenSize": screenSize,
    //             "condition": condition,
    //             "price": price,
    //             "img": img             
    //         };
    //         console.log(returnJson);
            
    //         var image = document.createElement("img");
    //         image.src = img;
    //         document.querySelector("#test").appendChild(image);

    //         return false;
    //     }
    // });
});