<template>
  <nav class="flex flex-col md:flex-row items-center justify-center">
    <!-- Center the logo and buttons -->
    <div class="logo-container">
      <div @click="goHome">
        <img
          src="../assets/static/logo-no-bg.png"
          alt="Home"
          class="logo-image"
        />
      </div>
    </div>

    <div
      class="button-container mt-4"
      v-if="!inCart && !inSellSomething"
      style="margin-bottom: 1rem"
    >
      <NuxtLink
        to="/sellSomething"
        class="py-3 px-6 bg-gray-800 text-white rounded-md whitespace-nowrap font-bold nav-links"
      >
        Sell Something
      </NuxtLink>

      <NuxtLink
        to="/theCart"
        class="py-3 px-6 bg-gray-800 text-white rounded-md whitespace-nowrap font-bold nav-links"
        style="display: flex; align-items: center"
      >
        Cart
        <span style="margin-left: 0.5rem">
          <Icon name="material-symbols:shopping-cart-sharp" color="white" />
        </span>
      </NuxtLink>
    </div>

    <div class="button-container mt-4" v-else-if="inCart">
      <div
        v-if="Object.keys(cartStore.cart).length"
        @click="clearCart"
        class="py-3 px-6 bg-gray-800 text-white rounded-md whitespace-nowrap font-bold nav-links"
      >
        Clear Cart
      </div>

      <div
        v-if="Object.keys(cartStore.cart).length"
        @click="checkout"
        class="py-3 px-6 bg-gray-800 text-white rounded-md whitespace-nowrap font-bold nav-links"
        style="display: flex; align-items: center"
      >
        Checkout
        <span style="margin-left: 0.5rem">
          <Icon name="material-symbols:shopping-cart-sharp" color="white" />
        </span>
      </div>
    </div>
    <div class="button-container mt-4" v-else-if="inSellSomething">
      <NuxtLink
        to="/theCart"
        class="py-3 px-6 bg-gray-800 text-white rounded-md whitespace-nowrap font-bold nav-links"
        style="display: flex; align-items: center"
      >
        Cart
        <span style="margin-left: 0.5rem">
          <Icon name="material-symbols:shopping-cart-sharp" color="white" />
        </span>
      </NuxtLink>
    </div>
  </nav>
</template>

<script>
import { useCartStore } from "~/store/cart";
export default {
  props: {
    inSellSomething: {
      type: Boolean,
      default: false, // Default value if the prop is not provided
    },
    inCart: {
      type: Boolean,
      default: false, // Default value if the prop is not provided
    },
  },
  data() {
    return {
      cartStore: useCartStore(),
    };
  },
  methods: {
    clearCart() {
      this.cartStore.clearCart();
    },
    checkout() {
      this.$router.push("/checkout");
    },
    goHome() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.site-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center; /* Vertically center the content */
  align-items: center; /* Horizontally center the content */
}

.logo-container {
  display: flex;
  justify-content: center; /* Center the logo horizontally */
  margin: 2rem;
}

.logo-image {
  width: 40%;
  height: auto;
}

/* Styles for screens with a maximum width of 600px (adjust as needed) */
@media (max-width: 780px) {
  .logo-image {
    margin-left: 32%;
  }
}

.button-container {
  display: flex;
  justify-content: center; /* Center the buttons horizontally */
  align-items: center;
  margin-top: 1rem;
}

.nav-links {
  display: flex;
  align-items: center;
  margin-right: 1rem;
}
</style>