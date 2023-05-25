let products = {
    data: [
      {
        productName: "Biblioteca Karl C. Parrish Jr.",
        category: "Topwear",
        ocuppation: "35",
        image: "white-tshirt.jpg",
      },
      {
        productName: "Casa de Estudio Alfredo Correa De Andreis",
        category: "Bottomwear",
        ocuppation: "64",
        image: "short-skirt.jpg",
      },
      {
        productName: "Bloque k salon cree",
        category: "Watch",
        ocuppation: "99",
        image: "sporty-smartwatch.jpg",
      },
      {
        productName: "Bloque J sala konder",
        category: "Jacket",
        ocuppation: "29",
        image: "knitted-top.jpg",
      },
      {
        productName: "Bloque b piso 2",
        category: "Bottomwear",
        ocuppation: "129",
        image: "black-leather-jacket.jpg",
      },
      {
        productName: "Bloque F piso 2",
        category: "Jacket",
        ocuppation: "89",
        image: "pink-trousers.jpg",
      },
    ],
  };
  function createCard(product) {
    let card = document.createElement("div");
    card.classList.add("card", product.category);

    let imgContainer = document.createElement("div");
    imgContainer.classList.add("image-container");

    let image = document.createElement("img");
    image.setAttribute("src", product.image);
    imgContainer.appendChild(image);
    card.appendChild(imgContainer);

    let container = document.createElement("div");
    container.classList.add("container");

    let name = document.createElement("h5");
    name.classList.add("product-name");
    name.innerText = product.productName.toUpperCase();
    container.appendChild(name);

    let ocuppation = document.createElement("h6");
    ocuppation.innerText = "Ocupación: " +  product.ocuppation  + " Personas";
    container.appendChild(ocuppation);

    card.appendChild(container);
    return card;
  }

  function displayAllProducts() {
    let productsContainer = document.getElementById("products");
    productsContainer.innerHTML = "";

    for (let product of products.data) {
      let card = createCard(product);
      productsContainer.appendChild(card);
    }
  }

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

  document.getElementById("search-input").addEventListener("input", () => {
    let searchInput = document.getElementById("search-input").value;
    filterProducts(searchInput);
  });

  window.onload = () => {
    displayAllProducts();
  };