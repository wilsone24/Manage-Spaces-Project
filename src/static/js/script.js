/* Genera las caraceristicas de los espacios */
let products = {
  data: [
    {
      productName: "Biblioteca Karl C. Parrish Jr.",
      category: "t",
      ocuppation: "35",
    },
    {
      productName: "Casa de Estudio Alfredo Correa De Andreis",
      category: "b",
      ocuppation: "64",
    },
    {
      productName: "Bloque k salon cree",
      category: "w",
      ocuppation: "99",
    },
    {
      productName: "Bloque J sala konder",
      category: "a",
      ocuppation: "29",
    },
    {
      productName: "Bloque b piso 2",
      category: "b",
      ocuppation: "129",
    },
    {
      productName: "Bloque F piso 2",
      category: "a",
      ocuppation: "89",
    },
  ],
};

/* Crea las tarjetas con las caracteristicas de los espacios */
function createCard(product) {
  let card = document.createElement("div");
  card.classList.add("card", product.category);

  let imgContainer = document.createElement("div");
  imgContainer.classList.add("image-container");

  let container = document.createElement("div");
  container.classList.add("container");

  let name = document.createElement("h5");
  name.classList.add("product-name");
  name.innerText = product.productName.toUpperCase();
  container.appendChild(name);

  let ocuppation = document.createElement("h6");
  ocuppation.innerText = "Ocupación: " + product.ocuppation + " Personas";
  container.appendChild(ocuppation);

  card.appendChild(container);
  return card;
}
/* Muestra todos los espacios */

function displayAllProducts() {
  let productsContainer = document.getElementById("products");
  productsContainer.innerHTML = "";

  for (let product of products.data) {
    let card = createCard(product);
    productsContainer.appendChild(card);
  }
}

/* Funcion para actualizar la ocupación */

function updateOccupation() {
  let cards = document.querySelectorAll(".card");

  cards.forEach((card) => {
    let ocuppationElement = card.querySelector("h6");
    let randomOccupation = Math.floor(Math.random() * 151); // Genera un número aleatorio entre 0 y 150
    ocuppationElement.innerText = "Ocupación: " + randomOccupation + " Personas";
  });
}
/* Funcion para filtrar los elementos */

function filterProducts(searchInput) {
  let elements = document.querySelectorAll(".product-name");
  let cards = document.querySelectorAll(".card");

  elements.forEach((element, index) => {
    if (element.innerText.includes(searchInput.toUpperCase())) {
      cards[index].classList.remove("hide");
    } else {
      cards[index].classList.add("hide");
    }
  });
}
/* Filtar productos */

document.getElementById("search-input").addEventListener("input", () => {
  let searchInput = document.getElementById("search-input").value;
  filterProducts(searchInput);
});

/* Se ejecuta al iniciar */
window.onload = () => {
  displayAllProducts();
  setInterval(updateOccupation, 10000); // Actualiza la ocupación cada 10 segundos
};