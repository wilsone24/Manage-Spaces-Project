// De reporte

// Toggle menu
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function(){
    navigation.classList.toggle("active");
    main.classList.toggle("active");
}

// Hovered class
let list = document.querySelectorAll(".navigation li");
function activeLink(){
    list.forEach((item) =>
    item.classList.remove("hovered"));
    this.classList.add("hovered");
}
list.forEach((item) =>
item.addEventListener("mouseover", activeLink));
    // Chart
// Obtén los datos de la primera gráfica
var datos1 = [302, 285, 98, 18, 24, 18];

// Crea la primera gráfica
var ctx1 = document.getElementById('chart1').getContext('2d');
var chart1 = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: ['Casa de estudio', 'Biblioteca', 'Laboratorio 5K', 'Laboratorio 6K', 'Bloque B SDU2', 'Bloque B SDU3'],
        datasets: [{
        label: 'Estudiantes en salas',
        data: datos1,
        backgroundColor: ['rgba(3, 4, 94, 0.4)', 'rgba(2, 62, 138, 0.4)', 'rgba(0, 119, 182, 0.4)', 'rgba(0, 180, 216, 0.4)', 'rgba(72, 202, 228, 0.4)', 'rgba(173, 232, 244, 0.4)'],
        borderColor: ['rgba(3, 4, 94, 1)', 'rgba(2, 62, 138, 1)', 'rgba(0, 119, 182, 1)', 'rgba(0, 180, 216, 1)', 'rgba(72, 202, 228, 1)', 'rgba(0, 150, 199, 1)'],
        borderWidth: 1
        }]
    },
    options: {
        scales: {
        y: {
            beginAtZero: true
        }
        }
    }
    });



// Obtén los datos de la segunda gráfica
var datos2 = [302, 285, 98, 18, 24, 18];

// Crea la segunda gráfica circular
var ctx2 = document.getElementById('chart2').getContext('2d');
var chart2 = new Chart(ctx2, {
type: 'doughnut',
data: {
    labels: ['Casa de estudio', 'Biblioteca', 'Laboratorio 5K', 'Laboratorio 6K', 'Bloque B SDU2', 'Bloque B SDU3'],
    datasets: [{
    data: datos2,
    backgroundColor: ['rgba(3, 4, 94, 0.4)', 'rgba(2, 62, 138, 0.4)', 'rgba(0, 119, 182, 0.4)', 'rgba(0, 180, 216, 0.4)', 'rgba(72, 202, 228, 0.4)', 'rgba(173, 232, 244, 0.4)'],
    borderColor: ['rgba(3, 4, 94, 1)', 'rgba(2, 62, 138, 1)', 'rgba(0, 119, 182, 1)', 'rgba(0, 180, 216, 1)', 'rgba(72, 202, 228, 1)', 'rgba(0, 150, 199, 1)'],
    borderWidth: 1
    }]
},
options: {
    cutout: '60%', // Controla el tamaño del círculo central abierto
    plugins: {
    legend: {
        display: false // Oculta la leyenda
    }
    }
}
});

    // Obtén todos los botones con la clase CSS 'cambio-modo'
const botonesModo = document.querySelectorAll('.cambio-modo');

// Agrega el controlador de eventos a cada botón
botonesModo.forEach(function(boton) {
boton.addEventListener('click', function() {
    // Obtén todos los elementos en los que deseas aplicar el modo nocturno
    const elementos = document.querySelectorAll('body, .navigation, .navigation ul');

    // Alternar la clase 'modo-nocturno' en cada elemento
    elementos.forEach(function(elemento) {
    elemento.classList.toggle('modo-nocturno');
    });

    const fondo = document.querySelectorAll('.cardBox, .main');
    fondo.forEach(function(elemento_fondo) {
    elemento_fondo.classList.toggle('modo-nocturno-fondo');
    });

    const navigationItems = document.querySelectorAll('.navigation ul li');
    navigationItems.forEach(function(item) {
    item.addEventListener('mouseover', function() {
        this.querySelector('a::after').style.boxShadow = '0 2px 5px rgba(255, 255, 255, 0.5)';
        this.querySelector('a::after').style.boxShadow = '0 2px 5px rgba(255, 255, 255, 0.5)';
    
    });

    item.addEventListener('mouseout', function() {
        this.querySelector('a::after').style.boxShadow = ''; // Restablecer el valor por defecto
        this.querySelector('a::before').style.boxShadow = '';
    });
});
    
});
});