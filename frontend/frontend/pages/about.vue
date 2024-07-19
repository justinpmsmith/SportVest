
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
  import config from "~/config";

  
  export default {
    components: {
      theHeader,
    },
    data() {
      return {
        aboutText:config.aboutText
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