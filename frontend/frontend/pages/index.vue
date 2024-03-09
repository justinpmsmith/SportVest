<template>
  <div class="text-center">
    <theHeader></theHeader>
    <div class="flex flex-col items-center justify-center px-6 py-3">
      <h1 class="text-md text-white">Once Loved Sports Equipment And Shoes</h1>
      <h1 class="text-7xl text-white">SPORTVEST</h1>
    </div>

    <div class="catagories">
      <NuxtLink
        to="/products/Cricket"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md catagoryButton"
        >Cricket</NuxtLink
      >
      <NuxtLink
        to="/products/Rugby"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md catagoryButton"
        >Rugby</NuxtLink
      >
      <NuxtLink
        to="/products/Hockey"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md catagoryButton"
        >Hockey</NuxtLink
      >
      <NuxtLink
        to="/products/Golf"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md catagoryButton"
        >Golf</NuxtLink
      >
      <NuxtLink
        to="/products/shoes"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md catagoryButton"
        >Shoes</NuxtLink
      >
      <NuxtLink
        to="/products/Athletics"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md catagoryButton"
        >Athletics</NuxtLink
      >
      <NuxtLink
        to="/products/Tennis"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md catagoryButton"
        >Tennis</NuxtLink
      >
      <NuxtLink
        to="/products/other"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md catagoryButton"
        >Other</NuxtLink
      >
      <NuxtLink
        to="/products/all"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md catagoryButton"
        >All</NuxtLink
      >
      <NuxtLink
        to="/products/Horse_Riding"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md catagoryButton"
        >Horse Riding</NuxtLink
      >

      <br />
      <br />
      <br />
    </div>
  </div>
</template>
<script>
// import axios from 'axios';
import bgImg from "../assets/static/home_bg.jpeg";
import { useCartStore } from "~/store/cart";
import theHeader from "~/components/theHeader.vue";

export default {
  components: {
    theHeader,
  },
  data() {
    return {
      bg_img: bgImg,
      cartStore: useCartStore(),
    };
  },
};
</script>


<style scoped>
.text-center {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
.categories {
  padding-top: 3rem;
  padding-bottom: 4rem;
}
.catagoryButton {
  margin: 0.8rem;
  width: 25%;
}

/* Add a media query for smaller screens */
@media (max-width: 768px) {
  .text-md {
    font-size: 15px; /* Adjust the font size as needed */
  }
  .text-7xl {
    font-size: 60px; /* Adjust the font size as needed */
  }
}
</style>