<template>
  <div>
    <h2 class="category-heading">{{ category }}</h2>

    <div class="bg-teal-650 flex flex-wrap justify-center px-6 py-3">
      <v-card v-for="product in products" :key="product.prodCode" class="flex-shrink-0 card" @click="openPopup(product)">
        <v-img :src="product.image" class="prodImage"></v-img>
      </v-card>
    </div>

    <PopUpCard
      v-if="selectedProduct"
      :product="selectedProduct"
      @close="closePopUp"
    ></PopUpCard>
  </div>
</template>


<script>
import axios from 'axios';
import popUpCard from '@/components/popUpCard.vue'



export default {
  components: {
    popUpCard
  },
    props:['category'],

    data(){
    return {products: [],
            selectedProduct: null,}
  },

  created() {
    this.loadProducts(this.category)
  },
  computed: {
    productFilter(category) {
        //TODO: implement product filter 
    },
  },

  methods: {
    loadProducts(category) {
      const extension = '/backend/products';
      const params = { params: { category: category } };

      axios.get('http://127.0.0.1:8000/' + extension, params) //http://127.0.0.1:8000/
        .then((response) => {
          console.log(response.data);
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
    }
  },

}
</script>

<style scoped>
.prodImage {
  width: 10rem;
  padding: 2%;
}

.flex-wrap {
  flex-wrap: wrap;
}

.flex-shrink-0 {
  flex-shrink: 0;
}
.card {
  margin: 0.5rem;
}
.category-heading {
  text-align: center;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
  color: white;
}
</style>
