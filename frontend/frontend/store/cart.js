// store/cart.js

import { defineStore } from "pinia";

export const useCartStore = defineStore("cart", {
  state: () => ({
    cartItems: {},
    cartTotal: 0,
    buyerInfo: {},
    shippingFee: 0,
    inactivityTimerId: null, // to store the timer ID
  }),
  persist: {
    storage: persistedState.localStorage,
  },
  getters: {
    cart: (state) => state.cartItems,
    getCartTotal: (state) => (state.cartTotal === 0 ? 0 : state.cartTotal),
    getOrderTotal: (state) => state.cartTotal + state.shippingFee,
    getbuyerInfo: (state) => state.buyerInfo,
    getShippingFee: (state) => state.shippingFee,
  },
  actions: {
    startInactivityTimer() {
      // Clear existing timer if there is one
      if (this.inactivityTimerId) {
        clearTimeout(this.inactivityTimerId);
      }
      let timeoutMins = 10;
      let timeoutMillis = timeoutMins * 60000;

      this.inactivityTimerId = setTimeout(() => {
        console.log("clearing cart")
        this.clearAll(); 
      }, timeoutMillis);
    },
    addToCart(product) {
      if (!Object.hasOwn(this.cartItems, product.prodCode)) {
        this.cartItems[product.prodCode] = product;
        this.cartTotal += product.price;
        this.startInactivityTimer();
        return true;
      }
      console.log("Item already in cart");
      return false;
    },
    removeFromCart(prodCode) {
      if (this.cartItems[prodCode]) {
        this.cartTotal -= this.cartItems[prodCode].price;
        delete this.cartItems[prodCode];
        this.startInactivityTimer(); 
      }
    },
    clearCart() {
      this.cartItems = {};
      this.cartTotal = 0;
      this.startInactivityTimer(); 
    },
    addBuyerInfo(info) {
      this.buyerInfo = info;
      this.buyerInfo.products = this.cartItems;
      this.startInactivityTimer(); 
    },
    setShippingFee(fee) {
      this.shippingFee = fee;
      this.startInactivityTimer(); 
    },
    clearAll() {
      this.clearCart();
      this.buyerInfo = {};
      this.shippingFee = 0;
      clearTimeout(this.inactivityTimerId); 
      this.inactivityTimerId = null; 
    },
  },
});
