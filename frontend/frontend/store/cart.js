// store/cart.js

import { defineStore } from 'pinia';


export const useCartStore = defineStore('cart', {
  state: () => {
    return{
    cartItems: {},
    cartTotal: 0,
    buyerInfo: {},
  }
  },
  persist: {
    storage: persistedState.localStorage,
  },
  getters: {
    cart: (state) => state.cartItems,
    getCartTotal: (state) => state.cartTotal,
    getbuyerInfo: (state) => state.buyerInfo,
  },
  actions: {
    addToCart(product) {
      if(!Object.hasOwn( this.cartItems, product.prodCode))
      {
        console.log("item already in cart")
        this.cartItems[product.prodCode] = product;
        this.cartTotal += product.price;
        return true;
      }
      console.log("item added")

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
    addBuyerInfo(info){
      this.buyerInfo = info;
      this.buyerInfo.products = this.cartItems;
    }

  },
});
