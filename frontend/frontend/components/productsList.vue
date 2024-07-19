<template>
  <div>
    <theHeader :inCart="false" :inSellSomething="false"> </theHeader>
    <h2 class="text-white text-4xl text-center my-8">
      {{ formattedCategory }}
    </h2>
    <div v-if="products.length == 0">
      <h2 class="text-white text-2xl text-center my-8">
        No products for this category
      </h2>
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
    </div>

    <div class="bg-teal-650 flex flex-wrap justify-center px-6 py-3">
      <v-card
        v-for="product in products"
        :key="product.prodCode"
        class="flex-shrink-0 card"
        @click="openPopup(product)"
      >
        <v-img :src="product.image" class="prodImage" contain></v-img>
      </v-card>
    </div>

    <PopUpCard
      v-if="selectedProduct"
      :product="selectedProduct"
      @close-popup="closePopUp"
    ></PopUpCard>
    <br />
    <br />
    <br />
  </div>
</template>

<script>
import axios from "axios";
import popUpCard from "@/components/popUpCard.vue";
import { useCartStore } from "~/store/cart";
import theHeader from "./theHeader.vue";
import config from "~/config";

export default {
  components: {
    popUpCard,
    theHeader,
  },
  props: ["category"],

  data() {
    return {
      products: [],
      cartStore: useCartStore(),
      selectedProduct: null,
    };
  },

  created() {
    this.loadProducts(this.category);
  },
  computed: {
    formattedCategory() {
      if (this.category.includes("_")) {
        return this.category.replace(/_/g, " ");
      }
      if (this.category == "Tennis") {
        return "Court";
      }
      if (this.category == "Rugby") {
        return "Rugby/Soccer";
      }

      return this.category;
    },
  },
  methods: {
    loadProducts(category) {
      const params = { params: { category: category } };

      axios
        .get(config.apiUrl + config.loadProductsExt, params)
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    openPopup(product) {
      this.selectedProduct = product;
    },
    closePopUp() {
      this.selectedProduct = null;
    },
  },
};
</script>

<style scoped>
.prodImage {
  /* width: 100%; */
  height: 100%;
  object-fit: fill;
  padding: 0.5%;
}

.card {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 9rem;
  /* height: 9rem; */
  max-height: 13rem;
  margin: 0.5rem;
  background-color: #8cacaf;
}

.flex-wrap {
  flex-wrap: wrap;
}

.flex-shrink-0 {
  flex-shrink: 0;
}
</style>
