<template>

  <body>
    <header class="min-vh-100">
      <nav class="navbar navbar-expand-lg fixed-top bg-white bg-opacity-75">
        <div class="container">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01"
            aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
            <a class="navbar-brand" href="#">
              <img src="../../logo (2).png" width="50px" height="50px" alt="Medical logo" />
            </a>
            <p
              style="font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; color: #333; margin-top: 12px;">
              RenalScan Pro</p>
          </div>
        </div>
      </nav>

      <div class="container vh-100 d-flex align-items-center justify-content-center">
        <div class="row w-100">
          <div class="card col-lg-6 bg-transparent border-0 text-white">
            <div class="card-body">
              <h1 class="card-title display-3">The best doctors in <b>Medicine!</b></h1>
              <h5 class="card-subtitle mb-2">in the world of modern medicine!</h5>
              <p class="card-text my-5">Chez RenalScan Pro, nous nous engageons à faire progresser les
                diagnostics médicaux grâce à la technologie. Notre plateforme innovante exploite l'imagerie de pointe et
                l'apprentissage automatique pour détecter avec précision diverses maladies rénales à partir de simples
                téléchargements d'images. Cet outil est conçu pour soutenir les professionnels de la santé en
                fournissant des informations diagnostiques rapides et fiables, essentielles pour une intervention
                précoce et la planification du traitement.</p>
              <button class="btn btn-info bg-light text-dark border-0 rounded-0 text-uppercase"
                @click="smoothScroll('scrollPlace')" type="submit">Get
                started</button>
            </div>
          </div>
        </div>
      </div>
    </header>

    <main>
      <div id="scrollPlace" class="py-5" style="margin-bottom: 200px">
        <div class="container">
          <div class="row align-items-center">
            <div class="col-md-6 ">
              <div class="card bg-transparent border-0">
                <div class="card-body">
                  <h6 class="card-title text-mavi text-uppercase">Welcome to clinic</h6>
                  <h2 class="card-subtitle mb-2">Why you should choose us?</h2>
                  <p class="card-text my-4">En téléchargeant vos radiographies sur notre plateforme, notre modèle
                    d'intelligence artificielle analyse les images pour identifier toute anomalie rénale. Cette approche
                    permet une détection précoce des maladies rénales, améliorant ainsi les chances de traitement
                    réussi.</p>
                  <div>
                    <div style="display: flex;justify-content: space-between">
                      <div>
                        <div class="drop-area" @dragover.prevent @dragenter.prevent @drop="handleFileDrop"
                          @dragleave="handleDragLeave" @dragenter="handleDragEnter" @click="triggerFileInput">
                          <p v-if="!file">{{ dragging ? 'Drop your file here' :
                            'Drag and drop your file here, or click to select a file' }}</p>
                          <p v-else>{{ file.name }}</p>
                          <input type="file" @change="handleFileUpload" class="file-input" ref="fileInput" />
                        </div>
                        <img style="margin-bottom: 20px;" v-if="file" :src="filePreview" width="300px" height="200px">
                        <div v-if="predictedClass">Predicted Class: {{ predictedClass }}</div>
                        <div style="display:flex">
                          <button @click="TraiterImage" class="download-button"
                            style="width: 200px;height: 50px;">Traiter l'image
                          </button>
                          <div v-if="loading" class="loader" style="margin-top: 0px;"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6 text-end">
              <img src="../public/images/hekimbaba.jpg" class="mw-100" alt="Hekim baba" />
            </div>
          </div>
        </div>
      </div>

      <div class="bg-mavi">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-6 vh-50 d-flex align-items-center order-md-1" style="background-color: #6bc1f1;">
              <div class="card bg-transparent border-0 text-white text-center mx-md-5 px-md-5">
                <div class="card-body">
                  <h6 class="card-title text-uppercase">CARACTÉRISTIQUES</h6>
                  <h2 class="card-subtitle mb-2">Chirurgiens professionnels</h2>
                  <p class="card-text my-4">Dans notre clinique, nous sommes fiers de notre équipe de chirurgiens
                    hautement qualifiés et expérimentés. Chaque membre de notre équipe chirurgicale est dévoué à fournir
                    le plus haut niveau de soins et d'expertise à nos patients. Des interventions courantes aux
                    chirurgies complexes, vous pouvez avoir confiance en sachant que vous êtes entre de bonnes mains.
                    Nos chirurgiens combinent des années de formation et d'expérience avec les dernières techniques
                    chirurgicales et technologies pour garantir les meilleurs résultats possibles pour nos patients.</p>
                </div>
              </div>
            </div>
            <div class="col-md-6 vh-50 features" style="background: url('images/features1.jpg') center/cover;">
            </div>
            <div class="col-md-6 vh-50 d-flex align-items-center order-md-1" style="background-color: #6bc1f1;">
              <div class="card bg-transparent border-0 text-white text-center mx-md-5 px-md-5 ">
                <div class="card-body">
                  <h6 class="card-title text-uppercase">CARACTÉRISTIQUES</h6>
                  <h2 class="card-subtitle mb-2">Soins d'urgence pour enfants</h2>
                  <p class="card-text my-4">Notre équipe médicale spécialisée est disponible à tout moment pour fournir
                    une assistance rapide et attentive aux enfants nécessitant des soins d'urgence, garantissant ainsi
                    la tranquillité d'esprit des parents.</p>
                </div>
              </div>
            </div>
            <div class="col-md-6 vh-50 order-md-1 features"
              style="background: url('images/features2.jpg') center/cover">
            </div>
          </div>
        </div>
      </div>

      <div class="py-5">
        <div class="container">
          <div class="row ">
            <div class="col-md-4 justify-content-center flex-column">
              <div class="card my-5 border-0 align-items-center">
                <img src="../public/images/ic1.jpg" class="card-img-top serviceimgs" alt="...">
                <div class="card-body text-center">
                  <h5 class="card-title">Diagnostic Avancé</h5>
                  <p class="card-text">Accélérez le diagnostic des maladies rénales avec notre technologie
                    d'analyse d'images.</p>
                </div>
              </div>

              <div class="card border-0 align-items-center">
                <img src="../public/images/ic2.jpg" class="card-img-top serviceimgs" alt="...">
                <div class="card-body text-center">
                  <h5 class="card-title">Suivi Patient</h5>
                  <p class="card-text">Gérez efficacement le suivi des patients avec des rapports détaillés et
                    personnalisés.</p>
                </div>
              </div>
            </div>

            <div class="col-md-4 ">
              <div class="card my-5 border-0 align-items-center">
                <img src="../public/images/ic3.jpg" class="card-img-top serviceimgs" alt="...">
                <div class="card-body text-center">
                  <h5 class="card-title ">Recherche Médicale</h5>
                  <p class="card-text">Participez à l'avancement de la recherche médicale en maladies rénales
                    grâce à votre contribution.</p>
                </div>
              </div>

              <div class="card border-0 align-items-center">
                <img src="../public/images/ic4.jpg" class="card-img-top serviceimgs" alt="...">
                <div class="card-body text-center">
                  <h5 class="card-title">Consultations en Ligne</h5>
                  <p class="card-text">Consultez des spécialistes en ligne pour un conseil médical immédiat et
                    personnalisé.</p>
                </div>
              </div>
            </div>

            <div class="col-md-4">
              <div class="card my-5 border-0 align-items-center">
                <img src="../public/images/ic5.jpg" class="card-img-top serviceimgs" alt="...">
                <div class="card-body text-center">
                  <h5 class="card-title"> Urgences Médicales</h5>
                  <p class="card-text">Réagissez rapidement en cas d'urgence grâce à une orientation vers des
                    spécialistes qualifiés.</p>
                </div>
              </div>

              <div class="card border-0 align-items-center">
                <img src="../public/images/ic6.jpg" class="card-img-top serviceimgs" alt="...">
                <div class="card-body text-center">
                  <h5 class="card-title">Éducation à la Santé</h5>
                  <p class="card-text">Améliorez votre connaissance des maladies rénales avec nos ressources
                    éducatives accessibles.</p>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>

      <div class="bg-boz py-3">
        <div class="container">
          <div class="row">
            <div class="col-md-4">
              <img src="../public/images/portfolio-6.jpg" class="card-img my-5" alt="...">
              <img src="../public/images/portfolio-2.jpg" class="card-img " alt="...">
            </div>
            <div class="col-md-4">
              <img src="../public/images/portfolio-3.jpg" class="card-img my-5" alt="...">
              <img src="../public/images/portfolio-4.jpg" class="card-img" alt="...">
            </div>
            <div class="col-md-4">
              <img src="../public/images/portfolio-5.jpg" class="card-img my-5" alt="...">
              <img src="../public/images/portfolio-1.jpg" class="card-img mb-5" alt="...">
            </div>
          </div>
        </div>
      </div>
      <div class="bg-mavi py-5">
        <div class="container">
          <div class="col d-flex flex-column">
            <div class="d-flex justify-content-center mb-5">
              <div class="card-body text-center text-white w-50 d-flex flex-column">
                <h1 class="card-title">''</h1>
                <p class="card-text">This is Photoshop's version of Lorem Ipsum. Proin gravida nibh vel velit auctor
                  aliquet. Aenean sollicitudin, lorem quis bibendum auctor, nisi elit consequat ipsum, nec sagittis
                  sem
                  nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris. Morbi accumsan ipsum
                  velit. Nam nec tellus a odio tincidunt auctor a ornare odio. Sed non mauris vitae erat consequat
                  auctor eu in elit.</p>
              </div>
            </div>


            <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active bt1"
                  aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" class="bt2"
                  aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" class="bt3"
                  aria-label="Slide 3"></button>
                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" class="bt4"
                  aria-label="Slide 4"></button>
                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="4" class="bt5"
                  aria-label="Slide 5"></button>
              </div>
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <div class="carousel-caption d-flex flex-column py-3 d-md-block py-md-5">
                    <h6>Jane Galadriel</h6>
                    <p>Ceo Tengkurep</p>
                  </div>
                </div>
                <div class="carousel-item">
                  <div class="carousel-caption d-flex flex-column py-3 d-md-block py-md-5">
                    <h6>Jane Galadriel</h6>
                    <p>Ceo Tengkurep</p>
                  </div>
                </div>
                <div class="carousel-item">
                  <div class="carousel-caption d-flex flex-column py-3 d-md-block py-md-5">
                    <h6>Jane Galadriel</h6>
                    <p>Ceo Tengkurep</p>
                  </div>
                </div>
                <div class="carousel-item">
                  <div class="carousel-caption d-flex flex-column py-3 d-md-block py-md-5">
                    <h6>Jane Galadriel</h6>
                    <p>Ceo Tengkurep</p>
                  </div>
                </div>
                <div class="carousel-item">
                  <div class="carousel-caption d-flex flex-column py-3 d-md-block py-md-5">
                    <h6>Jane Galadriel</h6>
                    <p>Ceo Tengkurep</p>
                  </div>
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions"
                data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions"
                data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="py-5">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-md-4">
              <div class="mb-3">
                <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Name">
              </div>
              <div class="mb-3">
                <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="E-mail">
              </div>
              <div class="mb-3">
                <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Subject">
              </div>
              <div class="mb-3">
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"
                  placeholder="Your Message"></textarea>
              </div>
              <div class="col d-flex justify-content-center">
                <button type="button" class="btn btn-outline-primary">Middle</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <footer class="bg-goy">
      <div class="container">
        <div class="row  py-4 jus d-flex justify-content-center">
          <div class="col-md-5 text-white ">
            <h5>Medical</h5>
            <p>orem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod </p>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et
              dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
              ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate</p>
          </div>
          <div class="col-md-4 text-white ">
            <h5>New York</h5>
            <p>709 Honey Creek Dr. <br> New York <br> NY 10028</p>
            <p>1-888-299-2000 <br> yourmail@ompany.com</p>
          </div>
          <div class="col-md-3 text-white">
            <h5>London</h5>
            <p>4851 Willow Greene Drive <br> Montgomery <br> AL 36109</p>
            <p>1-888-299-2000 <br> yourmail@ompany.com</p>
          </div>
        </div>
      </div>
    </footer>

  </body>
</template>

<script setup>

import { ref, computed } from 'vue';
import axios from 'axios';

const file = ref(null);
const dragging = ref(false);

const handleFileUpload = (event) => {
  file.value = event.target.files[0];

};

const handleFileDrop = (event) => {
  event.preventDefault();
  file.value = event.target.files[0];
  dragging.value = false;

};

const handleDragEnter = () => {
  dragging.value = true;
};

const handleDragLeave = () => {
  dragging.value = false;
};

let predictedClass = ref('');
let loading = ref(false);
const TraiterImage = async () => {
  try {
    loading.value = true;
    const formData = new FormData();
    formData.append('file', file.value);

    const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    predictedClass.value = response.data.message;
    loading.value = false;
    console.log(response.data.message);
  } catch (error) {
    if (error.response) {
      console.error('Error response:', error.response.data);
    } else if (error.request) {
      console.error('Error request:', error.request);
    } else {
      console.error('Error message:', error.message);
    }
  }
};

const filePreview = computed(() => {
  if (!file.value) return ''; // Return empty string if no file is uploaded
  return URL.createObjectURL(file.value); // Return the URL of the uploaded image
});

const triggerFileInput = () => {
  document.querySelector('input[type="file"]').click();
};

function smoothScroll(targetId) {
  const targetElement = document.getElementById(targetId);
  if (targetElement) {
    targetElement.scrollIntoView({ behavior: 'smooth' });
  }
}
</script>

<style scoped>
:root {
  --mavi: #6bc1f1
}

header {
  background: url('../public/images/headerbg.jpg') center/cover
}

.bg-mavi {
  background-color: var(--mavi)
}

.bg-goy {
  background-color: #072035;
}

.bg-boz {
  background-color: #f1f1f1
}

.text-mavi {
  color: var(--mavi)
}

.vh-50 {
  min-height: 50vh;
}

.features:hover {
  opacity: .5;
}

.serviceimgs {
  width: 100px;
  height: 100px;
}

.carousel-caption,
.carousel-item {
  height: 200px;
}

.carousel-indicators button {
  width: 45px !important;
  height: 45px !important;
  border-radius: 50%;
}

.carousel-indicators button.active {
  width: 50px !important;
  height: 50px !important;
}

.carousel-inner h6 {
  text-transform: uppercase;
  letter-spacing: .1rem;
}

.carousel-inner p {
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.7);
}

footer p {
  opacity: 0.7;
  font-size: 0.8rem;
  line-height: 30px;
  color: #fff;
  font-weight: 400;
  font-family: "Roboto";
}

footer h5 {
  margin-top: 40px;
  font-size: 1.1rem;
  color: #fff;
  font-weight: 400;
  font-family: "Roboto";

}

.bt1 {
  background: url("../public/images/feature-1.jpg") center/cover;
}

.bt2 {
  background: url("../public/images/feature-2.jpg") center/cover;
}

.bt3 {
  background: url("../public/images/feature-3.jpg") center/cover;
}

.bt4 {
  background: url("../public/images/feature-4.jpg") center/cover;
}

.bt5 {
  background: url("../public/images/feature-5.jpg") center/cover;
}

#app {
  font-family: Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin: -10px;
}

.loader {
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #333;
  /* Adjust the color of the spinner */
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
  /* Apply rotation animation */
  margin: 20% auto;
  /* Adjust the margin to center the spinner */
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

body {
  overflow: hidden;
}



.drop-area {
  width: 300px;
  height: 150px;
  border: 2px dashed #ccc;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-bottom: 15px;
  cursor: pointer;
  transition: border-color 0.3s;
}

.drop-area.dragging {
  border-color: #007bff;
}

.drop-area p {
  margin: 0;
  padding: 20px;
  font-size: 16px;
  color: #666;
}

.file-input {
  display: none;
}

.file-preview {
  margin-top: 15px;
  text-align: center;
}

.image-preview {
  max-width: 100%;
  max-height: 200px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-top: 10px;
}

.download-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.download-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.download-button:hover:not(:disabled) {
  background-color: #0056b3;
}
</style>
