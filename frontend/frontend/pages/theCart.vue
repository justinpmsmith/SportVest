<template>
  <div>
    <theHeader :inCart="true" :inSellSomething="false"> </theHeader>

    <h1 class="text-white text-4xl text-center my-8">Your Cart</h1>
    <h1
      class="text-white text-2xl text-center my-2"
      v-if="Object.keys(cartStore.cart).length"
    >
      Cart Total: R{{ cartTotal }}
    </h1>

    <div v-if="Object.keys(cartStore.cart).length">
    <!-- <h6 class="text-white  text-center">Shipping fee(flat rate): R120</h6> -->
    <p class="text-white text-center">Cart will clear after 10 minutes of inactivity</p>

      <div
        v-for="product in Object.values(cartStore.cart)"
        :key="product.prodCode"
        class="product-item card"
      >
        <v-img :src="product.image" class="prodImage"></v-img>
        <div class="product-details">
          <p class="product-name">{{ product.name }}</p>
          <p class="product-price">R{{ product.price }}</p>
        </div>
        <button @click="removeFromCart(product.prodCode)" class="remove-button">
          Remove
        </button>
      </div>
    </div>
    <!-- product list  -->

    <div v-else>
      <p class="text-white text-center">Your cart is empty</p>
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
      <br />
      <br />
    </div>
    <br />
    <br />
    <br />
    <br />
  </div>
</template>
<script>
import { useCartStore } from "~/store/cart";
import theHeader from "~/components/theHeader.vue";

export default {
  components: {
    theHeader,
  },
  data() {
    return {
      cartStore: useCartStore(),
    };
  },
  computed: {
    cartTotal() {
      let total = this.cartStore.getCartTotal;
      return total;
    },
  },
  methods: {
    removeFromCart(prodCode) {
      this.cartStore.removeFromCart(prodCode);
    },
  },
};
</script>
<style scoped>
.card {
  background-color: rgb(217, 240, 229);
  padding: 20px;
}

.product-item {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
  margin: 1rem;
}

.prodImage {
  max-width: 4rem;
  height: auto;
}

.product-details {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.product-name {
  font-weight: bold;
  font-size: 18px;
}

.product-price {
  font-size: 16px;
}
.remove-button {
  float: right; /* Position the button on the right */
  /* margin-right: 0.1rem; Adjust the desired space from the price */
  margin-left: 1rem;
  padding: 0.5rem 1rem; /* Add padding to the button for styling */
  background-color: #454343; /* Customize the button's appearance */
  color: #ffffff; /* Text color */
  border: none; /* Remove button border */
  cursor: pointer;
  font-size: 12px;
}
</style>