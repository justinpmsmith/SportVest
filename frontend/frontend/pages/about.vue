
<template>
  <div class="centered-content categories">
    <theHeader :inCart="false" :inSellSomething="false" />

    <h1 class="text-white text-4xl text-center my-8">About Us</h1>
    <v-card class="bg-main" style="margin: 5%; padding: 2%; color: aliceblue;" elevation="8">

    <div class="card" style="width: 100%; margin: auto;">  <img class="card-img-top" src="../assets/static/aboutImg.jpeg" alt="Card image cap">
        <br>
      <div class="card-body text-center" >  <p class="card-text">
          {{ aboutText }}
        </p>
      </div>
    </div>
</v-card>
<br><br>
  </div>
</template>
  
  <script>
  import theHeader from "~/components/theHeader.vue";

  
  export default {
    components: {
      theHeader,
    },
    data() {
      return {
        aboutText:
          'Welcome to our website, where we are dedicated to helping everyone stay active and involved in sports without breaking the bank. As a hockey coach and mom of sporty kids, I understand the struggle of constantly needing new sports equipment and shoes as kids quickly outgrow them. That\'s why I have combined my passion for sports with my desire to make them more accessible to all. Our mission is simple - to provide affordable and quality sports gear so that everyone can stay active and enjoy the benefits of physical activity. With our motto "we keep you moving," we strive to keep you on the move and in the game, no matter your budget. Thank you for visiting our site, and we hope to help you find the perfect gear to keep you active and thriving in your favorite sports.',
      };
    },
    computed: {},
    methods: {},
  };
  </script>
  
<style scoped>
.bg-main {
  background-color: #286d6e;
  font: serif;
  font-size: 1.5em; /* Default font size */
}

/* Media queries for different screen sizes */
@media (max-width: 768px) {  /* Targets screens smaller than 768px */
  .bg-main {
    font-size: 1.2em;  /* Adjust font size for smaller screens */
  }
}

@media (min-width: 768px) and (max-width: 992px) {  /* Targets screens between 768px and 992px */
  .bg-main {
    font-size: 1.3em;  /* Adjust font size for medium screens (optional) */
  }
}

@media (min-width: 992px) {  /* Targets screens larger than 992px */
  .bg-main {
    font-size: 1.5em;  /* Use default font size for larger screens */
  }
}
</style>