// store/cart.js

import { defineStore } from 'pinia';

export const useCartStore = defineStore('cart', {
  state: () => {
    return{
    cartItems: {},
    inCart: false,
  }
  },
  persist: {
    storage: persistedState.localStorage,
  },
  getters: {
    cart: (state) => state.cartItems,
    inCartFlag: (state) => state.inCart,
    
  },
  actions: {
    addToCart(product) {
      
      this.cartItems[product.prodCode] = product;
    },
    removeFromCart(prodCode) {
      if (this.cartItems[prodCode]) {
        delete this.cartItems[prodCode];
      }
    },
    clearCart() {
        this.cartItems = {};
      },
      setInCartFlag(value){
        this.inCart = value;
      }
  },
});
