// store/cart.js

import { defineStore } from "pinia";

export const useCartStore = defineStore("cart", {
  state: () => {
    return {
      cartItems: {},
      cartTotal: 0,
      buyerInfo: {},
      shippingFee: 0,
    };
  },
  persist: {
    storage: persistedState.localStorage,
  },
  getters: {
    cart: (state) => state.cartItems,
    getCartTotal: (state) => {
      if (state.cartTotal == 0) {
        return 0;
      } else {
        return state.cartTotal;
      }
    },
    getOrderTotal: (state) => {
      return state.cartTotal + state.shippingFee;
    },
    getbuyerInfo: (state) => state.buyerInfo,
    getShippingFee: (state) => state.shippingFee,
  },
  actions: {
    addToCart(product) {
      if (!Object.hasOwn(this.cartItems, product.prodCode)) {
        console.log("item already in cart");
        this.cartItems[product.prodCode] = product;
        this.cartTotal += product.price;
        return true;
      }
      console.log("item added");

      return false;
    },
    removeFromCart(prodCode) {
      if (this.cartItems[prodCode]) {
        this.cartTotal -= this.cartItems[prodCode].price;
        delete this.cartItems[prodCode];
      }
    },
    clearCart() {
      this.cartItems = {};
      this.cartTotal = 0;
    },
    addBuyerInfo(info) {
      this.buyerInfo = info;
      this.buyerInfo.products = this.cartItems;
    },
    setShippingFee(fee) {
      this.shippingFee = fee;
    },
  },
});
