// store/cart.js

import { defineStore } from 'pinia';

export const useCartStore = defineStore('cart', {
  state: () => {
    return{
    cartItems: {},
    inCart: false,
    inHome:true,
    inSellSomething: false, 
  }
  },
  persist: {
    storage: persistedState.localStorage,
  },
  getters: {
    cart: (state) => state.cartItems,
    inCartFlag: (state) => state.inCart,
    inHomeFlag: (state) => state.inHome,
    inSellSomethingFlag: (state) => state.inSellSomething,
    
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
      },
      setInHomeFlag(value){
        this.inHome = value;
      },
      setInSellSomethingFlag(value){
        this.inSellSomething = value;
      }
  },
});
