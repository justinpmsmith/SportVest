// store/cart.js

import { defineStore } from 'pinia';

export const useCartStore = defineStore('cart', {
  state: () => ({
    cartItems: {},
  }),
  getters: {
    cart: (state) => state.cartItems,
  },
  actions: {
    addToCart(product) {
      const { prodCode } = product;
      if (!this.cartItems[prodCode]) {
        this.cartItems[prodCode] = { ...product, quantity: 1 };
      } else {
        this.cartItems[prodCode].quantity += 1;
      }
    },
    removeFromCart(prodCode) {
      if (this.cartItems[prodCode]) {
        if (this.cartItems[prodCode].quantity > 1) {
          this.cartItems[prodCode].quantity -= 1;
        } else {
          delete this.cartItems[prodCode];
        }
      }
    },
    clearCart() {
        this.cartItems = {};
      },
  },
});
