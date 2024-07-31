<template>
  <div class="text-center">
    <theHeader></theHeader>
    <div class="flex flex-col items-center justify-center px-6 py-3">
      <h1 class="text-md text-white">Once Loved Sports Equipment And Shoes</h1>
      <h1 class="text-7xl text-white">SPORTVEST</h1>
    </div>

    <div class="categories">
      <v-btn v-for="category in categories" :key="category.id" size="medium" elevation="8"
        :to="category.link"
        class="inline-block py-3 px-8 bg-teal-900 text-white rounded-md button"
        >{{ category.name }}</v-btn
      >
    </div>
  </div>
</template>

<script>
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
      categories: [
        { id: 1, name: "All", link: "/products/all" },
        { id: 2, name: "Cricket", link: "/products/Cricket" },
        { id: 3, name: "Hockey", link: "/products/Hockey" },
        { id: 4, name: "Golf", link: "/products/Golf" },
        { id: 5, name: "Shoes", link: "/products/shoes" },
        { id: 6, name: "Athletics", link: "/products/Athletics" },
        { id: 7, name: "Court", link: "/products/Tennis" }, // Assuming "Court" refers to Tennis
        { id: 8, name: "Horse Riding", link: "/products/Horse_Riding" }, // Assuming "Equin" refers to Horse Riding
        { id: 9, name: "Rugby/Soccer", link: "/products/Rugby" },
        { id: 10, name: "Cycling", link: "/products/Cycling" },
        { id: 11, name: "Trainers", link: "/products/Trainers" },
        { id: 12, name: "Other", link: "/products/Other" },



      ],
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
  display: flex;
  flex-wrap: wrap;
  justify-content: center; /* Center the links horizontally */
  padding-top: 3rem;
  padding-bottom: 4rem;
  max-width: 40rem;
  margin: 0 auto; /* Center the container itself */
}

.button {
  color: rgb(230, 226, 226); /* Adjust text color for contrast */
  background-color: rgb(19, 82, 82);
  margin: 0.3rem;
  margin-bottom: 0.8rem;
  width: 10rem;
}

@media (max-width: 768px) {
  .text-md {
    font-size: 15px; /* Adjust the font size as needed */
  }
  .text-7xl {
    font-size: 60px; /* Adjust the font size as needed */
  }
}
</style>
