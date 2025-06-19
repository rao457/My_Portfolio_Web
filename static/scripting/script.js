const img1 = document.getElementById("img1");
const img2 = document.getElementById("img2");
const togglebtn = document.getElementById("navtogglebtn");
const navLinks = document.querySelector(".nav-links")
const subBtn = document.getElementById("subBtn");
const okBtn = document.getElementById("okBtn");
const popupEl = document.getElementById("popup");
const formEl = document.getElementById("contact-form");
const url = document.getElementById('subBtn').dataset.url;


function toggleImage() {
  const isVisibile1 = img1.getAttribute("data-visibility") === "true";
  img1.setAttribute("data-visibility", !isVisibile1);
  img2.setAttribute("data-visibility", isVisibile1);
  img1.style.display = isVisibile1 ? "none" : "block";
  img2.style.display = isVisibile1 ? "block" : "none";
}

togglebtn.addEventListener("click", () => {
  navLinks.classList.toggle("show")
})

// function openPopup() {
//   popupEl.classList.add("open-popup");
// }
// function closePopup() {
//   popupEl.classList.remove("open-popup");
// }
formEl.addEventListener("submit", function(e) {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);
  fetch(url, {
    method: "POST",
    headers: {
       'X-Requested-With' : 'XMLHttpRequest'
    },
    body: formData
  })
  .then(response =>{
    if(response.ok) {
      popupEl.classList.add("open-popup");
      okBtn.addEventListener("click", () =>{
        popupEl.classList.remove("open-popup")
      })
      form.reset();
    }
  });

});
